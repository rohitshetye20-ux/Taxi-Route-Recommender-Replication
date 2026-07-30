"""
build_presentation.py
=====================

Build the complete PowerPoint presentation using the
Presentation Builder framework.

This script compiles all Markdown presentation slides,
figures, and layouts into a professional PowerPoint deck.

Usage
-----
python scripts/build_presentation.py

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

# ============================================================
# Project Root
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT))

# ============================================================
# Imports
# ============================================================

from src.utils import (
    Timer,
    get_logger,
)

from presentation_builder.builder import PresentationBuilder

logger = get_logger(__name__)

# ============================================================
# Default Paths
# ============================================================

OUTPUT_DIR = PROJECT_ROOT / "output"

DEFAULT_OUTPUT = (
    OUTPUT_DIR /
    "Taxi_Route_Recommender_Presentation.pptx"
)

# ============================================================
# Presentation Pipeline
# ============================================================


def build_presentation(
    output_file: Path,
):
    """
    Generate the complete PowerPoint presentation.
    """

    logger.info(
        "Initializing Presentation Builder..."
    )

    builder = PresentationBuilder()

    logger.info(
        "Building presentation..."
    )

    builder.build()

    logger.info(
        "Exporting PowerPoint..."
    )

    builder.export_pptx(
        output_file,
    )

    logger.info(
        "Presentation generated successfully."
    )


# ============================================================
# CLI
# ============================================================


def parse_arguments():

    parser = argparse.ArgumentParser(

        description="Presentation Builder",

    )

    parser.add_argument(

        "--output",

        type=Path,

        default=DEFAULT_OUTPUT,

        help="Output PowerPoint filename.",

    )

    return parser.parse_args()


# ============================================================
# Main
# ============================================================


def main():

    args = parse_arguments()

    with Timer(

        "Presentation Generation",

    ):

        build_presentation(

            output_file=args.output,

        )


if __name__ == "__main__":

    main()