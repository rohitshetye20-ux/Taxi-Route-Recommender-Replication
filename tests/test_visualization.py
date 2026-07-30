"""
test_visualization.py
=====================

Unit tests for src.visualization.

This module verifies generation and export of
publication-quality figures.

Run
---
pytest tests/test_visualization.py

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

from src.visualization import Visualizer


# ============================================================
# Fixture
# ============================================================

@pytest.fixture
def visualizer():

    return Visualizer()


# ============================================================
# Training History
# ============================================================

def test_plot_training_history(
    visualizer,
    temp_output_dir,
):

    history = {

        "loss": [1.0, 0.8, 0.5],

        "val_loss": [1.2, 0.9, 0.6],

    }

    output = temp_output_dir / "training.png"

    visualizer.plot_training_history(

        history,

        save_path=output,

    )

    assert output.exists()


# ============================================================
# Prediction Plot
# ============================================================

def test_plot_predictions(
    visualizer,
    temp_output_dir,
):

    actual = np.array([1, 2, 3, 4])

    predicted = np.array([1.1, 2.0, 2.8, 4.2])

    output = temp_output_dir / "prediction.png"

    visualizer.plot_predictions(

        actual,

        predicted,

        save_path=output,

    )

    assert output.exists()


# ============================================================
# Correlation Heatmap
# ============================================================

def test_correlation_heatmap(
    visualizer,
    temp_output_dir,
):

    dataframe = pd.DataFrame({

        "A": [1, 2, 3],

        "B": [4, 5, 6],

        "C": [7, 8, 9],

    })

    output = temp_output_dir / "heatmap.png"

    visualizer.correlation_heatmap(

        dataframe,

        save_path=output,

    )

    assert output.exists()


# ============================================================
# Confusion Matrix
# ============================================================

def test_confusion_matrix(
    visualizer,
    temp_output_dir,
):

    matrix = np.array([

        [5, 1],

        [2, 7],

    ])

    output = temp_output_dir / "confusion.png"

    visualizer.plot_confusion_matrix(

        matrix,

        labels=["Negative", "Positive"],

        save_path=output,

    )

    assert output.exists()


# ============================================================
# Output Files
# ============================================================

def test_generated_file_not_empty(
    visualizer,
    temp_output_dir,
):

    history = {

        "loss": [1.0, 0.7],

    }

    output = temp_output_dir / "history.png"

    visualizer.plot_training_history(

        history,

        save_path=output,

    )

    assert output.stat().st_size > 0


# ============================================================
# Error Handling
# ============================================================

def test_prediction_length_mismatch(
    visualizer,
    temp_output_dir,
):

    actual = np.array([1, 2, 3])

    predicted = np.array([1, 2])

    with pytest.raises(ValueError):

        visualizer.plot_predictions(

            actual,

            predicted,

            save_path=temp_output_dir / "invalid.png",

        )


def test_empty_history(
    visualizer,
    temp_output_dir,
):

    with pytest.raises(ValueError):

        visualizer.plot_training_history(

            {},

            save_path=temp_output_dir / "empty.png",

        )


# ============================================================
# Multiple Figure Generation
# ============================================================

def test_multiple_plots(
    visualizer,
    temp_output_dir,
):

    history = {

        "loss": [1.0, 0.8, 0.6]

    }

    for index in range(3):

        output = temp_output_dir / f"plot_{index}.png"

        visualizer.plot_training_history(

            history,

            save_path=output,

        )

        assert output.exists()


# ============================================================
# Figure Format
# ============================================================

def test_png_extension(
    visualizer,
    temp_output_dir,
):

    history = {

        "loss": [1.0, 0.5]

    }

    output = temp_output_dir / "figure.png"

    visualizer.plot_training_history(

        history,

        save_path=output,

    )

    assert output.suffix == ".png"


# ============================================================
# Integration
# ============================================================

def test_complete_visualization_pipeline(
    visualizer,
    temp_output_dir,
):

    history = {

        "loss": [1.0, 0.8, 0.5],

        "val_loss": [1.2, 0.9, 0.7],

    }

    predictions = np.array([1, 2, 3])

    targets = np.array([1.1, 2.1, 2.9])

    visualizer.plot_training_history(

        history,

        save_path=temp_output_dir / "history.png",

    )

    visualizer.plot_predictions(

        targets,

        predictions,

        save_path=temp_output_dir / "predictions.png",

    )

    assert (

        temp_output_dir / "history.png"

    ).exists()

    assert (

        temp_output_dir / "predictions.png"

    ).exists()