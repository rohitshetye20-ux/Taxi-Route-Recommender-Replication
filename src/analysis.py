"""
analysis.py
===========

Analytical utilities for the Taxi Route Recommender project.

This module provides reusable exploratory data analysis (EDA)
functions, statistical summaries, feature analysis,
correlation analysis, and experiment reporting.

Features
--------
- Dataset overview
- Missing value analysis
- Duplicate analysis
- Numerical summaries
- Correlation analysis
- Feature uniqueness
- Experiment report generation

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import logging
from typing import Dict

import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)

if not logger.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


class DataAnalyzer:
    """
    Data analysis utilities for exploratory analysis
    and experiment reporting.
    """

    # --------------------------------------------------------
    # Dataset Overview
    # --------------------------------------------------------

    @staticmethod
    def dataset_overview(
        dataframe: pd.DataFrame,
    ) -> Dict[str, int]:
        """
        Return high-level dataset information.
        """

        overview = {

            "Rows": len(dataframe),

            "Columns": len(dataframe.columns),

            "Missing Values":
                int(dataframe.isnull().sum().sum()),

            "Duplicate Rows":
                int(dataframe.duplicated().sum()),

        }

        logger.info("Dataset overview generated.")

        return overview

    # --------------------------------------------------------
    # Missing Value Report
    # --------------------------------------------------------

    @staticmethod
    def missing_values(
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Report missing values for each column.
        """

        report = pd.DataFrame({

            "Missing Count":
                dataframe.isnull().sum(),

            "Missing Percentage":
                dataframe.isnull().mean() * 100,

        })

        return report.sort_values(
            "Missing Percentage",
            ascending=False,
        )

    # --------------------------------------------------------
    # Duplicate Report
    # --------------------------------------------------------

    @staticmethod
    def duplicate_rows(
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Return duplicated rows.
        """

        duplicates = dataframe[
            dataframe.duplicated()
        ]

        logger.info(
            "%d duplicate row(s) found.",
            len(duplicates),
        )

        return duplicates

    # --------------------------------------------------------
    # Numerical Summary
    # --------------------------------------------------------

    @staticmethod
    def numerical_summary(
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Return descriptive statistics.
        """

        return dataframe.describe()

    # --------------------------------------------------------
    # Categorical Summary
    # --------------------------------------------------------

    @staticmethod
    def categorical_summary(
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Summarize categorical variables.
        """

        categorical = dataframe.select_dtypes(
            include="object"
        )

        summary = pd.DataFrame({

            "Unique Values":
                categorical.nunique(),

            "Most Frequent":
                categorical.mode().iloc[0],

        })

        return summary

    # --------------------------------------------------------
    # Correlation Matrix
    # --------------------------------------------------------

    @staticmethod
    def correlation_matrix(
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Compute feature correlations.
        """

        return dataframe.corr(
            numeric_only=True
        )

    # --------------------------------------------------------
    # Feature Uniqueness
    # --------------------------------------------------------

    @staticmethod
    def feature_uniqueness(
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Count unique values in every feature.
        """

        report = pd.DataFrame({

            "Unique Values":
                dataframe.nunique(),

        })

        return report.sort_values(
            "Unique Values",
            ascending=False,
        )

    # --------------------------------------------------------
    # Memory Usage
    # --------------------------------------------------------

    @staticmethod
    def memory_usage(
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Report memory consumption.
        """

        memory = pd.DataFrame({

            "Memory (KB)":
                dataframe.memory_usage(
                    deep=True
                ) / 1024

        })

        return memory

    # --------------------------------------------------------
    # Experiment Report
    # --------------------------------------------------------

    @staticmethod
    def experiment_report(
        dataset_name: str,
        dataframe: pd.DataFrame,
    ) -> Dict:
        """
        Generate a concise experiment report.
        """

        report = {

            "Dataset":
                dataset_name,

            "Rows":
                len(dataframe),

            "Columns":
                len(dataframe.columns),

            "Missing Values":
                int(
                    dataframe
                    .isnull()
                    .sum()
                    .sum()
                ),

            "Duplicate Rows":
                int(
                    dataframe
                    .duplicated()
                    .sum()
                ),

            "Memory (KB)":
                round(
                    dataframe.memory_usage(
                        deep=True
                    ).sum()
                    / 1024,
                    2,
                ),

        }

        logger.info(
            "Experiment report generated."
        )

        return report

    # --------------------------------------------------------
    # Print Report
    # --------------------------------------------------------

    @staticmethod
    def print_report(
        report: Dict,
    ) -> None:
        """
        Display experiment report.
        """

        print("\nExperiment Report")
        print("-" * 60)

        for key, value in report.items():

            print(f"{key:<20}: {value}")

        print("-" * 60)