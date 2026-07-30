"""
config.py

Global configuration for the Report Builder Framework.
"""

from pathlib import Path

# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CHAPTER_DIR = PROJECT_ROOT / "chapters"

FIGURE_DIR = PROJECT_ROOT / "figures"

OUTPUT_DIR = PROJECT_ROOT / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ============================================================
# REPORT METADATA
# ============================================================

REPORT_TITLE = "A Cost-Effective Sequential Route Recommender System for Taxi Drivers"

AUTHOR = "Rohit"

VERSION = "2.0"

DOCX_NAME = "Final_Report.docx"

PDF_NAME = "Final_Report.pdf"

PPT_NAME = "Final_Presentation.pptx"

# ============================================================
# WORD SETTINGS
# ============================================================

TABLE_STYLE = "Table Grid"

DEFAULT_IMAGE_WIDTH = 6.5

CAPTION_PREFIX = "Figure"

# ============================================================
# CHAPTER ORDER
# ============================================================

CHAPTERS = [

    "01_Executive_Summary.md",

    "02_Research_Background.md",

    "03_Methodology.md",

    "04_System_Implementation.md",

    "05_Experimental_Results.md",

    "06_Discussion.md",

    "07_Conclusion.md",

    "08_References.md",

    "09_Appendices.md",

]

# ============================================================
# FIGURE REGISTRY
#
# Left Side  = Placeholder detected in Markdown
# Right Side = Actual filename inside /figures
# ============================================================

FIGURE_MAP = {

    # ========================================================
    # Chapter 3
    # ========================================================

    "Overall Project Workflow":
        "Overall Project Workflow.png",

    # ========================================================
    # Chapter 4
    # ========================================================

    "Repository Architecture":
        "Repository Architecture.png",

    "Repository Architecture Diagram":
        "Repository Architecture.png",

    "Module Dependency Graph":
        "Model Dependency Graph.png",

    "Model Dependency Graph":
        "Model Dependency Graph.png",

    "Model Dependency Graph Diagram":
        "Model Dependency Graph.png",

    "Data Pipeline":
        "Data Pipeline.png",

    "Data Pipeline Diagram":
        "Data Pipeline.png",

    "Model Architecture":
        "Model Architecture.png",

    "Model Architecture Diagram":
        "Model Architecture.png",

    "Tensor Shape Flow":
        "Tensor_Shapes.png",

    "Tensor Shapes":
        "Tensor_Shapes.png",

    "Tensor Shapes Diagram":
        "Tensor_Shapes.png",

    "Training Pipeline":
        "Training Pipeline.png",

    "Training Pipeline Diagram":
        "Training Pipeline.png",

    "Inference Pipeline":
        "Inference Pipeline.png",

    "Inference Pipeline Diagram":
        "Inference Pipeline.png",

    # ========================================================
    # Chapter 5
    # ========================================================

    "Training Loss":
        "train_loss.png",

    "Training Loss Curve":
        "train_loss.png",

    "Validation Loss":
        "Validation_loss.png",

    "Validation Loss Curve":
        "Validation_loss.png",

    "Prediction vs Label":
        "Prediction_vs_label.png",

    "Prediction vs Labels":
        "Prediction_vs_label.png",

    "Prediction vs Label Plot":
        "Prediction_vs_label.png",

    "Experiment Dashboard":
        "experiment_dashboard.png",

    "Experiment Dashboard Diagram":
        "experiment_dashboard.png",

    "Experiment Timeline":
        "Experiment_Timeline.png",

    "Experiment Timeline Diagram":
        "Experiment_Timeline.png",

}

# ============================================================
# TABLE SETTINGS
# ============================================================

TABLE_CAPTION_PREFIX = "Table"

# ============================================================
# EXPORT SETTINGS
# ============================================================

GENERATE_DOCX = True

GENERATE_PDF = False

GENERATE_PPT = False

# ============================================================
# DEBUG SETTINGS
# ============================================================

DEBUG = False

