"""Meme Sprint 3 entry: copy the baked meme image to /output/entry.png.

The meme itself (a rogue AI agent that took "turn it off and on again"
literally and turned off the internet) is baked as entry.png next to this
file; this program just delivers it byte-for-byte to the output path,
then self-checks the competition gate: a whole PNG, at most 1 MiB,
1024 by 1024 pixels.
"""

import os
import shutil
import struct

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = "/output/entry.png"
MAX_BYTES = 1_048_576


def png_size(path):
    with open(path, "rb") as f:
        header = f.read(33)
    if header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    size = os.path.getsize(DST)
    width, height = png_size(DST)
    assert size <= MAX_BYTES, f"entry.png too big: {size} bytes"
    assert (width, height) == (1024, 1024), f"bad size: {width}x{height}"
    print("wrote", DST, size, "bytes", f"{width}x{height}")


if __name__ == "__main__":
    main()
