"""
test_model_interface.py
=======================

Unit tests for src.model_interface.

This module verifies the behavior of the ModelManager
abstraction layer.

Run
---
pytest tests/test_model_interface.py

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import pytest

from src.model_interface import ModelManager


# ============================================================
# Initialization
# ============================================================

def test_model_manager_initialization(dummy_model):

    manager = ModelManager(dummy_model)

    assert manager.model is dummy_model


# ============================================================
# Build
# ============================================================

def test_build_model(dummy_model):

    manager = ModelManager(dummy_model)

    manager.build_model()

    assert manager.model is not None


# ============================================================
# Training
# ============================================================

def test_train_model(dummy_model, sample_dataframe):

    manager = ModelManager(dummy_model)

    history = manager.train_model(sample_dataframe)

    assert isinstance(history, dict)

    assert "loss" in history


def test_training_history_length(dummy_model, sample_dataframe):

    manager = ModelManager(dummy_model)

    history = manager.train_model(sample_dataframe)

    assert len(history["loss"]) == 3


# ============================================================
# Prediction
# ============================================================

def test_prediction(dummy_model, sample_dataframe):

    manager = ModelManager(dummy_model)

    predictions = manager.predict(sample_dataframe)

    assert len(predictions) == len(sample_dataframe)


def test_prediction_type(dummy_model, sample_dataframe):

    manager = ModelManager(dummy_model)

    predictions = manager.predict(sample_dataframe)

    assert hasattr(predictions, "__len__")


# ============================================================
# Evaluation
# ============================================================

def test_evaluate_model(dummy_model, sample_dataframe):

    manager = ModelManager(dummy_model)

    metrics = manager.evaluate_model(sample_dataframe)

    assert isinstance(metrics, dict)

    assert "accuracy" in metrics


# ============================================================
# Save / Load
# ============================================================

def test_save_model(dummy_model, tmp_path):

    manager = ModelManager(dummy_model)

    model_file = tmp_path / "model.keras"

    manager.save_model(model_file)

    assert model_file.exists()


def test_load_model(dummy_model, tmp_path):

    manager = ModelManager(dummy_model)

    model_file = tmp_path / "model.keras"

    manager.save_model(model_file)

    manager.load_model(model_file)

    assert model_file.exists()


# ============================================================
# Multiple Predictions
# ============================================================

def test_multiple_prediction_calls(dummy_model, sample_dataframe):

    manager = ModelManager(dummy_model)

    first = manager.predict(sample_dataframe)

    second = manager.predict(sample_dataframe)

    assert len(first) == len(second)


# ============================================================
# Error Handling
# ============================================================

def test_load_missing_model(dummy_model, tmp_path):

    manager = ModelManager(dummy_model)

    missing = tmp_path / "missing.keras"

    with pytest.raises(FileNotFoundError):

        manager.load_model(missing)


def test_invalid_model_initialization():

    with pytest.raises(TypeError):

        ModelManager(None)


# ============================================================
# Integration
# ============================================================

def test_complete_model_pipeline(dummy_model, sample_dataframe, tmp_path):

    manager = ModelManager(dummy_model)

    manager.build_model()

    history = manager.train_model(sample_dataframe)

    predictions = manager.predict(sample_dataframe)

    metrics = manager.evaluate_model(sample_dataframe)

    model_file = tmp_path / "pipeline.keras"

    manager.save_model(model_file)

    manager.load_model(model_file)

    assert model_file.exists()

    assert len(predictions) == len(sample_dataframe)

    assert "loss" in history

    assert "accuracy" in metrics