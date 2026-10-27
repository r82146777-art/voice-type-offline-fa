#!/usr/bin/env python3
"""Extract archive inventory and printable DEX strings from an Android APK.

Usage: python3 extract_apk_strings.py input.apk output-directory
This is a triage tool, not a DEX decompiler. Use JADX for readable Java source.
"""
import os
import re
import sys
import zipfile

if len(sys.argv) != 3:
    raise SystemExit("Usage: extract_apk_strings.py input.apk output-directory")

apk, out_dir = sys.argv[1], sys.argv[2]
os.makedirs(out_dir, exist_ok=True)
with zipfile.ZipFile(apk) as zf:
    names = zf.namelist()
    with open(os.path.join(out_dir, "apk-file-list.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(names) + "\n")
    if "classes.dex" not in names:
        raise SystemExit("APK has no classes.dex")
    dex = zf.read("classes.dex")

    # DEX strings are length-prefixed/encoded; printable runs are useful for
    # triage but are not a faithful extraction of the DEX string pool.
    runs = (m.group().decode("ascii", "ignore")
            for m in re.finditer(rb"[\x20-\x7e]{4,}", dex))
    unique = list(dict.fromkeys(runs))
    with open(os.path.join(out_dir, "classes-dex-printable-strings.txt"),
              "w", encoding="utf-8") as f:
        f.write("\n".join(unique) + "\n")

print(f"APK entries: {len(names)}")
print(f"classes.dex bytes: {len(dex)}")
print("Note: printable strings are not Java/Kotlin source. Run JADX on the APK.")
