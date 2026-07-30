"""
graph_builder.py
================

Graph construction utilities for the Taxi Route Recommender project.

This module converts tabular transportation datasets into graph
representations suitable for Graph Neural Networks (GCNs).

Features
--------
- Graph creation from edge lists
- Node attribute assignment
- Adjacency matrix generation
- Degree statistics
- Connectivity validation
- Graph visualization support

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Dict, List, Optional

import networkx as nx
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

if not logger.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


class GraphBuilder:
    """
    Build graph representations from transportation datasets.
    """

    def __init__(self) -> None:
        self.graph = nx.Graph()

        logger.info("GraphBuilder initialized.")

    # --------------------------------------------------------
    # Build Graph
    # --------------------------------------------------------

    def build_graph(
        self,
        dataframe: pd.DataFrame,
        source_column: str,
        target_column: str,
        weight_column: Optional[str] = None,
    ) -> nx.Graph:
        """
        Build a graph from an edge list.

        Parameters
        ----------
        dataframe : pandas.DataFrame
            Edge list dataset.

        source_column : str
            Source node column.

        target_column : str
            Destination node column.

        weight_column : str, optional
            Edge weight column.

        Returns
        -------
        networkx.Graph
        """

        self.graph.clear()

        for _, row in dataframe.iterrows():

            source = row[source_column]
            target = row[target_column]

            if weight_column:

                weight = row[weight_column]

                self.graph.add_edge(
                    source,
                    target,
                    weight=weight,
                )

            else:

                self.graph.add_edge(
                    source,
                    target,
                )

        logger.info(
            "Graph created with %d nodes and %d edges.",
            self.graph.number_of_nodes(),
            self.graph.number_of_edges(),
        )

        return self.graph

    # --------------------------------------------------------
    # Add Node Features
    # --------------------------------------------------------

    def add_node_attributes(
        self,
        dataframe: pd.DataFrame,
        node_column: str,
    ) -> None:
        """
        Attach node attributes from a dataframe.
        """

        attributes = dataframe.set_index(node_column).to_dict("index")

        nx.set_node_attributes(
            self.graph,
            attributes,
        )

        logger.info(
            "Node attributes assigned."
        )

    # --------------------------------------------------------
    # Graph Statistics
    # --------------------------------------------------------

    def graph_statistics(self) -> Dict[str, float]:
        """
        Return basic graph statistics.
        """

        stats = {

            "nodes": self.graph.number_of_nodes(),

            "edges": self.graph.number_of_edges(),

            "density": nx.density(self.graph),

            "average_degree":
                (
                    sum(
                        dict(
                            self.graph.degree()
                        ).values()
                    )
                    /
                    self.graph.number_of_nodes()
                )
                if self.graph.number_of_nodes()
                else 0,

            "connected":
                nx.is_connected(self.graph)
                if self.graph.number_of_nodes()
                else False,
        }

        logger.info("Graph statistics generated.")

        return stats

    # --------------------------------------------------------
    # Adjacency Matrix
    # --------------------------------------------------------

    def adjacency_matrix(self) -> np.ndarray:
        """
        Return adjacency matrix.
        """

        matrix = nx.to_numpy_array(self.graph)

        logger.info(
            "Adjacency matrix created: %s",
            matrix.shape,
        )

        return matrix

    # --------------------------------------------------------
    # Degree Distribution
    # --------------------------------------------------------

    def degree_dataframe(self) -> pd.DataFrame:
        """
        Return node degree information.
        """

        degrees = dict(self.graph.degree())

        dataframe = pd.DataFrame({

            "Node": list(degrees.keys()),

            "Degree": list(degrees.values()),

        })

        return dataframe.sort_values(
            "Degree",
            ascending=False,
        )

    # --------------------------------------------------------
    # Shortest Path
    # --------------------------------------------------------

    def shortest_path(
        self,
        source,
        target,
    ) -> List:
        """
        Compute shortest path between two nodes.
        """

        return nx.shortest_path(
            self.graph,
            source,
            target,
        )

    # --------------------------------------------------------
    # Connected Components
    # --------------------------------------------------------

    def connected_components(self) -> List[set]:
        """
        Return graph connected components.
        """

        return list(
            nx.connected_components(self.graph)
        )

    # --------------------------------------------------------
    # Export Graph
    # --------------------------------------------------------

    def save_graphml(
        self,
        filepath: str | Path,
    ) -> None:
        """
        Save graph as GraphML.
        """

        nx.write_graphml(
            self.graph,
            filepath,
        )

        logger.info(
            "Graph exported to %s",
            filepath,
        )

    # --------------------------------------------------------
    # Load GraphML
    # --------------------------------------------------------

    def load_graphml(
        self,
        filepath: str | Path,
    ) -> nx.Graph:
        """
        Load GraphML file.
        """

        self.graph = nx.read_graphml(filepath)

        logger.info(
            "Graph loaded from %s",
            filepath,
        )

        return self.graph

    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    def summary(self) -> None:
        """
        Print graph summary.
        """

        stats = self.graph_statistics()

        print("\nGraph Summary")
        print("-" * 60)

        for key, value in stats.items():
            print(f"{key:<20}: {value}")

        print("-" * 60)