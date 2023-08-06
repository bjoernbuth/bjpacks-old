import os
import pyperclip
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
    # spam = pyperclip.paste()


def copy_path_to_clipboard():
    current_path = os.getcwd()
    pyperclip.copy(current_path)


if __name__ == "__main__":
    print(80 * "-")
    # list_saved_dirs()
    main()
    print(80 * "-")
