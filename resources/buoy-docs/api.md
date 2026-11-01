---
title: "Power activity API"
summary: "Balance a macOS native activity token around user-requested work."
category: "Reference"
order: 20
keywords: ["poweractivity", "power", "activity", "API", "lifecycle"]
symbols: ["PowerActivitySupported", "PowerActivity", "PowerActivity.IsActive", "PowerActivity.Close"]
related: ["index.md", "getting-started.md", "typed-api.md"]
---

# Power activity API

Import the `poweractivity` package. Constructors below use the class name; invoke them with `New`. Listed members are public client APIs; native declarations and trampoline helpers are implementation details.

## Public surface

| Symbol | Contract |
| --- | --- |
| `PowerActivitySupported() As Boolean` | Checks for the macOS implementation without beginning an activity. |
| `PowerActivity(reason As String, preventIdleSleep As Boolean = False, keepDisplayAwake As Boolean = False)` | Begins one native activity. Supply a user-facing reason; both prevention options default false. |
| `PowerActivity.IsActive As Boolean` | Read-only ownership state; false after Close. |
| `PowerActivity.Close()` | Idempotently ends the owned activity and releases its native token. |
| `PowerActivity.RefreshUserActivity()` | Optional local user-activity reporting using IOKit, separate from sleep/display prevention. May wake the display. Throws after Close. |

## Ownership and timing

Keep one token alive for the lifetime of a task and Close it in Finally. Close is idempotent and destruction is a final safeguard. Each object balances exactly its own native begin/end activity and retains the native token. Do not concurrently Close the same object.

For media-player style keep-awake behavior, explicitly select `preventIdleSleep: True`
and `keepDisplayAwake: True`, hold the token during the task, then Close. No
periodic refresh or user-activity reporting is required for sleep/display prevention.

Separately, `RefreshUserActivity()` can report local activity. If used continuously,
call it before the configured idle timeout. This uses `IOPMAssertionDeclareUserActivity` with
`kIOPMUserActiveLocal` and tracks the returned assertion ID across refreshes.
Close releases the current ID; the last activity may still affect the next idle
deadline. Defaults and constructor behavior are unchanged.

This reports activity rather than changing screen-saver preferences. It does not
unlock a session, dismiss a manually started screen saver, override managed lock
policies, or guarantee all screen savers are suppressed. A display-sleep token
alone does not control screen savers. No privacy grant is required. Native errors
from the refresh API throw Exception. Confine refresh and Close to one caller thread.

## Errors and result interpretation

A blank reason and unsupported-platform construction throw InvalidArgumentException. Failure to obtain a native token throws Exception. The default options do not request idle-system or display-sleep prevention.

## Platform behavior

PowerActivitySupported is true on macOS and false elsewhere. Construction on unsupported platforms throws. Activity options do not prevent manual sleep, shutdown, exhausted-battery sleep, or system-enforced suspension.

See the [complete usage example](getting-started.md) and the [package overview](index.md).


[Full typed API: properties, parameters, defaults, and returns](typed-api.md)
