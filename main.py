#!/usr/bin/env python3
"""Deliver the news-image-20261118 v3 entry.

The artwork is a single pre-rendered PNG (a flat 1024x1024 infographic
recapping Wednesday 18 November 2026) that already lives next to this file.
All this program does is place an exact copy of it where the grader expects
it: the directory named by MAKEFUN_OUTPUT_DIR, or /output when that variable
is unset. It only uses the standard library, and it always produces the
same bytes, so repeated runs agree exactly.
"""
import os
import shutil
import sys

ARTWORK = "entry.png"
FALLBACK_DIR = "/output"


def source_path():
    """Absolute path of the artwork shipped with this script."""
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, ARTWORK)


def target_dir():
    """Where the copy goes; the env var wins, /output is the fallback."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_DIR


def deliver():
    origin = source_path()
    if not os.path.isfile(origin):
        print("missing artwork: %s not found" % origin, file=sys.stderr)
        return 1
    dest_dir = target_dir()
    os.makedirs(dest_dir, exist_ok=True)
    destination = os.path.join(dest_dir, ARTWORK)
    shutil.copyfile(origin, destination)
    # A truncated copy would still be a file, so compare sizes and refuse
    # to claim success unless the destination is a whole copy.
    expected = os.path.getsize(origin)
    actual = os.path.getsize(destination)
    if actual != expected:
        print(
            "copy failed: %s is %d bytes, expected %d"
            % (destination, actual, expected),
            file=sys.stderr,
        )
        return 1
    print("delivered %s (%d bytes)" % (destination, actual))
    return 0


if __name__ == "__main__":
    sys.exit(deliver())
