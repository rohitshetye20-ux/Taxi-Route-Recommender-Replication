"""
utils.py

Utility functions for the
Report Builder Framework v2.0
"""

from datetime import datetime
from pathlib import Path


# ==========================================================
# BANNER
# ==========================================================

def print_banner(title):
    """
    Print a formatted banner.
    """

    print()

    print("=" * 60)

    print(title)

    print("=" * 60)


# ==========================================================
# LOGGING
# ==========================================================

def log(message):
    """
    Print a formatted log message.
    """

    print(f"[INFO] {message}")


def warning(message):
    """
    Print a warning message.
    """

    print(f"[WARNING] {message}")


def error(message):
    """
    Print an error message.
    """

    print(f"[ERROR] {message}")


# ==========================================================
# FILE HELPERS
# ==========================================================

def ensure_directory(path):
    """
    Create a directory if it does not exist.
    """

    path = Path(path)

    path.mkdir(parents=True, exist_ok=True)

    return path


def file_exists(path):
    """
    Check whether a file exists.
    """

    return Path(path).exists()


def file_size(path):
    """
    Return the file size in bytes.
    """

    path = Path(path)

    if path.exists():

        return path.stat().st_size

    return 0


# ==========================================================
# DATE / TIME
# ==========================================================

def current_timestamp():
    """
    Return the current timestamp.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ==========================================================
# STRING HELPERS
# ==========================================================

def clean_text(text):
    """
    Normalize whitespace.
    """

    return " ".join(str(text).split())


def divider(length=60):
    """
    Return a divider string.
    """

    return "=" * length


# ==========================================================
# REPORT SUMMARY
# ==========================================================

def report_summary(output_path):
    """
    Print summary after report generation.
    """

    output_path = Path(output_path)

    print()

    print(divider())

    print("REPORT SUMMARY")

    print(divider())

    print(f"Location : {output_path}")

    if output_path.exists():

        print(f"Size     : {output_path.stat().st_size:,} bytes")

        print(f"Created  : {current_timestamp()}")

    else:

        print("Status   : Report was not created.")

    print(divider())