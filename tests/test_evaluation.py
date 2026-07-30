"""
test_evaluation.py
==================

Unit tests for src.evaluation.

This module verifies regression metrics, evaluation reports,
summary generation, and error handling.

Run
---
pytest tests/test_evaluation.py

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import numpy as np
import pytest

from src.evaluation import ModelEvaluator


# ============================================================
# Fixture
# ============================================================

@pytest.fixture
def evaluator():

    return ModelEvaluator()


# ============================================================
# MAE
# ============================================================

def test_mean_absolute_error(
    evaluator,
    sample_targets,
    sample_predictions,
):

    mae = evaluator.mean_absolute_error(
        sample_targets,
        sample_predictions,
    )

    assert mae >= 0


# ============================================================
# MSE
# ============================================================

def test_mean_squared_error(
    evaluator,
    sample_targets,
    sample_predictions,
):

    mse = evaluator.mean_squared_error(
        sample_targets,
        sample_predictions,
    )

    assert mse >= 0


# ============================================================
# RMSE
# ============================================================

def test_root_mean_squared_error(
    evaluator,
    sample_targets,
    sample_predictions,
):

    rmse = evaluator.root_mean_squared_error(
        sample_targets,
        sample_predictions,
    )

    assert rmse >= 0


# ============================================================
# R²
# ============================================================

def test_r2_score(
    evaluator,
    sample_targets,
    sample_predictions,
):

    score = evaluator.r2_score(
        sample_targets,
        sample_predictions,
    )

    assert score <= 1.0


# ============================================================
# Complete Evaluation
# ============================================================

def test_evaluate(
    evaluator,
    sample_targets,
    sample_predictions,
):

    metrics = evaluator.evaluate(
        sample_targets,
        sample_predictions,
    )

    assert isinstance(metrics, dict)


def test_evaluation_keys(
    evaluator,
    sample_targets,
    sample_predictions,
):

    metrics = evaluator.evaluate(
        sample_targets,
        sample_predictions,
    )

    expected = {

        "mae",

        "mse",

        "rmse",

        "r2",

    }

    assert expected.issubset(metrics.keys())


# ============================================================
# Perfect Prediction
# ============================================================

def test_perfect_prediction(evaluator):

    values = np.array(

        [10, 20, 30, 40]

    )

    metrics = evaluator.evaluate(

        values,

        values,

    )

    assert metrics["mae"] == 0

    assert metrics["mse"] == 0

    assert metrics["rmse"] == 0

    assert metrics["r2"] == 1.0


# ============================================================
# Poor Prediction
# ============================================================

def test_poor_prediction(evaluator):

    actual = np.array(

        [10, 20, 30]

    )

    predicted = np.array(

        [100, 200, 300]

    )

    metrics = evaluator.evaluate(

        actual,

        predicted,

    )

    assert metrics["mae"] > 0


# ============================================================
# Shape Validation
# ============================================================

def test_mismatched_array_lengths(evaluator):

    actual = np.array(

        [1, 2, 3]

    )

    predicted = np.array(

        [1, 2]

    )

    with pytest.raises(ValueError):

        evaluator.evaluate(

            actual,

            predicted,

        )


# ============================================================
# Empty Arrays
# ============================================================

def test_empty_arrays(evaluator):

    actual = np.array([])

    predicted = np.array([])

    with pytest.raises(ValueError):

        evaluator.evaluate(

            actual,

            predicted,

        )


# ============================================================
# Summary Report
# ============================================================

def test_summary_report(
    evaluator,
    sample_targets,
    sample_predictions,
):

    metrics = evaluator.evaluate(

        sample_targets,

        sample_predictions,

    )

    report = evaluator.summary_report(

        metrics,

    )

    assert isinstance(report, str)


# ============================================================
# Multiple Evaluations
# ============================================================

def test_multiple_evaluations(
    evaluator,
    sample_targets,
    sample_predictions,
):

    first = evaluator.evaluate(

        sample_targets,

        sample_predictions,

    )

    second = evaluator.evaluate(

        sample_targets,

        sample_predictions,

    )

    assert first == second


# ============================================================
# Numeric Types
# ============================================================

def test_metric_types(
    evaluator,
    sample_targets,
    sample_predictions,
):

    metrics = evaluator.evaluate(

        sample_targets,

        sample_predictions,

    )

    assert isinstance(metrics["mae"], float)

    assert isinstance(metrics["mse"], float)

    assert isinstance(metrics["rmse"], float)

    assert isinstance(metrics["r2"], float)


# ============================================================
# Integration
# ============================================================

def test_complete_evaluation_pipeline(
    evaluator,
    sample_targets,
    sample_predictions,
):

    metrics = evaluator.evaluate(

        sample_targets,

        sample_predictions,

    )

    report = evaluator.summary_report(

        metrics,

    )

    assert report

    assert metrics["mae"] >= 0