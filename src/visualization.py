"""
visualization.py
================

Visualization utilities for the Taxi Route Recommender project.

This module provides reusable plotting functions for
exploratory analysis, model evaluation, graph visualization,
and publication-quality figures.

Features
--------
- Training history plots
- Prediction vs Actual visualization
- Confusion matrix visualization
- Correlation heatmap
- Network graph visualization
- Figure export

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
from typing import Dict, Optional

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

if not logger.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


class Visualizer:
    """
    Visualization engine for machine learning
    and graph analytics.
    """

    def __init__(self) -> None:
        plt.style.use("default")
        logger.info("Visualizer initialized.")

    # --------------------------------------------------------
    # Training History
    # --------------------------------------------------------

    @staticmethod
    def plot_training_history(
        history: Dict[str, list],
        save_path: Optional[str | Path] = None,
    ) -> None:
        """
        Plot training and validation loss.
        """

        plt.figure(figsize=(8, 5))

        if "loss" in history:
            plt.plot(history["loss"], label="Training Loss")

        if "val_loss" in history:
            plt.plot(history["val_loss"], label="Validation Loss")

        plt.title("Training History")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.legend()
        plt.grid(True)

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            logger.info("Figure saved to %s", save_path)

        plt.show()

    # --------------------------------------------------------
    # Prediction vs Actual
    # --------------------------------------------------------

    @staticmethod
    def plot_predictions(
        actual: np.ndarray,
        predicted: np.ndarray,
        save_path: Optional[str | Path] = None,
    ) -> None:
        """
        Plot predicted values against actual values.
        """

        plt.figure(figsize=(8, 5))

        plt.scatter(actual, predicted)

        plt.plot(
            [actual.min(), actual.max()],
            [actual.min(), actual.max()],
            linestyle="--",
        )

        plt.xlabel("Actual")
        plt.ylabel("Predicted")
        plt.title("Prediction vs Actual")
        plt.grid(True)

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            logger.info("Figure saved to %s", save_path)

        plt.show()

    # --------------------------------------------------------
    # Correlation Heatmap
    # --------------------------------------------------------

    @staticmethod
    def correlation_heatmap(
        dataframe: pd.DataFrame,
        save_path: Optional[str | Path] = None,
    ) -> None:
        """
        Plot feature correlation matrix.
        """

        correlation = dataframe.corr(numeric_only=True)

        plt.figure(figsize=(10, 8))

        plt.imshow(correlation, interpolation="nearest")

        plt.colorbar()

        plt.xticks(
            range(len(correlation.columns)),
            correlation.columns,
            rotation=90,
        )

        plt.yticks(
            range(len(correlation.columns)),
            correlation.columns,
        )

        plt.title("Correlation Heatmap")

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            logger.info("Figure saved to %s", save_path)

        plt.show()

    # --------------------------------------------------------
    # Confusion Matrix
    # --------------------------------------------------------

    @staticmethod
    def plot_confusion_matrix(
        matrix: np.ndarray,
        labels: list[str],
        save_path: Optional[str | Path] = None,
    ) -> None:
        """
        Plot confusion matrix.
        """

        plt.figure(figsize=(6, 6))

        plt.imshow(matrix)

        plt.title("Confusion Matrix")

        plt.colorbar()

        plt.xticks(range(len(labels)), labels)

        plt.yticks(range(len(labels)), labels)

        plt.xlabel("Predicted")

        plt.ylabel("Actual")

        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            logger.info("Figure saved to %s", save_path)

        plt.show()

    # --------------------------------------------------------
    # Network Graph
    # --------------------------------------------------------

    @staticmethod
    def plot_graph(
        graph: nx.Graph,
        save_path: Optional[str | Path] = None,
    ) -> None:
        """
        Visualize a NetworkX graph.
        """

        plt.figure(figsize=(10, 8))

        position = nx.spring_layout(
            graph,
            seed=42,
        )

        nx.draw_networkx(
            graph,
            pos=position,
            with_labels=False,
            node_size=25,
            width=0.5,
        )

        plt.title("Transportation Network")

        plt.axis("off")

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            logger.info("Figure saved to %s", save_path)

        plt.show()

    # --------------------------------------------------------
    # Save Current Figure
    # --------------------------------------------------------

    @staticmethod
    def save_current_figure(
        filepath: str | Path,
    ) -> None:
        """
        Save the current active figure.
        """

        plt.savefig(
            filepath,
            dpi=300,
            bbox_inches="tight",
        )

        logger.info(
            "Figure exported to %s",
            filepath,
        )

    # --------------------------------------------------------
    # Close All Figures
    # --------------------------------------------------------

    @staticmethod
    def close_all() -> None:
        """
        Close all open matplotlib figures.
        """

        plt.close("all")

        logger.info("All figures closed.")