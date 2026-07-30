"""
test_inference.py
=================

Unit tests for src.inference.

This module verifies prediction workflows, batch inference,
prediction summaries, and error handling.

Run
---
pytest tests/test_inference.py

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from src.inference import InferenceEngine
from src.model_interface import ModelManager


# ============================================================
# Fixture
# ============================================================

@pytest.fixture
def inference_engine(dummy_model):

    manager = ModelManager(dummy_model)

    return InferenceEngine(manager)


# ============================================================
# Prediction
# ============================================================

def test_predict_dataframe(
    inference_engine,
    sample_dataframe,
):

    predictions = inference_engine.predict(
        sample_dataframe
    )

    assert len(predictions) == len(sample_dataframe)


def test_prediction_is_iterable(
    inference_engine,
    sample_dataframe,
):

    predictions = inference_engine.predict(
        sample_dataframe
    )

    assert hasattr(predictions, "__len__")


def test_prediction_not_empty(
    inference_engine,
    sample_dataframe,
):

    predictions = inference_engine.predict(
        sample_dataframe
    )

    assert len(predictions) > 0


# ============================================================
# Prediction Summary
# ============================================================

def test_prediction_summary(
    inference_engine,
):

    predictions = np.array(
        [10, 20, 30, 40]
    )

    summary = inference_engine.prediction_summary(
        predictions
    )

    assert isinstance(summary, dict)


def test_prediction_summary_keys(
    inference_engine,
):

    predictions = np.array(
        [10, 20, 30]
    )

    summary = inference_engine.prediction_summary(
        predictions
    )

    expected = {
        "count",
        "minimum",
        "maximum",
        "mean",
        "standard_deviation",
    }

    assert expected.issubset(summary.keys())


def test_prediction_summary_values(
    inference_engine,
):

    predictions = np.array(
        [10, 20, 30]
    )

    summary = inference_engine.prediction_summary(
        predictions
    )

    assert summary["count"] == 3
    assert summary["minimum"] == 10
    assert summary["maximum"] == 30


# ============================================================
# Empty Input
# ============================================================

def test_empty_prediction_summary(
    inference_engine,
):

    predictions = np.array([])

    with pytest.raises(ValueError):

        inference_engine.prediction_summary(
            predictions
        )


# ============================================================
# Batch Prediction
# ============================================================

def test_multiple_prediction_calls(
    inference_engine,
    sample_dataframe,
):

    first = inference_engine.predict(
        sample_dataframe
    )

    second = inference_engine.predict(
        sample_dataframe
    )

    assert len(first) == len(second)


# ============================================================
# Prediction Export
# ============================================================

def test_prediction_dataframe_creation(
    inference_engine,
    sample_dataframe,
):

    predictions = inference_engine.predict(
        sample_dataframe
    )

    result = sample_dataframe.copy()

    result["prediction"] = predictions

    assert "prediction" in result.columns


def test_prediction_column_length(
    inference_engine,
    sample_dataframe,
):

    predictions = inference_engine.predict(
        sample_dataframe
    )

    assert len(predictions) == len(sample_dataframe)


# ============================================================
# Display Summary
# ============================================================

def test_display_summary(
    inference_engine,
):

    summary = {

        "count": 5,

        "minimum": 10,

        "maximum": 30,

        "mean": 20,

        "standard_deviation": 7,

    }

    inference_engine.display_summary(
        summary
    )


# ============================================================
# Integration
# ============================================================

def test_complete_inference_pipeline(
    inference_engine,
    sample_dataframe,
):

    predictions = inference_engine.predict(
        sample_dataframe
    )

    summary = inference_engine.prediction_summary(
        predictions
    )

    assert len(predictions) == len(sample_dataframe)

    assert summary["count"] == len(sample_dataframe)

    assert summary["maximum"] >= summary["minimum"]