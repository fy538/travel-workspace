#!/usr/bin/env python3
"""Run a command with fresh, non-printed Clerk dogfood session tokens.

The Clerk Backend API creates a short-lived session JWT in two steps: create a
session for the known test user, then mint a token from that session. This
wrapper places those JWTs only in the child process environment and revokes the
temporary sessions afterward; it never prints or persists token values.

Requires ``CLERK_SECRET_KEY`` from the same Clerk instance as the linked
dogfood accounts.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any

API_BASE = os.environ.get("CLERK_API_BASE", "https://api.clerk.com/v1").rstrip("/")
PERSONA_USER_IDS = {
    "elif": "user_3G621LSmNvoI83lwBU3cOsNeGq4",
    "mara": "user_3G61xwb0fxRgMjBfRba8Rvgox4F",
    "dao": "user_3G8xNde9WFwJGRqKMpylrsD24fj",
    "reza": "user_3G8xSMAIFayifJeEgeAfxxvmz6Z",
    "mike": "user_3GFchXnB2br5CQVtPbTKvMyStXt",
    "sarah": "user_3GFclYhqEnGKH7QQXwlng2r6nhs",
}
ENV_NAME_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")


@dataclass(frozen=True)
class PersonaEnv:
    persona: str
    env_name: str


class ClerkSessionError(RuntimeError):
    pass


def _request(secret: str, method: str, path: str, body: dict[str, Any] | None = None) -> dict:
    payload = None if body is None else json.dumps(body).encode("utf-8")
    request = urllib.request.Request(
        f"{API_BASE}{path}",
        data=payload,
        method=method,
        headers={
            "Authorization": f"Bearer {secret}",
            "Content-Type": "application/json",
            "User-Agent": "vesper-dogfood-cert/1.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise ClerkSessionError(f"Clerk {method} {path} failed with HTTP {exc.code}") from exc
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise ClerkSessionError(f"Clerk {method} {path} failed: {type(exc).__name__}") from exc


def _create_session(secret: str, user_id: str) -> str:
    response = _request(secret, "POST", "/sessions", {"user_id": user_id})
    session_id = response.get("id")
    if not isinstance(session_id, str) or not session_id:
        raise ClerkSessionError("Clerk session response did not include an id")
    return session_id


def _mint_token(secret: str, session_id: str) -> str:
    response = _request(secret, "POST", f"/sessions/{session_id}/tokens", {})
    token = response.get("jwt")
    if not isinstance(token, str) or not token:
        raise ClerkSessionError("Clerk token response did not include a jwt")
    return token


def _revoke_session(secret: str, session_id: str) -> None:
    _request(secret, "POST", f"/sessions/{session_id}/revoke", {})


def _parse_persona_env(value: str) -> PersonaEnv:
    persona, separator, env_name = value.partition("=")
    if not separator or persona not in PERSONA_USER_IDS or not ENV_NAME_RE.fullmatch(env_name):
        allowed = ", ".join(sorted(PERSONA_USER_IDS))
        raise argparse.ArgumentTypeError(
            f"expected PERSONA=ENV_NAME with persona in: {allowed}"
        )
    return PersonaEnv(persona=persona, env_name=env_name)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--persona-env",
        action="append",
        required=True,
        type=_parse_persona_env,
        help="Map a known dogfood persona to a child-process environment variable.",
    )
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)

    command = list(args.command)
    if command[:1] == ["--"]:
        command = command[1:]
    if not command:
        parser.error("a command is required after --")

    secret = os.environ.get("CLERK_SECRET_KEY", "").strip()
    if not secret:
        print("CLERK_SECRET_KEY is required to mint dogfood sessions", file=sys.stderr)
        return 2

    child_env = os.environ.copy()
    # The child needs the minted JWTs, never the Clerk backend credential.
    child_env.pop("CLERK_SECRET_KEY", None)
    temporary_sessions: list[str] = []
    minted: list[str] = []
    try:
        for mapping in args.persona_env:
            if child_env.get(mapping.env_name, "").strip():
                continue
            session_id = _create_session(secret, PERSONA_USER_IDS[mapping.persona])
            temporary_sessions.append(session_id)
            child_env[mapping.env_name] = _mint_token(secret, session_id)
            minted.append(f"{mapping.persona}->{mapping.env_name}")

        if minted:
            print(f"Minted temporary Clerk session(s): {', '.join(minted)}")
        completed = subprocess.run(command, env=child_env, check=False)
        return completed.returncode
    except ClerkSessionError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    finally:
        for session_id in temporary_sessions:
            try:
                _revoke_session(secret, session_id)
            except ClerkSessionError:
                print(
                    "Warning: could not revoke one temporary Clerk session; "
                    "its short-lived token will expire automatically.",
                    file=sys.stderr,
                )


if __name__ == "__main__":
    raise SystemExit(main())
