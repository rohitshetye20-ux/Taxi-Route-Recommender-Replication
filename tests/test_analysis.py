"""
test_analysis.py
================

Unit tests for src.analysis.

This module verifies statistical analysis,
summary generation, descriptive statistics,
distribution analysis, correlation analysis,
and reporting.

Run
---
pytest tests/test_analysis.py

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

from src.analysis import DataAnalyzer


# ============================================================
# Fixture
# ============================================================

@pytest.fixture
def analyzer():

    return DataAnalyzer()


# ============================================================
# Descriptive Statistics
# ============================================================

def test_descriptive_statistics(
    analyzer,
    sample_dataframe,
):

    stats = analyzer.descriptive_statistics(
        sample_dataframe
    )

    assert isinstance(stats, pd.DataFrame)


def test_statistics_not_empty(
    analyzer,
    sample_dataframe,
):

    stats = analyzer.descriptive_statistics(
        sample_dataframe
    )

    assert not stats.empty


# ============================================================
# Summary Report
# ============================================================

def test_summary_report(
    analyzer,
    sample_dataframe,
):

    report = analyzer.summary_report(
        sample_dataframe
    )

    assert isinstance(report, str)


# ============================================================
# Correlation
# ============================================================

def test_correlation_matrix(
    analyzer,
):

    dataframe = pd.DataFrame(

        {

            "A": [1, 2, 3],

            "B": [4, 5, 6],

            "C": [7, 8, 9],

        }

    )

    correlation = analyzer.correlation_matrix(
        dataframe
    )

    assert isinstance(correlation, pd.DataFrame)


def test_correlation_square(
    analyzer,
):

    dataframe = pd.DataFrame(

        {

            "A": [1, 2],

            "B": [3, 4],

        }

    )

    matrix = analyzer.correlation_matrix(
        dataframe
    )

    assert matrix.shape == (2, 2)


# ============================================================
# Numeric Summary
# ============================================================

def test_numeric_summary(
    analyzer,
):

    dataframe = pd.DataFrame(

        {

            "Fare": [100, 120, 150],

            "Distance": [2.0, 3.5, 4.1],

        }

    )

    summary = analyzer.numeric_summary(
        dataframe
    )

    assert isinstance(summary, dict)


# ============================================================
# Missing Values
# ============================================================

def test_missing_value_summary(
    analyzer,
):

    dataframe = pd.DataFrame(

        {

            "A": [1, None, 3],

            "B": [4, 5, None],

        }

    )

    summary = analyzer.missing_value_summary(
        dataframe
    )

    assert isinstance(summary, dict)

    assert summary["total_missing"] == 2


# ============================================================
# Duplicate Analysis
# ============================================================

def test_duplicate_summary(
    analyzer,
):

    dataframe = pd.DataFrame(

        {

            "A": [1, 1, 2],

            "B": [3, 3, 4],

        }

    )

    duplicates = analyzer.duplicate_summary(
        dataframe
    )

    assert duplicates == 1


# ============================================================
# Dataset Shape
# ============================================================

def test_dataset_shape(
    analyzer,
    sample_dataframe,
):

    rows, columns = analyzer.dataset_shape(
        sample_dataframe
    )

    assert rows == 4

    assert columns == 5


# ============================================================
# Empty Dataset
# ============================================================

def test_empty_dataframe(
    analyzer,
):

    dataframe = pd.DataFrame()

    with pytest.raises(ValueError):

        analyzer.summary_report(
            dataframe
        )


# ============================================================
# Distribution
# ============================================================

def test_distribution_analysis(
    analyzer,
):

    dataframe = pd.DataFrame(

        {

            "Fare": [

                100,

                120,

                130,

                150,

            ]

        }

    )

    distribution = analyzer.distribution_analysis(

        dataframe,

        column="Fare",

    )

    assert isinstance(distribution, dict)


# ============================================================
# Outlier Detection
# ============================================================

def test_outlier_detection(
    analyzer,
):

    dataframe = pd.DataFrame(

        {

            "Fare": [

                100,

                120,

                150,

                5000,

            ]

        }

    )

    outliers = analyzer.detect_outliers(

        dataframe,

        column="Fare",

    )

    assert len(outliers) == 1


# ============================================================
# Integration
# ============================================================

def test_complete_analysis_pipeline(
    analyzer,
    sample_dataframe,
):

    stats = analyzer.descriptive_statistics(

        sample_dataframe,

    )

    report = analyzer.summary_report(

        sample_dataframe,

    )

    shape = analyzer.dataset_shape(

        sample_dataframe,

    )

    assert not stats.empty

    assert report

    assert shape == (4, 5)