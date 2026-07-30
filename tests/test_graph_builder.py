"""
test_graph_builder.py
=====================

Unit tests for src.graph_builder.

This module verifies graph construction, graph statistics,
adjacency matrix generation, GraphML export/import, and
error handling.

Run
---
pytest tests/test_graph_builder.py

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

from src.graph_builder import GraphBuilder


# ============================================================
# Fixture
# ============================================================

@pytest.fixture
def builder():

    return GraphBuilder()


# ============================================================
# Graph Construction
# ============================================================

def test_build_graph(builder, sample_graph_dataframe):

    graph = builder.build_graph(

        dataframe=sample_graph_dataframe,

        source_column="source",

        target_column="target",

        weight_column="weight",

    )

    assert isinstance(graph, nx.Graph)


def test_graph_node_count(builder, sample_graph_dataframe):

    graph = builder.build_graph(

        dataframe=sample_graph_dataframe,

        source_column="source",

        target_column="target",

        weight_column="weight",

    )

    assert graph.number_of_nodes() == 4


def test_graph_edge_count(builder, sample_graph_dataframe):

    graph = builder.build_graph(

        dataframe=sample_graph_dataframe,

        source_column="source",

        target_column="target",

        weight_column="weight",

    )

    assert graph.number_of_edges() == 4


# ============================================================
# Edge Weights
# ============================================================

def test_edge_weights(builder, sample_graph_dataframe):

    graph = builder.build_graph(

        dataframe=sample_graph_dataframe,

        source_column="source",

        target_column="target",

        weight_column="weight",

    )

    assert graph["A"]["B"]["weight"] == 5


# ============================================================
# Adjacency Matrix
# ============================================================

def test_adjacency_matrix(builder, sample_graph_dataframe):

    builder.build_graph(

        dataframe=sample_graph_dataframe,

        source_column="source",

        target_column="target",

        weight_column="weight",

    )

    matrix = builder.adjacency_matrix()

    assert isinstance(matrix, np.ndarray)


def test_adjacency_shape(builder, sample_graph_dataframe):

    builder.build_graph(

        dataframe=sample_graph_dataframe,

        source_column="source",

        target_column="target",

        weight_column="weight",

    )

    matrix = builder.adjacency_matrix()

    assert matrix.shape == (4, 4)


# ============================================================
# Graph Statistics
# ============================================================

def test_graph_statistics(builder, sample_graph_dataframe):

    builder.build_graph(

        dataframe=sample_graph_dataframe,

        source_column="source",

        target_column="target",

        weight_column="weight",

    )

    stats = builder.graph_statistics()

    assert isinstance(stats, dict)


def test_statistics_keys(builder, sample_graph_dataframe):

    builder.build_graph(

        dataframe=sample_graph_dataframe,

        source_column="source",

        target_column="target",

        weight_column="weight",

    )

    stats = builder.graph_statistics()

    expected = {

        "nodes",

        "edges",

        "density",

        "average_degree",

    }

    assert expected.issubset(stats.keys())


# ============================================================
# GraphML
# ============================================================

def test_save_graphml(builder, sample_graph_dataframe, tmp_path):

    builder.build_graph(

        dataframe=sample_graph_dataframe,

        source_column="source",

        target_column="target",

        weight_column="weight",

    )

    file = tmp_path / "graph.graphml"

    builder.save_graphml(file)

    assert file.exists()


def test_load_saved_graph(tmp_path):

    graph = nx.Graph()

    graph.add_edge("A", "B")

    file = tmp_path / "graph.graphml"

    nx.write_graphml(graph, file)

    loaded = nx.read_graphml(file)

    assert loaded.number_of_edges() == 1


# ============================================================
# Empty Graph
# ============================================================

def test_empty_dataframe(builder):

    dataframe = pd.DataFrame(

        columns=[

            "source",

            "target",

            "weight",

        ]

    )

    graph = builder.build_graph(

        dataframe=dataframe,

        source_column="source",

        target_column="target",

        weight_column="weight",

    )

    assert graph.number_of_nodes() == 0


# ============================================================
# Invalid Columns
# ============================================================

def test_invalid_source_column(builder, sample_graph_dataframe):

    with pytest.raises(KeyError):

        builder.build_graph(

            dataframe=sample_graph_dataframe,

            source_column="invalid",

            target_column="target",

        )


# ============================================================
# Graph Connectivity
# ============================================================

def test_graph_connected(builder, sample_graph_dataframe):

    graph = builder.build_graph(

        dataframe=sample_graph_dataframe,

        source_column="source",

        target_column="target",

        weight_column="weight",

    )

    assert nx.is_connected(graph)


# ============================================================
# Performance
# ============================================================

def test_large_graph(builder):

    dataframe = pd.DataFrame(

        {

            "source": range(500),

            "target": range(1, 501),

            "weight": 1,

        }

    )

    graph = builder.build_graph(

        dataframe=dataframe,

        source_column="source",

        target_column="target",

        weight_column="weight",

    )

    assert graph.number_of_edges() == 500


# ============================================================
# Duplicate Edges
# ============================================================

def test_duplicate_edges(builder):

    dataframe = pd.DataFrame(

        {

            "source": ["A", "A"],

            "target": ["B", "B"],

            "weight": [5, 5],

        }

    )

    graph = builder.build_graph(

        dataframe=dataframe,

        source_column="source",

        target_column="target",

        weight_column="weight",

    )

    assert graph.number_of_edges() == 1