"""
Main Module
"""

import argparse
from . import __software__, __version__, __author__, __copyright__, __license__

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
        print(f"{__copyright__} {__author__} - {__software__}, v{__version__}")
        print(f"This software library is licensed under the {__license__}")
