"""
Main Module
"""

import argparse

from .__metadata__ import (
    __author__,
    __copyright__,
    __license__,
    __license_url__,
    __software__,
    __version__,
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Qaekwy Python Library")
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Display the version of the library",
    )

    args = parser.parse_args()
    if args.version:
        print(f"{__software__}, v{__version__}")
        print(f"{__copyright__} {__author__}")
        print(f"Licensed under the {__license__}")
        print(f"You may obtain a copy of the License at {__license_url__}")
        print(
            "You are free to use, modify, and redistribute this work under the terms of this license."
        )
