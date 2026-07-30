"""
test_data_loader.py
===================

Unit tests for src.data_loader.

This module verifies CSV loading, GraphML loading,
basic validation, and error handling.

Run
---
pytest tests/test_data_loader.py

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
import pandas as pd
import pytest

from src.data_loader import DataLoader


# ============================================================
# CSV Loading
# ============================================================

def test_load_csv_success(tmp_path):

    file = tmp_path / "sample.csv"

    dataframe = pd.DataFrame(
        {
            "A": [1, 2, 3],
            "B": [4, 5, 6],
        }
    )

    dataframe.to_csv(file, index=False)

    loader = DataLoader()

    result = loader.load_csv(file)

    assert isinstance(result, pd.DataFrame)
    assert result.shape == (3, 2)


def test_load_csv_column_names(tmp_path):

    file = tmp_path / "columns.csv"

    dataframe = pd.DataFrame(
        {
            "Pickup": [1],
            "Dropoff": [2],
            "Fare": [120],
        }
    )

    dataframe.to_csv(file, index=False)

    loader = DataLoader()

    result = loader.load_csv(file)

    assert list(result.columns) == [
        "Pickup",
        "Dropoff",
        "Fare",
    ]


def test_load_csv_missing_file(tmp_path):

    loader = DataLoader()

    missing = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):

        loader.load_csv(missing)


# ============================================================
# GraphML Loading
# ============================================================

def test_load_graphml_success(tmp_path):

    graph = nx.Graph()

    graph.add_edge("A", "B")

    file = tmp_path / "graph.graphml"

    nx.write_graphml(graph, file)

    loader = DataLoader()

    loaded = loader.load_graphml(file)

    assert loaded.number_of_nodes() == 2
    assert loaded.number_of_edges() == 1


def test_load_graphml_missing_file(tmp_path):

    loader = DataLoader()

    file = tmp_path / "missing.graphml"

    with pytest.raises(FileNotFoundError):

        loader.load_graphml(file)


# ============================================================
# Data Validation
# ============================================================

def test_dataframe_row_count(sample_dataframe):

    assert len(sample_dataframe) == 4


def test_dataframe_column_count(sample_dataframe):

    assert sample_dataframe.shape[1] == 5


def test_dataframe_has_expected_columns(sample_dataframe):

    expected = {
        "Trip_ID",
        "Pickup",
        "Dropoff",
        "Fare",
        "Distance",
    }

    assert set(sample_dataframe.columns) == expected


# ============================================================
# Empty Dataset
# ============================================================

def test_empty_csv(tmp_path):

    file = tmp_path / "empty.csv"

    pd.DataFrame().to_csv(file, index=False)

    loader = DataLoader()

    result = loader.load_csv(file)

    assert result.empty


# ============================================================
# Data Types
# ============================================================

def test_numeric_columns(sample_dataframe):

    assert pd.api.types.is_numeric_dtype(
        sample_dataframe["Fare"]
    )

    assert pd.api.types.is_numeric_dtype(
        sample_dataframe["Distance"]
    )


# ============================================================
# Duplicate Loading
# ============================================================

def test_multiple_csv_loads(tmp_path):

    file = tmp_path / "sample.csv"

    dataframe = pd.DataFrame(
        {
            "A": [1, 2],
            "B": [3, 4],
        }
    )

    dataframe.to_csv(file, index=False)

    loader = DataLoader()

    first = loader.load_csv(file)

    second = loader.load_csv(file)

    pd.testing.assert_frame_equal(
        first,
        second,
    )


# ============================================================
# Path Objects
# ============================================================

def test_load_csv_accepts_path_object(tmp_path):

    file = Path(tmp_path) / "sample.csv"

    pd.DataFrame(
        {
            "X": [1],
            "Y": [2],
        }
    ).to_csv(file, index=False)

    loader = DataLoader()

    result = loader.load_csv(file)

    assert isinstance(result, pd.DataFrame)