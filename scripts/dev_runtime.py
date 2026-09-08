#!/usr/bin/env python3
"""Start one explicitly owned dev runtime; propagate failures and stop owned groups."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import signal
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def runtime_environment(root=ROOT):
    manifest = root / ".workspace-lane.json"
    runtime = json.loads(manifest.read_text())["runtime"] if manifest.exists() else {}
    if runtime and runtime.get("ownership") != "isolated":
        raise ValueError(
            "Dev launcher requires an isolated runtime; shared stacks need their operator runbook"
        )
    env = os.environ.copy()
    project = runtime.get("compose_project") or (
        "travel-agent"
        if root.name == "travel-workspace"
        else "vesper-" + hashlib.sha256(str(root).encode()).hexdigest()[:10]
    )
    defaults = {
        "COMPOSE_PROJECT_NAME": project,
        "POSTGRES_HOST_PORT": str(runtime.get("postgres_port", 15432)),
        "QDRANT_HOST_PORT": str(runtime.get("qdrant_port", 6333)),
        "QDRANT_GRPC_HOST_PORT": str(runtime.get("qdrant_grpc_port", 6334)),
        "API_PORT": str(runtime.get("api_port", 8000)),
        "EXPO_PORT": str(runtime.get("expo_port", 8081)),
    }
    # Lane file is the resource assignment; conflicting ambient environment
    # should not silently point this checkout at another session's services.
    for key, value in defaults.items():
        if runtime and key in env and env[key] != value:
            raise ValueError(f"{key} conflicts with this lane runtime")
        env.setdefault(key, value)
    env.setdefault(
        "DATABASE_URL",
        f"postgresql://vesper:localdev@localhost:{env['POSTGRES_HOST_PORT']}/vesper",
    )
    from urllib.parse import urlsplit

    target = urlsplit(env["DATABASE_URL"])
    if (
        target.hostname not in {"localhost", "127.0.0.1"}
        or target.port != int(env["POSTGRES_HOST_PORT"])
        or target.path != "/vesper"
    ):
        raise ValueError(
            "DATABASE_URL does not identify this lane Compose database; credentials omitted"
        )
    env["QDRANT_URL"] = f"http://localhost:{env['QDRANT_HOST_PORT']}"
    env["EXPO_PUBLIC_API_URL"] = f"http://localhost:{env['API_PORT']}"
    env["PYTHONPATH"] = "."
    return env


def stop_owned(processes):
    for process in processes:
        # Kill the process group even if its leader exited (reload workers).
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
    deadline = time.monotonic() + 3
    while any(p.poll() is None for p in processes) and time.monotonic() < deadline:
        time.sleep(0.05)
    for process in processes:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait()


def wait_ready(process, url, timeout=60):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        code = process.poll()
        if code is not None:
            raise subprocess.CalledProcessError(code or 1, process.args)
        try:
            with urllib.request.urlopen(url, timeout=0.5) as response:
                if response.status == 200:
                    return
        except OSError:
            pass
        time.sleep(0.1)
    raise TimeoutError(f"Service readiness timed out: {url}")


def supervise(commands, env, timeout=60):
    processes = []
    try:
        for name, command, cwd, url in commands:
            process = subprocess.Popen(
                command, cwd=cwd, env=env, start_new_session=True
            )
            processes.append(process)
            wait_ready(process, url, timeout)
            print(f"{name} ready: {url}", flush=True)
        while True:
            for process in processes:
                code = process.poll()
                if code is not None:
                    return code if code > 0 else 1
            time.sleep(0.1)
    finally:
        stop_owned(processes)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-expo", action="store_true")
    parser.add_argument("--no-migrate", action="store_true")
    parser.add_argument(
        "--print-runtime",
        action="store_true",
        help="Show resource ownership without starting services or credentials",
    )
    parser.add_argument(
        "--check-services",
        action="store_true",
        help="Bounded read-only check of this lane Compose Postgres",
    )
    args = parser.parse_args()
    env = runtime_environment()
    if args.check_services:
        subprocess.run(
            [
                "docker",
                "compose",
                "exec",
                "-T",
                "postgres",
                "pg_isready",
                "-U",
                "vesper",
            ],
            cwd=ROOT / "travel-agent",
            env=env,
            check=True,
            timeout=15,
        )
        return 0
    if args.print_runtime:
        print(
            json.dumps(
                {
                    key: env[key]
                    for key in (
                        "COMPOSE_PROJECT_NAME",
                        "POSTGRES_HOST_PORT",
                        "QDRANT_HOST_PORT",
                        "QDRANT_GRPC_HOST_PORT",
                        "API_PORT",
                        "EXPO_PORT",
                    )
                },
                indent=2,
            )
        )
        return 0
    backend = ROOT / "travel-agent"
    python = str(backend / ".venv/bin/python")
    if not Path(python).is_file():
        raise ValueError("Install backend dependencies in travel-agent/.venv first")
    if not shutil.which("docker") or (not args.no_expo and not shutil.which("npx")):
        raise ValueError("Required Docker/npx tooling is unavailable")
    # Refuse a port already serving a different API/Metro, before any migration.
    for key in ("API_PORT",) if args.no_expo else ("API_PORT", "EXPO_PORT"):
        with socket.socket() as sock:
            sock.bind(("127.0.0.1", int(env[key])))
    subprocess.run(
        ["docker", "compose", "up", "-d", "--wait", "--wait-timeout", "60"],
        cwd=backend,
        env=env,
        check=True,
        timeout=180,
    )
    if not args.no_migrate:
        subprocess.run(
            [python, "-m", "alembic", "upgrade", "head"],
            cwd=backend,
            env=env,
            check=True,
            timeout=180,
        )
    commands = [
        (
            "API",
            [
                python,
                "-m",
                "uvicorn",
                "backend.api.main:app",
                "--reload",
                "--port",
                env["API_PORT"],
            ],
            backend,
            f"http://127.0.0.1:{env['API_PORT']}/health",
        )
    ]
    if not args.no_expo:
        commands.append(
            (
                "Expo",
                ["npx", "expo", "start", "--port", env["EXPO_PORT"]],
                ROOT / "travel-app",
                f"http://127.0.0.1:{env['EXPO_PORT']}/status",
            )
        )
    return supervise(commands, env)


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, lambda *_: (_ for _ in ()).throw(KeyboardInterrupt()))
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
    except subprocess.CalledProcessError as exc:
        print(f"Dev process failed (status {exc.returncode})", file=sys.stderr)
        raise SystemExit(exc.returncode if exc.returncode > 0 else 1)
    except (OSError, ValueError, TimeoutError, subprocess.TimeoutExpired) as exc:
        print(f"Dev startup failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
