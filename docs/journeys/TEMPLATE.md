# Journey One-Pager Template

> Status: template  
> Owner: founder / engineering  
> Last updated: 2026-06-06  
> Source of truth for: turning a product journey into a dogfood-ready regression target

## Product Promise

What the user should believe after this journey works. Keep this in user language.

## Canonical User Story

As a traveler, I want to ..., so that ...

## Why This Journey Matters

- What production risk this exposes.
- Which part of the product vision it protects.
- Why mock dogfood might miss the failure.

## Starting State

- User persona:
- Trip state:
- Device / permission state:
- Mock fixture or backend seed:
- Required feature flags:

## Primary Surfaces

- Routes:
- App docs:
- Backend docs:
- Existing test anchors:

## Canonical Steps

1. Start from ...
2. Tap / enter ...
3. Confirm ...
4. Move to ...
5. End at ...

## Expected Outcome

- User-visible state:
- Data state:
- Cross-surface coherence:
- Privacy / trust state:

## Must Never Happen

- No private fact leaks.
- No no-op CTA with a visible affordance.
- No fake success if persistence failed.
- No stranded route after an action.
- No mock-only assumption unless the journey labels it.

## AI Trace Prompt

```text
Trace this journey from the app routes, components, hooks, API interface, mock fallback, and backend endpoint if present. For each step, report:
- screen and route
- component or hook handling the action
- API method or mutation
- mock behavior
- likely real-backend drift
- deterministic test that should exist
- any no-op CTA, missing param, privacy leak, or stale state risk
Do not call live LLM-backed product endpoints unless explicitly requested.
```

## Promotion Rule

This journey can move from draft to dogfood canary only when:

- Static route/API trace is clean.
- Mock-mode journey is walkable.
- Relevant deterministic tests pass.
- Any real-backend-only risk has a clear live canary rubric.

