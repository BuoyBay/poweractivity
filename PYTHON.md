# Python policy for poweractivity

Python files are ignored by default. New production tooling belongs in Buoy or BuoyScript.

The following exact files remain temporary production compatibility exceptions:

| File | Required capability |
| --- | --- |
| `build_native.py` | Only current native source builder for PowerActivity platform bridge slices. |

An exception may be removed after its native replacement passes the corresponding build or runtime checks.
Review additions file by file; directory-wide and wildcard Python exceptions are not allowed.
