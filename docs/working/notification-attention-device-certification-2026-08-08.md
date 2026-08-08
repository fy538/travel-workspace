---
title: Notification attention device certification matrix
status: active
owner: product-and-platform
created: 2026-08-08
date: 2026-08-08
doc_type: working
why_new: "Make the physical-device release boundary explicit after implementing the notification attention projection contract."
expires: 2026-08-30
scope: proactive signal → Activity → push → current truth
---

# Purpose

This matrix is the release boundary for notification presentation behavior.
Backend and mock tests prove contracts; they do not prove OS presentation,
lock-screen redaction, Focus/Doze behavior, or accessibility on a real device.

## Matrix

| Scenario | iOS simulator | iOS physical device | Android physical/emulator | Evidence / next action |
| --- | --- | --- | --- | --- |
| Activity normal/loading/error/offline states | Passed on iPhone 16 Pro simulator | Pending | Pending | Maestro `generated/stability/notifications.yaml` |
| Foreground receipt refreshes Activity without duplicate in-app toast | Mock/unit covered | Pending | Pending | `PushRegistrar` receipt path + device observation |
| Tap resolves current truth and deep-links | Mock/unit covered | Pending | Pending | Resolver contract + tap route tests; exercise with live delivery |
| Auth detour returns to intended trip/object | Mock/unit covered | Pending | Pending | Pending intent + post-auth tests; exercise with expired/current delivery |
| Private lock-screen copy | Not representative | Pending | Pending | Verify redacted text and no private metadata on lock screen |
| Focus / interruption-level behavior | Not representative | Pending | Pending | Verify passive vs active vs time-critical presentation |
| Android channel importance/visibility | N/A | N/A | Pending | Verify `vesper_channels_v2`, private visibility, user overrides |
| Android Doze / provider drop reconciliation | N/A | N/A | Pending | Force Doze/drop; confirm Activity refetch and no false read state |
| Replacement/collapse behavior | Not representative | Pending | Pending | Send same `presentation_key` with changed truth; verify one current row |
| Badge behavior across account switch | Mock/unit covered | Pending | Pending | Verify server-authoritative count and no prior-account carry-over |
| Accessibility (VoiceOver/TalkBack, Dynamic Type, reduced motion) | Partial UI smoke | Pending | Pending | Run screen reader and large-text pass on both OSes |

## Environment observed

- iOS 18.2 simulator: iPhone 16 Pro, booted; notification stability flow passed.
- iOS 18.2 simulator: iPhone 16, booted.
- Android: no `adb` device or emulator is available in this workspace.

## Exit criteria

Mark this matrix `certified` only after a live Expo/EAS build has passed the
physical iOS and Android rows above, with screenshots or recordings for
lock-screen privacy, Focus/Doze, replacement, badge, deep-link recovery, and
VoiceOver/TalkBack. Until then the implementation is code-complete but the OS
presentation journey remains uncertified.
