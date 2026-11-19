#!/usr/bin/env python3
"""Round-3 entrypoint for news-image-20261119.

The entry is a single pre-drawn poster. This program copies it to the
output directory the grader provides. It uses only the standard library,
touches no network, and writes the same bytes on every run.
"""
import os
import shutil

POSTER = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    shutil.copyfile(os.path.join(here, POSTER),
                    os.path.join(outdir, POSTER))


if __name__ == "__main__":
    main()
