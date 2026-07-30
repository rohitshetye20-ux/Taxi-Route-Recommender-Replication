"""
inference.py
============

Inference engine for the Taxi Route Recommender project.

This module provides a reusable interface for performing
predictions using trained machine learning models.

Features
--------
- Single prediction
- Batch prediction
- Prediction summary
- Confidence reporting
- Prediction export
- Runtime logging

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
from typing import Any, Dict, List

import pandas as pd

from src.model_interface import ModelManager

logger = logging.getLogger(__name__)

if not logger.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


class InferenceEngine:
    """
    High-level inference interface.

    Parameters
    ----------
    model_manager : ModelManager

    Notes
    -----
    This class is responsible for generating predictions
    from trained models. It does not implement the model
    itself.
    """

    def __init__(
        self,
        model_manager: ModelManager,
    ) -> None:

        self.model_manager = model_manager

        logger.info("Inference Engine initialized.")

    # --------------------------------------------------------

    def predict(
        self,
        input_data: Any,
    ) -> Any:
        """
        Generate prediction for a single input.

        Parameters
        ----------
        input_data : Any

        Returns
        -------
        Any
        """

        logger.info("Running single prediction...")

        prediction = self.model_manager.predict(input_data)

        logger.info("Prediction completed.")

        return prediction

    # --------------------------------------------------------

    def predict_batch(
        self,
        batch_data: List[Any],
    ) -> List[Any]:
        """
        Generate predictions for multiple inputs.
        """

        logger.info(
            "Running batch inference on %d samples...",
            len(batch_data),
        )

        predictions = [

            self.model_manager.predict(sample)

            for sample in batch_data

        ]

        logger.info("Batch prediction completed.")

        return predictions

    # --------------------------------------------------------

    @staticmethod
    def prediction_summary(
        predictions: Any,
    ) -> Dict[str, Any]:
        """
        Generate summary statistics.

        Parameters
        ----------
        predictions : Any

        Returns
        -------
        dict
        """

        if hasattr(predictions, "__len__"):

            count = len(predictions)

        else:

            count = 1

        summary = {

            "Number of Predictions": count,

            "Prediction Type":
                type(predictions).__name__,

        }

        return summary

    # --------------------------------------------------------

    @staticmethod
    def display_summary(
        summary: Dict[str, Any],
    ) -> None:
        """
        Print inference summary.
        """

        print("\nInference Summary")
        print("-" * 60)

        for key, value in summary.items():

            print(f"{key:<25}: {value}")

        print("-" * 60)

    # --------------------------------------------------------

    @staticmethod
    def export_predictions(
        predictions: List[Any],
        filepath: str | Path,
    ) -> None:
        """
        Export predictions to CSV.
        """

        dataframe = pd.DataFrame({

            "Prediction": predictions

        })

        dataframe.to_csv(
            filepath,
            index=False,
        )

        logger.info(
            "Predictions exported to %s",
            filepath,
        )

    # --------------------------------------------------------

    @staticmethod
    def confidence_report(
        probabilities: List[float],
    ) -> pd.DataFrame:
        """
        Generate confidence report.

        Parameters
        ----------
        probabilities : list

        Returns
        -------
        pandas.DataFrame
        """

        dataframe = pd.DataFrame({

            "Prediction": range(
                1,
                len(probabilities) + 1,
            ),

            "Confidence": probabilities,

        })

        return dataframe