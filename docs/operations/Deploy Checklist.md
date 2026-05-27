# Deploy Checklist

**Companion to** [`docs/Deploy & Rollback Runbook.md`](../Deploy%20&%20Rollback%20Runbook.md).
That doc covers *how* to deploy. This one covers *what to verify before, during, and
after* — the sanity checks that catch state mismatches and env drift before they
become 30-minute debugging sessions.

Origin: written 2026-05-27 after a session where two unmerged feature branches +
a baked-in env mismatch produced 8 API errors that looked like "the deploy is
broken" but were actually "we never deployed the merge."

---

## 1. Before you deploy — verify state matches your mental model

The single most expensive failure mode is "I thought we deployed that." Always run
these three checks before debugging "missing endpoints" or "stale data":

```bash
# 1. Is your local branch synced with origin? Are PRs actually merged?
cd ~/travel-workspace/travel-agent && git fetch && git status
gh pr list --state all --search "branch:codex/..." --limit 5

# 2. What commit is currently deployed?
fly status --app vesper-backend     # look at Image: tag + LAST UPDATED

# 3. Smoke a known recent route to confirm code is live.
#    404 == route missing from deploy. 401 == route present, auth required (good).
curl -s -o /dev/null -w "%{http_code}\n" https://vesper-backend.fly.dev/api/atlas/home
```

If `git log main..origin/main` shows commits you don't recognize, pull before
deploying. If `fly status` shows a stale image tag, the deploy you remember
running may have actually failed.

---

## 2. CI failures: code vs. infrastructure

Failing checks under 5 seconds are almost never code failures. Common reasons:

- **GitHub Actions billing exhausted** — message: "The job was not started because
  recent account payments have failed." Fix at <https://github.com/settings/billing>
  before merging anything, otherwise you're flying blind on every PR. Workaround
  is `gh pr merge --admin` but you lose CI signal.
- **Workflow YAML syntax error** — surfaces as "Invalid workflow file" on a single
  setup step.
- **Missing secret** — failing job's first step references `${{ secrets.X }}`.

Always click into the first failing job before assuming the code is broken.

---

## 3. Frontend env: it's baked in at build time

`EXPO_PUBLIC_*` variables are inlined into the JS bundle at **build** time, not
runtime. Consequences:

- Editing `.env` does not change a running app. **Rebuild and reinstall** to pick up changes.
- A build profile (`development` / `dogfood` / `preview` / `production` in
  `eas.json`) overrides `.env` with its own `env:` block. Know which profile
  you're using.
- **Common 401 cascade**: `EXPO_PUBLIC_SKIP_AUTH=true` + `EXPO_PUBLIC_USE_MOCK_API=false`
  + real `EXPO_PUBLIC_API_URL` → app sends no auth token to a real backend, every
  protected request returns 401. Either both flags must skip auth (mock mode),
  or neither (real auth via Clerk).

When in doubt, dump the active env in the running app via a debug overlay (we
have `QueryHealthOverlay`) rather than guessing from `.env`.

---

## 4. Build-environment papercuts (macOS local builds)

Pre-flight checks that prevent the most painful local-build failures:

| Symptom | Root cause | Fix |
|---|---|---|
| CocoaPods crashes with `URI::File.build` or ASCII-8BIT encoding error | Path has spaces, or shell locale isn't UTF-8 | Rename folder to no-spaces; prefix commands with `LANG=en_US.UTF-8` |
| `actool` fails with `Operation not permitted` during device build | Project lives in `~/Documents/` (macOS TCC blocks `actool` access) | Move project out of `~/Documents/` (e.g., `~/travel-workspace`) |
| App boots to splash, JS runs, but `Views = 0` in perf monitor | iOS 26 + Hermes + Fabric + stale native modules ([expo/expo#44925](https://github.com/expo/expo/issues/44925)) | `cd travel-app && npx expo prebuild --clean -p ios` then rebuild |
| `expo run:ios` errors with `LockdowndClient.startSession TypeError` | Expo CLI iOS 26 lockdown protocol bug | Build with xcodebuild, install with `xcrun devicectl device install app` |
| Build fails on "Upload Debug Symbols to Sentry" step | Sentry org not configured | `SENTRY_DISABLE_AUTO_UPLOAD=true SENTRY_ALLOW_FAILURE=true` |
| Xcode "Failed to load container for document at url" | Stale xcuserdata after folder rename | `rm -rf ios/TravelApp.xcworkspace/xcuserdata` and reopen |

For physical device JS debugging, use **Chrome at `chrome://inspect`**, not
Safari Web Inspector. Hermes contexts only register with Chrome. Add
`localhost:8081` to "Discover network targets" if no targets appear.

---

## 5. After you deploy — verify the change is live

Don't trust "Deploy successful" — verify the artifact is doing the thing.

```bash
# Backend
fly status --app vesper-backend                              # version bumped?
curl https://vesper-backend.fly.dev/healthz                  # alive
curl -s -o /dev/null -w "%{http_code}\n" \
  https://vesper-backend.fly.dev/api/<new-route>             # 200 or 401, NOT 404

# Frontend
xcrun devicectl device info apps --device <udid> | grep com.fyan.vesper
# Check build number + install timestamp against your local DerivedData
```

If a frontend env change was the goal: force-quit the app and relaunch. The dev
client caches the JS bundle; force-quit forces a re-fetch from Metro. If even
that doesn't pick up the change, the build itself doesn't include it — the env
was baked in *before* you edited `.env`.

---

## 6. Branch hygiene during multi-PR features

When several feature branches build on each other and squash-merge to main:

1. **Squashed branches show as "N commits ahead of main" even after merging** —
   `git log main..<branch>` shows the original commits, but the squash is on main
   with a different SHA. Verify by content (look for the PR's merge commit by title)
   not commit count.

2. **If your local WIP sits on top of a squash-merged branch**, the cleanest path
   to ship the WIP:

   ```bash
   git checkout -b new-branch-name                  # branch off your WIP state
   git add . && git commit -m "..."                 # commit WIP
   git push -u origin new-branch-name
   gh pr create
   ```

   When that PR conflicts with main (because main has the squash and your branch
   has the original commits), resolve with `git merge origin/main -X ours` —
   your branch *is* the newer state by construction.

3. **Delete merged branches both locally and on origin.** GitHub doesn't auto-delete
   when you squash-merge unless you opt in. `gh pr merge --delete-branch` handles
   both. For cleanup after the fact:

   ```bash
   git branch -D <name>                                                    # local
   gh api -X DELETE repos/<owner>/<repo>/git/refs/heads/<branch-name>      # remote
   ```

---

## 7. Quick recovery — "I don't know what's deployed"

Run all of these. The intersection is ground truth:

```bash
# What does GitHub think is on main?
gh api repos/fy538/travel-agent/commits/main --jq '.sha + " " + .commit.message'

# What did Fly actually deploy?
fly releases --app vesper-backend | head -5

# What does the live API actually serve?
curl -s https://vesper-backend.fly.dev/openapi.json | jq -r '.info.version'

# What does my local think is current?
git log -1 main --format="%h %s"
```

If all four agree, you know the state. If they disagree, the disagreement is
the bug.
