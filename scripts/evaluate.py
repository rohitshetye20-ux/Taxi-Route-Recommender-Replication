"""
evaluate.py
===========

Evaluate a trained GCN-LSTM model for the Taxi Route Recommender project.

This script loads a trained model and evaluation dataset,
computes performance metrics, prints a summary, and exports
evaluation results for reporting and visualization.

Usage
-----
python scripts/evaluate.py

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

# ============================================================
# Project Root
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT))

# ============================================================
# Imports
# ============================================================

from src.data_loader import DataLoader
from src.evaluation import ModelEvaluator
from src.model_interface import ModelManager
from src.utils import (
    Timer,
    ensure_directory,
    get_logger,
)

logger = get_logger(__name__)

# ============================================================
# Default Paths
# ============================================================

MODEL_DIR = PROJECT_ROOT / "models"

DATA_DIR = PROJECT_ROOT / "data"

OUTPUT_DIR = PROJECT_ROOT / "output"

DEFAULT_MODEL = MODEL_DIR / "gcn_lstm_model.keras"

DEFAULT_TEST_DATA = DATA_DIR / "processed" / "test_dataset.csv"

DEFAULT_JSON = OUTPUT_DIR / "evaluation_metrics.json"

DEFAULT_CSV = OUTPUT_DIR / "evaluation_metrics.csv"

# ============================================================
# Placeholder Model
# Replace with actual implementation
# ============================================================


class GCNLSTMModel:

    def build(self):
        pass

    def train(self, train_data, validation_data=None):
        return {}

    def predict(self, input_data):
        return input_data["prediction"].values

    def evaluate(self, test_data):
        return {}

    def save(self, filepath):
        pass

    def load(self, filepath):
        logger.info("Loaded model: %s", filepath)


# ============================================================
# Evaluation Pipeline
# ============================================================


def evaluate_model(
    model_file: Path,
    test_file: Path,
    json_output: Path,
    csv_output: Path,
):

    ensure_directory(json_output.parent)

    loader = DataLoader()

    dataframe = loader.load_csv(test_file)

    logger.info(
        "Loaded evaluation dataset (%d rows).",
        len(dataframe),
    )

    model = GCNLSTMModel()

    manager = ModelManager(model)

    manager.load_model(model_file)

    predictions = manager.predict(dataframe)

    metrics = ModelEvaluator.regression_metrics(
        dataframe["target"],
        predictions,
    )

    print("\nEvaluation Results")
    print("-" * 50)

    for key, value in metrics.items():
        print(f"{key:<15}: {value:.4f}")

    print("-" * 50)

    # --------------------------------------------------------
    # Export JSON
    # --------------------------------------------------------

    with open(
        json_output,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            metrics,
            file,
            indent=4,
        )

    # --------------------------------------------------------
    # Export CSV
    # --------------------------------------------------------

    pd.DataFrame(
        metrics.items(),
        columns=[
            "Metric",
            "Value",
        ],
    ).to_csv(
        csv_output,
        index=False,
    )

    logger.info("Evaluation completed successfully.")


# ============================================================
# CLI
# ============================================================


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Evaluate trained GCN-LSTM model",
    )

    parser.add_argument(
        "--model",
        type=Path,
        default=DEFAULT_MODEL,
    )

    parser.add_argument(
        "--test-data",
        type=Path,
        default=DEFAULT_TEST_DATA,
    )

    parser.add_argument(
        "--json-output",
        type=Path,
        default=DEFAULT_JSON,
    )

    parser.add_argument(
        "--csv-output",
        type=Path,
        default=DEFAULT_CSV,
    )

    return parser.parse_args()


# ============================================================
# Main
# ============================================================


def main():

    args = parse_arguments()

    with Timer("Model Evaluation"):

        evaluate_model(
            model_file=args.model,
            test_file=args.test_data,
            json_output=args.json_output,
            csv_output=args.csv_output,
        )


if __name__ == "__main__":

    main()