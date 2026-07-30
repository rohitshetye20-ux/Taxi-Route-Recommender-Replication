"""
test_preprocessing.py
=====================

Unit tests for src.preprocessing.

This module verifies data preprocessing operations including
missing value handling, duplicate removal, column standardization,
data validation, and feature preprocessing.

Run
---
pytest tests/test_preprocessing.py

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from src.preprocessing import DataPreprocessor


# ============================================================
# Fixture
# ============================================================

@pytest.fixture
def preprocessor():
    return DataPreprocessor()


# ============================================================
# Missing Values
# ============================================================

def test_remove_missing_values(preprocessor):

    dataframe = pd.DataFrame(
        {
            "A": [1, np.nan, 3],
            "B": [4, 5, np.nan],
        }
    )

    result = preprocessor.remove_missing_values(dataframe)

    assert result.isnull().sum().sum() == 0


def test_missing_value_count_reduced(preprocessor):

    dataframe = pd.DataFrame(
        {
            "A": [1, None, 3],
            "B": [None, 5, 6],
        }
    )

    before = dataframe.isnull().sum().sum()

    result = preprocessor.remove_missing_values(dataframe)

    after = result.isnull().sum().sum()

    assert after < before


# ============================================================
# Duplicate Removal
# ============================================================

def test_remove_duplicates(preprocessor):

    dataframe = pd.DataFrame(
        {
            "A": [1, 1, 2],
            "B": [3, 3, 4],
        }
    )

    result = preprocessor.remove_duplicates(dataframe)

    assert len(result) == 2


# ============================================================
# Column Standardization
# ============================================================

def test_standardize_column_names(preprocessor):

    dataframe = pd.DataFrame(
        columns=[
            "Trip ID",
            "Pickup Zone",
            "Dropoff Zone",
        ]
    )

    result = preprocessor.standardize_column_names(dataframe)

    assert list(result.columns) == [
        "trip_id",
        "pickup_zone",
        "dropoff_zone",
    ]


# ============================================================
# Data Types
# ============================================================

def test_convert_numeric_columns(preprocessor):

    dataframe = pd.DataFrame(
        {
            "fare": ["10", "20", "30"]
        }
    )

    result = preprocessor.convert_numeric_columns(
        dataframe,
        columns=["fare"],
    )

    assert pd.api.types.is_numeric_dtype(result["fare"])


# ============================================================
# Validation
# ============================================================

def test_validate_dataframe(preprocessor, sample_dataframe):

    assert preprocessor.validate_dataframe(
        sample_dataframe
    )


def test_empty_dataframe_validation(preprocessor):

    dataframe = pd.DataFrame()

    assert not preprocessor.validate_dataframe(
        dataframe
    )


# ============================================================
# Feature Engineering
# ============================================================

def test_create_distance_category(preprocessor):

    dataframe = pd.DataFrame(
        {
            "distance": [
                2,
                8,
                15,
            ]
        }
    )

    result = preprocessor.create_distance_category(
        dataframe
    )

    assert "distance_category" in result.columns


# ============================================================
# Outlier Handling
# ============================================================

def test_remove_outliers(preprocessor):

    dataframe = pd.DataFrame(
        {
            "fare": [
                10,
                12,
                15,
                1000,
            ]
        }
    )

    result = preprocessor.remove_outliers(
        dataframe,
        column="fare",
    )

    assert len(result) < len(dataframe)


# ============================================================
# Column Existence
# ============================================================

def test_required_columns(preprocessor, sample_dataframe):

    required = [
        "Trip_ID",
        "Pickup",
        "Dropoff",
    ]

    assert preprocessor.has_required_columns(
        sample_dataframe,
        required,
    )


# ============================================================
# Chained Pipeline
# ============================================================

def test_full_preprocessing_pipeline(preprocessor, sample_dataframe):

    dataframe = preprocessor.standardize_column_names(
        sample_dataframe
    )

    dataframe = preprocessor.remove_duplicates(
        dataframe
    )

    dataframe = preprocessor.remove_missing_values(
        dataframe
    )

    assert len(dataframe) > 0

    assert dataframe.isnull().sum().sum() == 0


# ============================================================
# Error Handling
# ============================================================

def test_invalid_numeric_conversion(preprocessor):

    dataframe = pd.DataFrame(
        {
            "fare": [
                "A",
                "B",
                "C",
            ]
        }
    )

    with pytest.raises(Exception):

        preprocessor.convert_numeric_columns(
            dataframe,
            columns=["fare"],
        )


# ============================================================
# Performance
# ============================================================

def test_large_dataframe(preprocessor):

    dataframe = pd.DataFrame(
        {
            "A": range(10000),
            "B": range(10000),
        }
    )

    result = preprocessor.remove_duplicates(
        dataframe
    )

    assert len(result) == 10000