"""
evaluation.py
=============

Model evaluation utilities for the Taxi Route Recommender project.

This module provides reusable evaluation functions for
machine learning models, including regression metrics,
classification metrics, performance summaries, and
result reporting.

Features
--------
- Regression metrics
- Classification metrics
- Confusion matrix
- Performance report
- Metric comparison
- Evaluation summary

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import logging
from typing import Dict, List

import numpy as np
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    confusion_matrix,
)

logger = logging.getLogger(__name__)

if not logger.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


class ModelEvaluator:
    """
    Evaluate machine learning model performance.
    """

    # --------------------------------------------------------
    # Regression Metrics
    # --------------------------------------------------------

    @staticmethod
    def regression_metrics(
        y_true,
        y_pred,
    ) -> Dict[str, float]:
        """
        Compute regression evaluation metrics.
        """

        mse = mean_squared_error(y_true, y_pred)

        metrics = {

            "MAE":
                mean_absolute_error(y_true, y_pred),

            "MSE":
                mse,

            "RMSE":
                np.sqrt(mse),

            "R²":
                r2_score(y_true, y_pred),
        }

        logger.info("Regression metrics computed.")

        return metrics

    # --------------------------------------------------------
    # Classification Metrics
    # --------------------------------------------------------

    @staticmethod
    def classification_metrics(
        y_true,
        y_pred,
    ) -> Dict[str, float]:
        """
        Compute classification metrics.
        """

        metrics = {

            "Accuracy":
                accuracy_score(y_true, y_pred),

            "Precision":
                precision_score(
                    y_true,
                    y_pred,
                    average="weighted",
                    zero_division=0,
                ),

            "Recall":
                recall_score(
                    y_true,
                    y_pred,
                    average="weighted",
                    zero_division=0,
                ),

            "F1 Score":
                f1_score(
                    y_true,
                    y_pred,
                    average="weighted",
                    zero_division=0,
                ),
        }

        logger.info("Classification metrics computed.")

        return metrics

    # --------------------------------------------------------
    # Confusion Matrix
    # --------------------------------------------------------

    @staticmethod
    def confusion(
        y_true,
        y_pred,
    ) -> np.ndarray:
        """
        Compute confusion matrix.
        """

        logger.info("Generating confusion matrix.")

        return confusion_matrix(
            y_true,
            y_pred,
        )

    # --------------------------------------------------------
    # Metric Comparison
    # --------------------------------------------------------

    @staticmethod
    def compare_models(
        results: Dict[str, Dict[str, float]],
    ) -> pd.DataFrame:
        """
        Compare evaluation metrics across models.

        Parameters
        ----------
        results : dict

        Returns
        -------
        pandas.DataFrame
        """

        dataframe = pd.DataFrame(results).T

        logger.info(
            "Compared %d model(s).",
            len(dataframe),
        )

        return dataframe

    # --------------------------------------------------------
    # Evaluation Summary
    # --------------------------------------------------------

    @staticmethod
    def summary(
        metrics: Dict[str, float],
    ) -> None:
        """
        Print evaluation summary.
        """

        print("\nEvaluation Summary")
        print("-" * 60)

        for key, value in metrics.items():

            if isinstance(value, float):

                print(f"{key:<20}: {value:.4f}")

            else:

                print(f"{key:<20}: {value}")

        print("-" * 60)

    # --------------------------------------------------------
    # Export Metrics
    # --------------------------------------------------------

    @staticmethod
    def export_metrics(
        metrics: Dict[str, float],
        filepath: str,
    ) -> None:
        """
        Export evaluation metrics to CSV.
        """

        dataframe = pd.DataFrame(

            metrics.items(),

            columns=[
                "Metric",
                "Value",
            ],

        )

        dataframe.to_csv(
            filepath,
            index=False,
        )

        logger.info(
            "Metrics exported to %s",
            filepath,
        )

    # --------------------------------------------------------
    # Best Model
    # --------------------------------------------------------

    @staticmethod
    def best_model(
        comparison: pd.DataFrame,
        metric: str,
        maximize: bool = True,
    ) -> pd.Series:
        """
        Select the best-performing model.

        Parameters
        ----------
        comparison : DataFrame
            Output from compare_models().

        metric : str
            Metric used for comparison.

        maximize : bool
            True for metrics like Accuracy or F1.
            False for metrics like RMSE or MAE.
        """

        if maximize:

            return comparison.loc[
                comparison[metric].idxmax()
            ]

        return comparison.loc[
            comparison[metric].idxmin()
        ]