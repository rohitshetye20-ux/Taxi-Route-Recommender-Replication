"""
Taxi Route Recommender
======================

Core source package for the Taxi Route Recommender project.

This package provides reusable modules for data loading,
preprocessing, graph construction, model interaction,
evaluation, visualization, and inference.

The implementation is designed to support the reproduction
of the research paper:

    "A Cost-Effective Sequential Route Recommender System
     for Taxi Drivers"

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

__version__ = "1.0.0"
__author__ = "Rohit"
__license__ = "MIT"

# Public modules

__all__ = [
    "analysis",
    "data_loader",
    "evaluation",
    "graph_builder",
    "inference",
    "model_interface",
    "preprocessing",
    "utils",
    "visualization",
]