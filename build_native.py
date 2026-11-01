#!/usr/bin/env python3
"""Build the macOS user-activity bridge against Apple's SDK for both architectures."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
if sys.platform != 'darwin':
    raise SystemExit('Rebuilding the power-activity bridge requires macOS and Xcode command-line tools.')
output = ROOT / 'runtime/arm64-apple-macos/libbuoy_poweractivity.dylib'
output.parent.mkdir(parents=True, exist_ok=True)
subprocess.run(['xcrun', 'clang', '-dynamiclib', '-Wall', '-Wextra', '-Werror',
                '-arch', 'arm64', '-arch', 'x86_64', '-mmacosx-version-min=11.0',
                '-framework', 'CoreFoundation', '-framework', 'IOKit',
                '-install_name', '@rpath/libbuoy_poweractivity.dylib',
                str(ROOT / 'native/bridge.c'), '-o', str(output)], check=True)
other = ROOT / 'runtime/x86_64-apple-macos/libbuoy_poweractivity.dylib'
other.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(output, other)
receipt = {'schema': 1,
           'inputs': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
                      for name in ['native/bridge.c', 'build_native.py']},
           'outputs': {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in [output, other]}}
(ROOT / 'native-build.json').write_text(json.dumps(receipt, indent=2) + '\n')
print('Built universal arm64/x86_64 power-activity bridge')
