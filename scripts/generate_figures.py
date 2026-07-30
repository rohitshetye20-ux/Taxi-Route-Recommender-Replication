"""
generate_figures.py
===================

Generate all publication-quality figures for the
Taxi Route Recommender project.

This script recreates every figure used in the
research paper, report, presentation, and GitHub
documentation.

Usage
-----
python scripts/generate_figures.py

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

import numpy as np
import pandas as pd

# ============================================================
# Project Root
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT))

# ============================================================
# Imports
# ============================================================

from src.visualization import Visualizer
from src.utils import (
    Timer,
    ensure_directory,
    get_logger,
)

logger = get_logger(__name__)

# ============================================================
# Paths
# ============================================================

OUTPUT_DIR = PROJECT_ROOT / "output"

FIGURE_DIR = PROJECT_ROOT / "figures"

TRAINING_HISTORY = OUTPUT_DIR / "training_history.json"

EVALUATION_METRICS = OUTPUT_DIR / "evaluation_metrics.csv"

PREDICTIONS = OUTPUT_DIR / "predictions.csv"

# ============================================================
# Figure Generation
# ============================================================


def generate_training_history(
    visualizer: Visualizer,
):
    """
    Generate training history plot.
    """

    if not TRAINING_HISTORY.exists():

        logger.warning(
            "Training history not found. Skipping."
        )

        return

    with open(
        TRAINING_HISTORY,
        "r",
        encoding="utf-8",
    ) as file:

        history = json.load(file)

    visualizer.plot_training_history(

        history,

        save_path=FIGURE_DIR / "training_history.png",

    )

    logger.info(
        "Training history figure created."
    )


# ------------------------------------------------------------


def generate_prediction_plot(
    visualizer: Visualizer,
):
    """
    Generate prediction visualization.
    """

    if not PREDICTIONS.exists():

        logger.warning(
            "Prediction file not found. Skipping."
        )

        return

    dataframe = pd.read_csv(PREDICTIONS)

    if {

        "target",

        "prediction",

    }.issubset(dataframe.columns):

        visualizer.plot_predictions(

            dataframe["target"].values,

            dataframe["prediction"].values,

            save_path=FIGURE_DIR / "prediction_vs_actual.png",

        )

        logger.info(
            "Prediction figure created."
        )


# ------------------------------------------------------------


def generate_correlation_heatmap(
    visualizer: Visualizer,
):
    """
    Generate feature correlation heatmap.
    """

    if not PREDICTIONS.exists():

        return

    dataframe = pd.read_csv(PREDICTIONS)

    visualizer.correlation_heatmap(

        dataframe,

        save_path=FIGURE_DIR / "correlation_heatmap.png",

    )

    logger.info(
        "Correlation heatmap created."
    )


# ------------------------------------------------------------


def generate_dummy_confusion_matrix(
    visualizer: Visualizer,
):
    """
    Placeholder confusion matrix.

    Replace with actual evaluation results.
    """

    matrix = np.array([

        [91, 9],

        [6, 94],

    ])

    visualizer.plot_confusion_matrix(

        matrix,

        labels=["Negative", "Positive"],

        save_path=FIGURE_DIR / "confusion_matrix.png",

    )

    logger.info(
        "Confusion matrix created."
    )


# ============================================================
# Main Pipeline
# ============================================================


def generate_all_figures():

    ensure_directory(FIGURE_DIR)

    visualizer = Visualizer()

    logger.info(
        "Generating publication figures..."
    )

    generate_training_history(
        visualizer,
    )

    generate_prediction_plot(
        visualizer,
    )

    generate_correlation_heatmap(
        visualizer,
    )

    generate_dummy_confusion_matrix(
        visualizer,
    )

    logger.info(
        "Figure generation completed."
    )


# ============================================================
# CLI
# ============================================================


def parse_arguments():

    parser = argparse.ArgumentParser(

        description="Generate publication figures",

    )

    return parser.parse_args()


# ============================================================
# Main
# ============================================================


def main():

    parse_arguments()

    with Timer(

        "Figure Generation",

    ):

        generate_all_figures()


if __name__ == "__main__":

    main()