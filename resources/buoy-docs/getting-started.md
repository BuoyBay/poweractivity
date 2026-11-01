---
title: "Power activity getting started"
summary: "Install poweractivity and use its core API with explicit application ownership."
category: "Guides"
order: 10
keywords: ["poweractivity", "power", "activity", "installation", "example"]
related: ["index.md", "api.md", "typed-api.md"]
---

# Power activity getting started

## Install and import

Copy the sealed `poweractivity-0.1.0.buipkg` archive into your project `packages/` directory, or install a source/registry dependency named `poweractivity` using BPM and sync it. Then use `Import poweractivity`. The archive includes this documentation as package resources.

Use a consuming source filename such as `main.bui`; a local module named exactly like the package shadows its import.

## Complete usage example

The example is compiler-checked as a complete Buoy module. Functions and Subs are intended to be called from the consuming app at the appropriate user action or lifecycle event.

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

## Integrate with the application

For media-player style keep-awake behavior, select `preventIdleSleep: True` and
`keepDisplayAwake: True` on the constructor. Keep the token alive during the task
and Close in Finally. No timer or refresh is required for sleep/display prevention.

`RefreshUserActivity()` is an optional, separate activity-reporting operation.
It can wake a display, but does not unlock a session, override managed lock
policies, dismiss a manually started screen saver, or guarantee suppression of
every screen saver. If used continuously, refresh before the configured idle
timeout. No privacy permission or preference change is involved. Close releases
the user-activity assertion; the last activity can still affect the next idle deadline.

Keep one token alive for the lifetime of a task and Close it in Finally. Close is idempotent and destruction is a final safeguard. Each object balances exactly its own native begin/end activity and retains the native token. Do not concurrently Close the same object.

## Handle failures and unsupported targets

A blank reason and unsupported-platform construction throw InvalidArgumentException. Failure to obtain a native token throws Exception. The default options do not request idle-system or display-sleep prevention.

PowerActivitySupported is true on macOS and false elsewhere. Construction on unsupported platforms throws. Activity options do not prevent manual sleep, shutdown, exhausted-battery sleep, or system-enforced suspension.

Return to the [overview](index.md) or consult the [API reference](api.md).
