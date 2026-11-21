"""Poster entry: AURELIA, the Floating Isles.

Copies the bundled entry.png (a vintage travel poster for an invented
place) into the make.fun output directory as entry.png.

The poster shows AURELIA, a place that does not exist: green-topped
isles drifting above a sea of clouds at golden hour, waterfalls spilling
into the mist below, and one white lighthouse on the largest isle, with
the name AURELIA set in large art-deco letters across the sky.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
# The image is a JPEG in a .png name on purpose: the gate accepts a whole
# PNG or JPEG at /output/entry.png, and the JPEG stays under the 1 MiB cap.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if not os.path.isfile(SOURCE):
        print(f"error: source image not found: {SOURCE}", file=sys.stderr)
        sys.exit(1)
    if os.path.getsize(SOURCE) == 0:
        print(f"error: source image is empty: {SOURCE}", file=sys.stderr)
        sys.exit(1)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    dest = os.path.join(OUTPUT_DIR, "entry.png")
    shutil.copyfile(SOURCE, dest)
    written = os.path.getsize(dest)
    if written != os.path.getsize(SOURCE):
        print(
            f"error: output size {written} != source size "
            f"{os.path.getsize(SOURCE)}",
            file=sys.stderr,
        )
        sys.exit(1)
    print(f"wrote {dest} ({written} bytes)")


if __name__ == "__main__":
    main()
