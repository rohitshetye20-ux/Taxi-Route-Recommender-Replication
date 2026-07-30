"""
build_graph.py
==============

Build graph representations from processed transportation datasets.

This script loads a processed dataset, constructs a transportation
graph, generates graph statistics, creates an adjacency matrix,
and exports graph artifacts for downstream machine learning tasks.

Usage
-----
python scripts/build_graph.py

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# ============================================================
# Project Root
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT))

# ============================================================
# Imports
# ============================================================

from src.data_loader import DataLoader
from src.graph_builder import GraphBuilder
from src.utils import (
    Timer,
    ensure_directory,
    get_logger,
)

# ============================================================
# Logger
# ============================================================

logger = get_logger(__name__)

# ============================================================
# Default Locations
# ============================================================

PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

GRAPH_DIR = PROJECT_ROOT / "data" / "graph"

DEFAULT_INPUT = PROCESSED_DATA_DIR / "taxi_routes_processed.csv"

DEFAULT_GRAPH = GRAPH_DIR / "transportation_network.graphml"

DEFAULT_ADJACENCY = GRAPH_DIR / "adjacency_matrix.csv"

DEFAULT_STATS = GRAPH_DIR / "graph_statistics.csv"

# ============================================================
# Graph Pipeline
# ============================================================


def build_transportation_graph(
    input_file: Path,
    graph_output: Path,
    adjacency_output: Path,
    statistics_output: Path,
    source_column: str,
    target_column: str,
    weight_column: str | None = None,
) -> None:
    """
    Execute the graph construction pipeline.
    """

    ensure_directory(graph_output.parent)

    loader = DataLoader()

    builder = GraphBuilder()

    logger.info("Loading processed dataset...")

    dataframe = loader.load_csv(input_file)

    logger.info(
        "Dataset loaded successfully (%d rows × %d columns).",
        len(dataframe),
        len(dataframe.columns),
    )

    logger.info("Building transportation graph...")

    graph = builder.build_graph(
        dataframe=dataframe,
        source_column=source_column,
        target_column=target_column,
        weight_column=weight_column,
    )

    logger.info(
        "Graph created with %d nodes and %d edges.",
        graph.number_of_nodes(),
        graph.number_of_edges(),
    )

    # --------------------------------------------------------
    # Save GraphML
    # --------------------------------------------------------

    builder.save_graphml(graph_output)

    logger.info("GraphML exported.")

    # --------------------------------------------------------
    # Save Adjacency Matrix
    # --------------------------------------------------------

    adjacency = builder.adjacency_matrix()

    pd.DataFrame(adjacency).to_csv(
        adjacency_output,
        index=False,
    )

    logger.info("Adjacency matrix exported.")

    # --------------------------------------------------------
    # Save Statistics
    # --------------------------------------------------------

    statistics = builder.graph_statistics()

    pd.DataFrame(
        [statistics]
    ).to_csv(
        statistics_output,
        index=False,
    )

    logger.info("Graph statistics exported.")

    logger.info("Graph construction completed successfully.")


# ============================================================
# CLI
# ============================================================

def parse_arguments():

    parser = argparse.ArgumentParser(
        description="Transportation Graph Builder"
    )

    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help="Processed CSV dataset.",
    )

    parser.add_argument(
        "--graph-output",
        type=Path,
        default=DEFAULT_GRAPH,
        help="Output GraphML file.",
    )

    parser.add_argument(
        "--adjacency-output",
        type=Path,
        default=DEFAULT_ADJACENCY,
        help="Adjacency matrix CSV.",
    )

    parser.add_argument(
        "--statistics-output",
        type=Path,
        default=DEFAULT_STATS,
        help="Graph statistics CSV.",
    )

    parser.add_argument(
        "--source-column",
        default="source",
        help="Source node column.",
    )

    parser.add_argument(
        "--target-column",
        default="target",
        help="Target node column.",
    )

    parser.add_argument(
        "--weight-column",
        default=None,
        help="Optional edge weight column.",
    )

    return parser.parse_args()


# ============================================================
# Main
# ============================================================

def main():

    args = parse_arguments()

    with Timer("Graph Construction"):

        build_transportation_graph(
            input_file=args.input,
            graph_output=args.graph_output,
            adjacency_output=args.adjacency_output,
            statistics_output=args.statistics_output,
            source_column=args.source_column,
            target_column=args.target_column,
            weight_column=args.weight_column,
        )


if __name__ == "__main__":

    main()