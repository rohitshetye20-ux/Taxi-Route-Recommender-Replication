"""
conftest.py
===========

Shared pytest fixtures for the Taxi Route Recommender project.

This module provides reusable fixtures that are shared across
all test modules.

Fixtures
--------
- sample_dataframe
- sample_graph_dataframe
- sample_prediction_dataframe
- sample_graph
- sample_predictions
- sample_targets
- temp_output_dir
- dummy_model

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

from pathlib import Path

import networkx as nx
import numpy as np
import pandas as pd
import pytest


# ============================================================
# Sample Tabular Dataset
# ============================================================

@pytest.fixture
def sample_dataframe():
    """
    Sample dataset for preprocessing tests.
    """

    return pd.DataFrame(
        {
            "Trip_ID": [1, 2, 3, 4],

            "Pickup": [
                "Zone_A",
                "Zone_B",
                "Zone_C",
                "Zone_D",
            ],

            "Dropoff": [
                "Zone_B",
                "Zone_C",
                "Zone_D",
                "Zone_E",
            ],

            "Fare": [
                120,
                150,
                210,
                175,
            ],

            "Distance": [
                3.5,
                4.2,
                6.8,
                5.4,
            ],
        }
    )


# ============================================================
# Graph Dataset
# ============================================================

@pytest.fixture
def sample_graph_dataframe():
    """
    Dataset for graph construction.
    """

    return pd.DataFrame(
        {
            "source": [
                "A",
                "A",
                "B",
                "C",
            ],

            "target": [
                "B",
                "C",
                "D",
                "D",
            ],

            "weight": [
                5,
                7,
                2,
                9,
            ],
        }
    )


# ============================================================
# Prediction Dataset
# ============================================================

@pytest.fixture
def sample_prediction_dataframe():
    """
    Dataset containing predictions.
    """

    return pd.DataFrame(
        {
            "target": [
                10,
                15,
                18,
                22,
                30,
            ],

            "prediction": [
                11,
                14,
                17,
                21,
                29,
            ],
        }
    )


# ============================================================
# Sample NetworkX Graph
# ============================================================

@pytest.fixture
def sample_graph():
    """
    Create a simple graph.
    """

    graph = nx.Graph()

    graph.add_edge("A", "B", weight=5)

    graph.add_edge("B", "C", weight=3)

    graph.add_edge("C", "D", weight=8)

    return graph


# ============================================================
# Regression Targets
# ============================================================

@pytest.fixture
def sample_targets():
    """
    Ground-truth values.
    """

    return np.array(
        [
            12,
            15,
            19,
            23,
            31,
        ]
    )


@pytest.fixture
def sample_predictions():
    """
    Model predictions.
    """

    return np.array(
        [
            11,
            14,
            18,
            22,
            30,
        ]
    )


# ============================================================
# Temporary Output Directory
# ============================================================

@pytest.fixture
def temp_output_dir(tmp_path):
    """
    Temporary directory for exported files.
    """

    output = tmp_path / "output"

    output.mkdir()

    return output


# ============================================================
# Dummy Model
# ============================================================

class DummyModel:
    """
    Minimal model implementation used
    for ModelManager tests.
    """

    def build(self):
        return None

    def train(self, train_data, validation_data=None):

        return {
            "loss": [
                1.0,
                0.7,
                0.4,
            ]
        }

    def predict(self, data):

        return np.ones(len(data))

    def evaluate(self, data):

        return {
            "accuracy": 0.95,
        }

    def save(self, filepath):

        Path(filepath).touch()

    def load(self, filepath):

        return None


@pytest.fixture
def dummy_model():
    """
    Return reusable dummy model.
    """

    return DummyModel()