import os
import sys


import os
import sys
from pathlib import Path


dir_file = (
    Path(os.path.expanduser("~")) / "config/directory_bookmarks/cmd/dir.txt"
)


def list_saved_dirs():
    with open(dir_file, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(reversed(lines), start=1):
            print(f"{i}: {line.strip()}")


def main():
    list_saved_dirs()


if __name__ == "__main__":
    print(80 * "-")
    # list_saved_dirs()
    main()
    print(80 * "-")
