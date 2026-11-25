"""Copy the pre-written apology line into the output directory.

The entry is a single line of text, written ahead of time in entry.txt.
This program only copies that file into MAKEFUN_OUTPUT_DIR as entry.txt,
using nothing but the standard library, so the grader run is deterministic.
"""

import os
import shutil


def main():
    # The apology itself never changes while this runs: it was drafted
    # beforehand and saved next to this script, so all this function does
    # is place that saved line where the grader expects to find it.
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(here, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
