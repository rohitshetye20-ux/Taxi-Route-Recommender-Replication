"""
data_loader.py
==============

Centralized data loading utilities for the Taxi Route Recommender project.

This module provides a unified interface for loading datasets used
throughout the project. It supports CSV, TXT, and NPZ formats,
performs input validation, and offers consistent logging and
error handling.

Supported Formats
-----------------
- CSV (.csv)
- Text (.txt)
- NumPy Archive (.npz)

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict, List, Optional, Union

import numpy as np
import pandas as pd

# ------------------------------------------------------------
# Configure Logger
# ------------------------------------------------------------

logger = logging.getLogger(__name__)

if not logger.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


# ------------------------------------------------------------
# DataLoader Class
# ------------------------------------------------------------

class DataLoader:
    """
    Unified interface for loading project datasets.

    Parameters
    ----------
    data_directory : str or Path
        Root directory containing project datasets.

    Examples
    --------
    >>> loader = DataLoader("data")
    >>> df = loader.load_csv("network_properties.csv")
    """

    def __init__(self, data_directory: Union[str, Path]) -> None:
        self.data_directory = Path(data_directory)

        if not self.data_directory.exists():
            raise FileNotFoundError(
                f"Data directory not found: {self.data_directory}"
            )

    # --------------------------------------------------------

    def _resolve_path(self, filename: str) -> Path:
        """
        Resolve a filename relative to the data directory.
        """

        file_path = self.data_directory / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {file_path}"
            )

        return file_path

    # --------------------------------------------------------

    def load_csv(
        self,
        filename: str,
        **kwargs,
    ) -> pd.DataFrame:
        """
        Load a CSV file.

        Parameters
        ----------
        filename : str
            CSV filename.

        Returns
        -------
        pandas.DataFrame
        """

        file_path = self._resolve_path(filename)

        logger.info(f"Loading CSV: {file_path}")

        dataframe = pd.read_csv(file_path, **kwargs)

        logger.info(
            f"Loaded {len(dataframe):,} rows × "
            f"{len(dataframe.columns)} columns"
        )

        return dataframe

    # --------------------------------------------------------

    def load_txt(
        self,
        filename: str,
        delimiter: Optional[str] = None,
        **kwargs,
    ) -> pd.DataFrame:
        """
        Load a text file.

        Returns
        -------
        pandas.DataFrame
        """

        file_path = self._resolve_path(filename)

        logger.info(f"Loading TXT: {file_path}")

        dataframe = pd.read_csv(
            file_path,
            delimiter=delimiter,
            **kwargs,
        )

        return dataframe

    # --------------------------------------------------------

    def load_npz(
        self,
        filename: str,
    ) -> Dict[str, np.ndarray]:
        """
        Load a NumPy compressed archive.

        Returns
        -------
        dict
            Dictionary containing arrays.
        """

        file_path = self._resolve_path(filename)

        logger.info(f"Loading NPZ: {file_path}")

        archive = np.load(file_path, allow_pickle=True)

        return {
            key: archive[key]
            for key in archive.files
        }

    # --------------------------------------------------------

    def dataset_exists(
        self,
        filename: str,
    ) -> bool:
        """
        Check whether a dataset exists.
        """

        return (self.data_directory / filename).exists()

    # --------------------------------------------------------

    def list_datasets(self) -> List[str]:
        """
        Return all datasets inside the data directory.
        """

        datasets = sorted(
            file.name
            for file in self.data_directory.iterdir()
            if file.is_file()
        )

        logger.info(
            f"Discovered {len(datasets)} dataset(s)."
        )

        return datasets

    # --------------------------------------------------------

    @staticmethod
    def summarize_dataframe(
        dataframe: pd.DataFrame,
    ) -> None:
        """
        Print a concise dataset summary.
        """

        print("\nDataset Summary")
        print("-" * 60)

        print(f"Rows      : {len(dataframe):,}")
        print(f"Columns   : {len(dataframe.columns)}")

        print("\nColumn Names")
        print(dataframe.columns.tolist())

        print("\nMissing Values")
        print(dataframe.isnull().sum())

        print("\nData Types")
        print(dataframe.dtypes)

        print("-" * 60)