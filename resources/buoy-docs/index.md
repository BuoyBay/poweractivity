---
title: "Power activity"
summary: "Balance a macOS native activity token around user-requested work."
category: "Overview"
order: 0
keywords: ["poweractivity", "power", "activity"]
related: ["getting-started.md", "api.md", "typed-api.md"]
---

# Power activity

PowerActivity marks a period of user-requested work using NSProcessInfo activity options. Its default marks user-initiated work while allowing idle system sleep. Sleep-prevention options must be selected explicitly.

For media-player style keep-awake behavior, opt into both sleep-prevention
options and hold the token until the task ends. No periodic refresh is required.
`RefreshUserActivity()` is a separate, optional operation. Close releases all owned
assertions. This does not change persistent settings or unlock a locked session;
see the API reference for screen-saver and idle-policy limits.

## Platform support

PowerActivitySupported is true on macOS and false elsewhere. Construction on unsupported platforms throws. Activity options do not prevent manual sleep, shutdown, exhausted-battery sleep, or system-enforced suspension.

## Start reading

- [Getting started](getting-started.md) walks through installation and a complete example.
- [API reference](api.md) describes public symbols, state, errors, and ownership.

## Scope

Keep one token alive for the lifetime of a task and Close it in Finally. Close is idempotent and destruction is a final safeguard. Each object balances exactly its own native begin/end activity and retains the native token. Do not concurrently Close the same object.
