"""
utils.py
========

Shared utility functions for the Taxi Route Recommender project.

This module provides reusable helper functions for logging,
timing, file operations, JSON handling, directory management,
and miscellaneous infrastructure tasks.

Features
--------
- Logger configuration
- Execution timing
- Directory creation
- JSON read/write
- File existence checks
- Timestamp generation

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime
from pathlib import Path
from typing import Any


# ============================================================
# Logger Configuration
# ============================================================

def get_logger(
    name: str,
    level: int = logging.INFO,
) -> logging.Logger:
    """
    Create or retrieve a configured logger.
    """

    logger = logging.getLogger(name)

    if not logger.handlers:

        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)

        logger.setLevel(level)

    return logger


# ============================================================
# Execution Timer
# ============================================================

class Timer:
    """
    Context manager for timing code execution.

    Example
    -------
    with Timer("Training"):
        train_model()
    """

    def __init__(self, task_name: str = "Task") -> None:
        self.task_name = task_name
        self.start_time = 0.0

    def __enter__(self):

        self.start_time = time.perf_counter()

        print(f"\nStarting: {self.task_name}")

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        elapsed = time.perf_counter() - self.start_time

        print(
            f"Completed: {self.task_name} "
            f"in {elapsed:.2f} seconds"
        )


# ============================================================
# Directory Utilities
# ============================================================

def ensure_directory(
    directory: str | Path,
) -> Path:
    """
    Create directory if it does not exist.
    """

    path = Path(directory)

    path.mkdir(
        parents=True,
        exist_ok=True,
    )

    return path


# ============================================================
# File Utilities
# ============================================================

def file_exists(
    filepath: str | Path,
) -> bool:
    """
    Check whether a file exists.
    """

    return Path(filepath).exists()


# ============================================================
# JSON Utilities
# ============================================================

def save_json(
    data: Any,
    filepath: str | Path,
    indent: int = 4,
) -> None:
    """
    Save data as JSON.
    """

    with open(
        filepath,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            indent=indent,
        )


def load_json(
    filepath: str | Path,
) -> Any:
    """
    Load JSON file.
    """

    with open(
        filepath,
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


# ============================================================
# Timestamp
# ============================================================

def current_timestamp() -> str:
    """
    Return current timestamp.
    """

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


# ============================================================
# Project Banner
# ============================================================

def print_banner() -> None:
    """
    Display project banner.
    """

    print("=" * 70)

    print("Taxi Route Recommender System")

    print("Research Reproduction Framework")

    print("Author : Rohit Shetye")

    print("Version: 1.0.0")

    print("=" * 70)


# ============================================================
# Environment Information
# ============================================================

def environment_summary() -> None:
    """
    Print runtime environment information.
    """

    import platform
    import sys

    print("\nEnvironment Information")

    print("-" * 60)

    print(f"Python Version : {sys.version.split()[0]}")

    print(f"Platform       : {platform.system()}")

    print(f"Architecture   : {platform.machine()}")

    print(f"Timestamp      : {current_timestamp()}")

    print("-" * 60)