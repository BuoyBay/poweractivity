---
title: "poweractivity typed API"
summary: "Source-derived public signatures, properties, parameters, defaults, and return values."
category: "Reference"
order: 21
types: ["PowerActivity"]
dependencies: []
symbols: ["PowerActivity"]
related: ["api.md", "getting-started.md", "index.md"]
---

# poweractivity typed API

Generated from the package source declarations. Platform guards are shown where present; inherited members are documented on the base type. See the [API contracts](api.md) for behavior and limitations.

## PowerActivity functions

### PowerActivitySupported

`Public Function PowerActivitySupported() As Boolean`

No parameters.

#### Returns

| Type |
| --- |
| `Boolean` |

## PowerActivity

`Public Class PowerActivity`

A balanced native activity token. Keep it alive for the work, then Close in Finally.

### Properties

| Name | Type | Read-Only | Shared | Default | Description |
| --- | --- | --- | --- | --- | --- |
| `IsActive` | `Boolean` | Yes | No | — | — |

### Constructor

`Public Sub Constructor(reason As String, preventIdleSleep As Boolean = False, keepDisplayAwake As Boolean = False)`

#### Parameters

| Name | Type | Passing | Default |
| --- | --- | --- | --- |
| `reason` | `String` | `ByVal` | Required |
| `preventIdleSleep` | `Boolean` | `ByVal` | `False` |
| `keepDisplayAwake` | `Boolean` | `ByVal` | `False` |

Returns: no value.

### RefreshUserActivity

`Public Sub RefreshUserActivity()`

Optional local user-activity reporting; not required for sleep/display prevention. If reporting continuously, refresh before the configured idle timeout. May wake the display. This does not unlock an already locked session.

No parameters.

Returns: no value.

### Close

`Public Sub Close()`

No parameters.

Returns: no value.

### Destructor

`Public Sub Destructor()`

No parameters.

Returns: no value.
