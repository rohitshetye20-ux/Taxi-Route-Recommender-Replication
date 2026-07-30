"""
preprocess.py
=============

Execute the complete data preprocessing pipeline.

This script loads the raw dataset, performs data cleaning,
preprocessing, and exports the processed dataset for
subsequent graph construction and model training.

Usage
-----
python scripts/preprocess.py

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

# ------------------------------------------------------------------
# Project Root
# ------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT))

# ------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------

from src.data_loader import DataLoader
from src.preprocessing import DataPreprocessor
from src.utils import (
    Timer,
    ensure_directory,
    get_logger,
)

# ------------------------------------------------------------------
# Logger
# ------------------------------------------------------------------

logger = get_logger(__name__)

# ------------------------------------------------------------------
# Default Locations
# ------------------------------------------------------------------

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

DEFAULT_INPUT = RAW_DATA_DIR / "taxi_routes.csv"

DEFAULT_OUTPUT = PROCESSED_DATA_DIR / "taxi_routes_processed.csv"

# ------------------------------------------------------------------
# Pipeline
# ------------------------------------------------------------------


def preprocess_dataset(
    input_file: Path,
    output_file: Path,
) -> None:
    """
    Execute preprocessing workflow.
    """

    ensure_directory(output_file.parent)

    loader = DataLoader()

    preprocessor = DataPreprocessor()

    logger.info("Loading dataset...")

    dataframe = loader.load_csv(input_file)

    logger.info(
        "Dataset loaded successfully: %d rows × %d columns",
        len(dataframe),
        len(dataframe.columns),
    )

    logger.info("Running preprocessing pipeline...")

    dataframe = preprocessor.remove_duplicates(dataframe)

    dataframe = preprocessor.handle_missing_values(dataframe)

    dataframe = preprocessor.standardize_column_names(dataframe)

    dataframe = preprocessor.remove_whitespace(dataframe)

    logger.info("Saving processed dataset...")

    dataframe.to_csv(
        output_file,
        index=False,
    )

    logger.info(
        "Processed dataset saved to:\n%s",
        output_file,
    )

    logger.info("Preprocessing completed successfully.")


# ------------------------------------------------------------------
# Command Line Interface
# ------------------------------------------------------------------

def parse_arguments():
    """
    Parse command-line arguments.
    """

    parser = argparse.ArgumentParser(
        description="Taxi Route Dataset Preprocessing",
    )

    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help="Path to raw CSV dataset.",
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Destination for processed dataset.",
    )

    return parser.parse_args()


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

def main():

    args = parse_arguments()

    with Timer("Data Preprocessing"):

        preprocess_dataset(
            input_file=args.input,
            output_file=args.output,
        )


if __name__ == "__main__":

    main()