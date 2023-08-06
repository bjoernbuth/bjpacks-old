from setuptools import setup, find_packages

setup(
    name="bjpacks",
    version="1.0.0",
    author="Bjoern",
    packages=find_packages(),
    install_requires=["pyperclip"],
    entry_points={
        "console_scripts": [
            # listing dir bookmarks
            "list_dir_bookmarks = src.list_dir_bookmarks.list_dir_bookmarks:list_saved_dirs",
            "ldb = src.list_dir_bookmarks.list_dir_bookmarks:list_saved_dirs",
            # path to clipboard
            "path_to_clippboard = src.path_to_clippboard.path_to_clippboard:copy_path_to_clipboard",
            "ptc = src.path_to_clippboard.path_to_clippboard:copy_path_to_clipboard",
        ],
    },
)
