# PowerActivity · 0.1.0

`Import poweractivity` exposes a scoped native macOS activity token:
`New PowerActivity(reason, preventIdleSleep = False, keepDisplayAwake = False)`.
`PowerActivitySupported()` is true on macOS, false elsewhere; unsupported
construction throws explicitly.

Keep the object alive while performing a user-requested export/download/task.
Call `Close()` in `Finally`; it is idempotent. `IsActive` reports whether this
object still owns a token, and destruction calls Close as a final safeguard.
Each object balances exactly its own NSProcessInfo begin/end activity and retains
its native token until completion. Objects are not safe for concurrent Close calls.

The default uses `NSActivityUserInitiatedAllowingIdleSystemSleep`: it marks
user-initiated work without preventing idle system sleep. The two explicit options
add idle-system-sleep/display-sleep prevention. These activities do not prevent
manual sleep, shutdown, exhausted-battery sleep or system-enforced suspension.
No activity begins on import, and nothing is installed or persisted.

## Keep a GUI test session awake

Use `New PowerActivity("Running GUI tests", preventIdleSleep: True, keepDisplayAwake: True)`
to prevent idle system and display sleep until `Close()`, like a media player.
Keep the token alive while the task runs, then Close in Finally. No timer,
periodic refresh, or synthetic input is needed for sleep/display prevention.
See the compiler-checked [example](../examples/poweractivity_keep_awake.bui).

### Optional explicit user activity

`activity.RefreshUserActivity()` separately reports local user activity. Use it
only when activity reporting is intended; it is not required for the scoped
keep-awake behavior above. If used continuously, call periodically at an interval
shorter than the configured idle timeout (for example every 15 seconds).

The user-activity API can wake a sleeping display and postpones idle behavior;
it does not unlock a locked session, dismiss a manually started screen saver,
override managed lock policies, or guarantee every screen saver is inhibited.
Display-sleep prevention alone is not a screen-saver control. `Close()` releases
the current user-activity assertion as well as the process activity; macOS may
still count the last reported activity when calculating its next idle timeout.
Calling `RefreshUserActivity()` after Close throws `InvalidArgumentException`.
No privacy permission is required and no sleep, screen-saver, or lock preference
is changed. This is explicit opt-in activity reporting, not a global setting.

The archive includes an SDK-linked universal macOS bridge for IOKit, which Buoy
0.72.0's bundled stubs omit. To rebuild it on a Mac, run
`python3 build_native.py`, then seal the package with
`python3 tools/build_integrations.py poweractivity --all-targets`.
Remove this bridge only after direct IOKit declarations build and pass the saved
native lifecycle test on supported macOS architectures; see the supplemental
upstream evidence.

Maintainers run the private validation suite before release. See the repository README for public build instructions.

[Apple's activity options](https://developer.apple.com/documentation/foundation/processinfo/activityoptions)
explain the tradeoffs. The native smoke test acquires and immediately closes a
default activity; the dedicated keep-awake test above exercises the prevention options.

Maintainers run the private validation suite before release. See the repository README for public build instructions.
