# Manage scoped macOS process and user activities

`Import poweractivity` exposes a scoped native macOS activity token:
`New PowerActivity(reason, preventIdleSleep = False, keepDisplayAwake = False)`.
`PowerActivitySupported()` is true on macOS, false elsewhere; unsupported
construction throws explicitly.

Keep the object alive while performing a user-requested export/download/task.
Call `Close()` in `Finally`; it is idempotent. `IsActive` reports whether this
object still owns a token, and destruction calls Close as a final safeguard.
Each object balances exactly its own NSProcessInfo begin/end activity and retains
its native token until completion. Objects are not safe for concurrent Close calls.

## Install

From a Buoy consumer project with BPM installed:

```sh
bpm add poweractivity --git https://github.com/BuoyBay/poweractivity.git --rev refs/heads/main
```

BPM records the resolved commit in its lockfile. Keep that lockfile with the
consumer project for reproducible installs.

## Example

```buoy
Import poweractivity

Sub RunUserRequestedWork()
    If Not PowerActivitySupported() Then Return
    Dim activity As New PowerActivity("Exporting a document")
    Try
        Print activity.IsActive
        ' Perform the requested export while activity remains alive.
    Finally
        activity.Close()
    End Try
End Sub
```

## Platform and scope

Uses macOS process/user activity APIs. Keep scoped activities balanced and leave the user in control of idle/sleep policy.

## Build and API reference

Source is in `modules/`, with native/runtime inputs where required. Use the
[package guide](docs/API.md) for backend-specific build prerequisites, ownership
rules and supported targets. Rebuilding a native backend requires that target's
compiler and SDK; sealing an archive alone does not rebuild the backend.

## Local Buoy setup

On your own machine, install Buoy and run:

```sh
buoy ai init --both
```

The generated agent files and editor settings stay local and are ignored by Git.

## Contributing

[Contributing](CONTRIBUTING.md) · [License](LICENSE)
