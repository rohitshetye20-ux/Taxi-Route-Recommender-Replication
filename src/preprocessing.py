"""
preprocessing.py
================

Data preprocessing utilities for the Taxi Route Recommender project.

This module provides reusable preprocessing functions for
cleaning, validating, transforming, and preparing datasets
prior to graph construction and model training.

Features
--------
- Missing value handling
- Duplicate removal
- Data type conversion
- Numeric normalization
- Column validation
- Dataset statistics

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import logging
from typing import Iterable, List, Optional

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# ------------------------------------------------------------
# Logger
# ------------------------------------------------------------

logger = logging.getLogger(__name__)

if not logger.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


# ------------------------------------------------------------
# Data Preprocessor
# ------------------------------------------------------------

class DataPreprocessor:
    """
    Reusable preprocessing engine for tabular datasets.
    """

    def __init__(self) -> None:
        logger.info("DataPreprocessor initialized.")

    # --------------------------------------------------------

    @staticmethod
    def remove_duplicates(
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Remove duplicate rows.
        """

        before = len(dataframe)

        dataframe = dataframe.drop_duplicates()

        removed = before - len(dataframe)

        logger.info(f"Removed {removed} duplicate row(s).")

        return dataframe

    # --------------------------------------------------------

    @staticmethod
    def remove_missing(
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Remove rows containing missing values.
        """

        before = len(dataframe)

        dataframe = dataframe.dropna()

        removed = before - len(dataframe)

        logger.info(f"Removed {removed} row(s) with missing values.")

        return dataframe

    # --------------------------------------------------------

    @staticmethod
    def fill_missing(
        dataframe: pd.DataFrame,
        strategy: str = "mean",
    ) -> pd.DataFrame:
        """
        Fill missing numeric values.

        Parameters
        ----------
        strategy : {"mean", "median", "zero"}
        """

        numeric_columns = dataframe.select_dtypes(
            include="number"
        ).columns

        for column in numeric_columns:

            if strategy == "mean":
                value = dataframe[column].mean()

            elif strategy == "median":
                value = dataframe[column].median()

            elif strategy == "zero":
                value = 0

            else:
                raise ValueError(
                    f"Unsupported strategy: {strategy}"
                )

            dataframe[column] = dataframe[column].fillna(value)

        logger.info(
            f"Missing values filled using '{strategy}' strategy."
        )

        return dataframe

    # --------------------------------------------------------

    @staticmethod
    def validate_columns(
        dataframe: pd.DataFrame,
        required_columns: Iterable[str],
    ) -> None:
        """
        Ensure required columns exist.
        """

        missing = [
            column
            for column in required_columns
            if column not in dataframe.columns
        ]

        if missing:
            raise ValueError(
                f"Missing required columns: {missing}"
            )

        logger.info("Required column validation passed.")

    # --------------------------------------------------------

    @staticmethod
    def convert_dtypes(
        dataframe: pd.DataFrame,
        dtype_mapping: dict,
    ) -> pd.DataFrame:
        """
        Convert column data types.
        """

        dataframe = dataframe.astype(dtype_mapping)

        logger.info("Column data types converted.")

        return dataframe

    # --------------------------------------------------------

    @staticmethod
    def normalize(
        dataframe: pd.DataFrame,
        columns: List[str],
    ) -> pd.DataFrame:
        """
        Min-Max normalize selected columns.
        """

        scaler = MinMaxScaler()

        dataframe[columns] = scaler.fit_transform(
            dataframe[columns]
        )

        logger.info(
            f"Normalized {len(columns)} column(s)."
        )

        return dataframe

    # --------------------------------------------------------

    @staticmethod
    def standardize(
        dataframe: pd.DataFrame,
        columns: List[str],
    ) -> pd.DataFrame:
        """
        Standardize selected columns.
        """

        scaler = StandardScaler()

        dataframe[columns] = scaler.fit_transform(
            dataframe[columns]
        )

        logger.info(
            f"Standardized {len(columns)} column(s)."
        )

        return dataframe

    # --------------------------------------------------------

    @staticmethod
    def dataset_statistics(
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Return descriptive statistics.
        """

        logger.info("Generating dataset statistics.")

        return dataframe.describe(include="all")

    # --------------------------------------------------------

    @staticmethod
    def dataframe_summary(
        dataframe: pd.DataFrame,
    ) -> None:
        """
        Print dataset summary.
        """

        print("\nDataset Summary")
        print("-" * 60)

        print(f"Rows       : {len(dataframe):,}")
        print(f"Columns    : {len(dataframe.columns)}")

        print("\nData Types")
        print(dataframe.dtypes)

        print("\nMissing Values")
        print(dataframe.isnull().sum())

        print("\nMemory Usage")
        print(
            f"{dataframe.memory_usage(deep=True).sum() / 1024:.2f} KB"
        )

        print("-" * 60)