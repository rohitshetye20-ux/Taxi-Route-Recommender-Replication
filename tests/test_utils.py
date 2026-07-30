"""
test_utils.py
=============

Unit tests for src.utils.

This module verifies the behavior of utility functions used
throughout the Taxi Route Recommender project.

Run
---
pytest tests/test_utils.py

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from src.utils import (
    Timer,
    ensure_directory,
    get_logger,
    load_json,
    save_json,
)

# ============================================================
# Directory Utilities
# ============================================================


def test_ensure_directory_creates_folder(tmp_path):
    """
    ensure_directory should create a directory
    when it does not exist.
    """

    directory = tmp_path / "new_directory"

    assert not directory.exists()

    ensure_directory(directory)

    assert directory.exists()
    assert directory.is_dir()


def test_ensure_directory_existing_folder(tmp_path):
    """
    Calling ensure_directory twice should not fail.
    """

    directory = tmp_path / "existing"

    ensure_directory(directory)

    ensure_directory(directory)

    assert directory.exists()


# ============================================================
# JSON Utilities
# ============================================================


def test_save_json(tmp_path):
    """
    Verify JSON file is written correctly.
    """

    filepath = tmp_path / "sample.json"

    data = {
        "name": "Taxi",
        "version": 1,
    }

    save_json(data, filepath)

    assert filepath.exists()


def test_load_json(tmp_path):
    """
    Verify JSON file can be loaded.
    """

    filepath = tmp_path / "sample.json"

    expected = {
        "accuracy": 0.95,
        "loss": 0.18,
    }

    with open(filepath, "w", encoding="utf-8") as file:

        json.dump(expected, file)

    result = load_json(filepath)

    assert result == expected


# ============================================================
# Logger
# ============================================================


def test_get_logger():

    logger = get_logger("pytest_logger")

    assert logger is not None

    assert logger.name == "pytest_logger"


# ============================================================
# Timer
# ============================================================


def test_timer_context_manager():

    with Timer("Dummy Timer"):

        value = sum(range(100))

    assert value == 4950


# ============================================================
# Error Handling
# ============================================================


def test_load_json_missing_file(tmp_path):

    filepath = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError):

        load_json(filepath)


def test_save_json_invalid_directory(tmp_path):

    filepath = tmp_path / "missing" / "sample.json"

    data = {"x": 1}

    with pytest.raises(Exception):

        save_json(data, filepath)


# ============================================================
# Multiple Calls
# ============================================================


def test_multiple_logger_instances():

    logger1 = get_logger("logger1")

    logger2 = get_logger("logger2")

    assert logger1.name != logger2.name


def test_multiple_directory_creation(tmp_path):

    for i in range(5):

        folder = tmp_path / f"folder_{i}"

        ensure_directory(folder)

        assert folder.exists()