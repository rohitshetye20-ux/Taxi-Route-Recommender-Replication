"""
model_interface.py
==================

Unified machine learning model interface for the
Taxi Route Recommender project.

This module defines a reusable interface for loading,
training, evaluating, saving, and performing inference
with graph-based machine learning models.

The interface is intentionally framework-agnostic so that
different implementations (TensorFlow, PyTorch, etc.)
can be integrated without changing the rest of the project.

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

if not logger.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


# ============================================================
# Abstract Base Model
# ============================================================

class BaseModel(ABC):
    """
    Abstract base class for machine learning models.

    Every model implementation should inherit from this class.
    """

    @abstractmethod
    def build(self) -> None:
        """Build the model architecture."""
        pass

    @abstractmethod
    def train(
        self,
        train_data: Any,
        validation_data: Optional[Any] = None,
    ) -> Dict[str, Any]:
        """
        Train the model.
        """
        pass

    @abstractmethod
    def predict(
        self,
        input_data: Any,
    ) -> Any:
        """
        Perform inference.
        """
        pass

    @abstractmethod
    def evaluate(
        self,
        test_data: Any,
    ) -> Dict[str, float]:
        """
        Evaluate the trained model.
        """
        pass

    @abstractmethod
    def save(
        self,
        filepath: str | Path,
    ) -> None:
        """
        Save model weights.
        """
        pass

    @abstractmethod
    def load(
        self,
        filepath: str | Path,
    ) -> None:
        """
        Load pretrained weights.
        """
        pass


# ============================================================
# Model Manager
# ============================================================

class ModelManager:
    """
    High-level interface for interacting with models.

    This class provides a consistent API regardless
    of the underlying machine learning framework.
    """

    def __init__(
        self,
        model: BaseModel,
    ) -> None:

        self.model = model

        logger.info(
            "ModelManager initialized with %s",
            model.__class__.__name__,
        )

    # --------------------------------------------------------

    def build_model(self) -> None:
        """
        Build model architecture.
        """

        logger.info("Building model...")

        self.model.build()

    # --------------------------------------------------------

    def train_model(
        self,
        train_data: Any,
        validation_data: Optional[Any] = None,
    ) -> Dict[str, Any]:
        """
        Train the model.
        """

        logger.info("Training started...")

        history = self.model.train(
            train_data,
            validation_data,
        )

        logger.info("Training completed.")

        return history

    # --------------------------------------------------------

    def evaluate_model(
        self,
        test_data: Any,
    ) -> Dict[str, float]:
        """
        Evaluate trained model.
        """

        logger.info("Evaluating model...")

        results = self.model.evaluate(test_data)

        logger.info("Evaluation completed.")

        return results

    # --------------------------------------------------------

    def predict(
        self,
        input_data: Any,
    ) -> Any:
        """
        Perform inference.
        """

        logger.info("Generating predictions...")

        predictions = self.model.predict(input_data)

        logger.info("Prediction completed.")

        return predictions

    # --------------------------------------------------------

    def save_model(
        self,
        filepath: str | Path,
    ) -> None:
        """
        Save trained model.
        """

        self.model.save(filepath)

        logger.info(
            "Model saved to %s",
            filepath,
        )

    # --------------------------------------------------------

    def load_model(
        self,
        filepath: str | Path,
    ) -> None:
        """
        Load trained model.
        """

        self.model.load(filepath)

        logger.info(
            "Model loaded from %s",
            filepath,
        )

    # --------------------------------------------------------

    @staticmethod
    def model_summary(
        model_information: Dict[str, Any],
    ) -> None:
        """
        Print model summary.
        """

        print("\nModel Summary")
        print("-" * 60)

        for key, value in model_information.items():
            print(f"{key:<25}: {value}")

        print("-" * 60)