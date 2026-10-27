#!/usr/bin/env python3
"""Create a reproducible text inventory from the original Android APK.

This intentionally does not pretend that decompilation reconstructs the original
Unity/C# project. It validates the APK, inventories DEX/native/model/assets,
extracts readable strings, and records hashes for later comparison.
"""
from __future__ import annotations
import argparse, hashlib, os, re, subprocess, sys, zipfile
from pathlib import Path

PATTERN = re.compile(r"(?i)(offline voice type|voice.?type|sherpa|onnx|\basr\b|\btts\b|speech|keyboard|talkback|silero|model|persian|farsi|vazir)")

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("apk", help="path to the original APK")
    p.add_argument("--out", default="apk-inventory", help="output directory")
    args = p.parse_args()
    apk = Path(args.apk)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    if not apk.is_file():
        p.error(f"APK not found: {apk}")
    raw = apk.read_bytes()
    if not zipfile.is_zipfile(apk):
        p.error("Input is not a ZIP-format APK")
    with zipfile.ZipFile(apk) as z:
        names = z.namelist()
        if "AndroidManifest.xml" not in names or not any(re.fullmatch(r"classes(?:[0-9]+)?\.dex", n) for n in names):
            p.error("Archive is missing AndroidManifest.xml or DEX files; refusing non-APK input")
        (out / "archive-entries.txt").write_text("\n".join(sorted(names))+"\n", encoding="utf-8")
        report = [
            "APK inventory (original binary, not reconstructed source)",
            f"Filename: {apk.name}",
            f"Size bytes: {len(raw)}",
            f"SHA256: {sha256(raw)}",
            f"ZIP entries: {len(names)}",
            "",
            "DEX files:",
        ]
        report += [f"  {n} ({z.getinfo(n).file_size} bytes)" for n in sorted(names) if re.fullmatch(r"classes(?:[0-9]+)?\.dex", n)]
        report += ["", "Native libraries:"]
        report += [f"  {n} ({z.getinfo(n).file_size} bytes)" for n in sorted(names) if n.startswith("lib/") and n.endswith(".so")]
        report += ["", "Speech/model/keyboard-related assets:"]
        matches = [n for n in sorted(names) if PATTERN.search(n)]
        report += [f"  {n} ({z.getinfo(n).file_size} bytes)" for n in matches]
        if not matches:
            report += ["  (none matched by filename)"]
        (out / "inventory.txt").write_text("\n".join(report)+"\n", encoding="utf-8")
        strings = set()
        for name in names:
            if not (name.endswith(".dex") or name.endswith(".xml") or name.endswith(".json") or name.endswith(".txt") or name.endswith(".properties") or name.endswith(".cfg")):
                continue
            try:
                data = z.read(name)
            except Exception:
                continue
            for m in re.finditer(rb"[ -~]{5,}|[\x20-\x7e\x80-\xff]{6,}", data):
                s = m.group().decode("utf-8", "ignore").strip()
                if s and PATTERN.search(s):
                    strings.add(f"{name}: {s[:500]}")
        (out / "relevant-strings.txt").write_text("\n".join(sorted(strings))+"\n", encoding="utf-8")
    print(f"Validated APK and wrote reports to {out}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
