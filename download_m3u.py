#!/usr/bin/env python3

import os
import argparse
import re
import requests

PROG = "m3u_download"
DESC = "Download all files from M3U playlist file."
PATTERN = re.compile(r"^#EXTINF:[\d]+,(.*)")

def get_args():
    """Parse cli args."""
    parser = argparse.ArgumentParser(prog=PROG, description=DESC)
    parser.add_argument(
        "m3u_path",
        help="Path to input M3U file.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        help="Output directory to save files.",
    )
    return parser.parse_args()


def fmt_title(s):
    """Format mp4 video title."""
    t = PATTERN.match(s).group(1)
    t = t.replace(" ", "_")
    t = re.sub("[^A-Za-z0-9_]+", "", t)
    t = t + ".mp4"
    return t


def main():
    args = get_args()
    out = os.getcwd()
    if args.output_dir:
        out = args.output_dir
    lines = list()
    with open(args.m3u_path) as m3u:
        lines = m3u.readlines()
    
    # Drop first and last line
    lines.pop(0), lines.pop()
    count = len(lines) // 2
    total = 0
    it = iter(lines)
    
    print(f"Preparing to download {count} files.")
    for i, (title, url) in enumerate(zip(it, it), start=1):
        title = fmt_title(title)
        print(f"Downloading ({i}/{count}) {title} ...")
        resp = requests.get(url)
        path = os.path.join(out, title)
        with open(path, "wb") as f:
            f.write(resp.content)
            size = len(resp.content) / pow(1000, 2)
            total += size
            print(f"    Saved {size:.2f} mb, Total {total:.2f} mb")
    print(f"Finished downloading {count} files, {total:.2f} mb.")

if __name__ == "__main__":
    main()
