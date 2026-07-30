"""
scripts
=======

Command-line execution package for the
Taxi Route Recommender project.

This package contains executable scripts that orchestrate
the end-to-end machine learning and research workflow,
including data preprocessing, graph construction, model
training, evaluation, inference, report generation, and
presentation creation.

Scripts in this package are intentionally lightweight.
They primarily coordinate components implemented in the
`src` package and avoid containing business logic.

Modules
-------
preprocess
    Execute the data preprocessing pipeline.

build_graph
    Build graph representations from processed datasets.

train
    Train the GCN-LSTM model.

evaluate
    Evaluate trained models.

predict
    Perform inference using trained models.

generate_figures
    Generate publication-quality figures.

build_report
    Build the research report.

build_presentation
    Generate the PowerPoint presentation.

run_pipeline
    Execute the complete project workflow.

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

__version__ = "1.0.0"

__author__ = "Rohit Shetye"

__license__ = "MIT"

__all__ = [
    "preprocess",
    "build_graph",
    "train",
    "evaluate",
    "predict",
    "generate_figures",
    "build_report",
    "build_presentation",
    "run_pipeline",
]