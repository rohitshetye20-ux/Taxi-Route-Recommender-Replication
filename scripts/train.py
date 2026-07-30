"""
train.py
========

Train the GCN-LSTM model for the Taxi Route Recommender project.

This script orchestrates the end-to-end training workflow,
including dataset loading, graph loading, model construction,
training, checkpoint saving, and training history export.

Usage
-----
python scripts/train.py

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

# ============================================================
# Project Root
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT))

# ============================================================
# Imports
# ============================================================

from src.data_loader import DataLoader
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

GRAPH_DIR = PROJECT_ROOT / "data" / "graph"

MODEL_DIR = PROJECT_ROOT / "models"

HISTORY_DIR = PROJECT_ROOT / "output"

DEFAULT_GRAPH = GRAPH_DIR / "transportation_network.graphml"

DEFAULT_MODEL = MODEL_DIR / "gcn_lstm_model.keras"

DEFAULT_HISTORY = HISTORY_DIR / "training_history.json"

# ============================================================
# Dummy Model
# Replace with actual implementation
# ============================================================


class GCNLSTMModel:
    """
    Placeholder implementation.

    Replace this class with the actual
    TensorFlow implementation.
    """

    def build(self):

        logger.info("Building GCN-LSTM model...")

    def train(
        self,
        train_data,
        validation_data=None,
    ):

        logger.info("Training started...")

        history = {

            "loss": [
                1.00,
                0.82,
                0.61,
                0.48,
                0.39,
            ],

            "val_loss": [
                1.05,
                0.89,
                0.71,
                0.58,
                0.50,
            ],

        }

        logger.info("Training completed.")

        return history

    def predict(self, data):

        return []

    def evaluate(self, data):

        return {}

    def save(
        self,
        filepath,
    ):

        Path(filepath).touch()

        logger.info(
            "Model saved to %s",
            filepath,
        )

    def load(
        self,
        filepath,
    ):

        logger.info(
            "Loaded model from %s",
            filepath,
        )


# ============================================================
# Training Pipeline
# ============================================================


def train_model(
    graph_file: Path,
    model_output: Path,
    history_output: Path,
):

    ensure_directory(model_output.parent)

    ensure_directory(history_output.parent)

    loader = DataLoader()

    logger.info(
        "Loading graph dataset..."
    )

    graph = loader.load_graphml(
        graph_file,
    )

    logger.info(
        "Graph loaded successfully."
    )

    model = GCNLSTMModel()

    manager = ModelManager(model)

    manager.build_model()

    history = manager.train_model(graph)

    manager.save_model(
        model_output,
    )

    with open(
        history_output,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            history,
            file,
            indent=4,
        )

    logger.info(
        "Training history exported."
    )

    logger.info(
        "Training pipeline completed."
    )


# ============================================================
# CLI
# ============================================================


def parse_arguments():

    parser = argparse.ArgumentParser(
        description="GCN-LSTM Training"
    )

    parser.add_argument(
        "--graph",
        type=Path,
        default=DEFAULT_GRAPH,
        help="Input GraphML file.",
    )

    parser.add_argument(
        "--model-output",
        type=Path,
        default=DEFAULT_MODEL,
        help="Output model file.",
    )

    parser.add_argument(
        "--history-output",
        type=Path,
        default=DEFAULT_HISTORY,
        help="Training history JSON.",
    )

    return parser.parse_args()


# ============================================================
# Main
# ============================================================


def main():

    args = parse_arguments()

    with Timer(
        "Model Training"
    ):

        train_model(
            graph_file=args.graph,
            model_output=args.model_output,
            history_output=args.history_output,
        )


if __name__ == "__main__":

    main()