#!/usr/bin/env python3
"""make.fun news-image-20261118 entry: write the pre-rendered entry.png
(a 1024x1024 infographic summing up Wednesday 18 November 2026) to the
output directory. Standard library only; the output is deterministic.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
IMAGE = "entry.png"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, IMAGE)
    dst = os.path.join(out_dir, IMAGE)
    shutil.copyfile(src, dst)
    # The gate runs the program twice and compares bytes: confirm the copy
    # landed whole before reporting success, so a partial write fails loudly.
    if os.path.getsize(dst) != os.path.getsize(src):
        print("entry.png copy incomplete", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
