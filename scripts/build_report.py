"""
build_report.py
===============

Build the complete research report using the Report Builder
framework.

This script compiles all Markdown chapters into a single
professional PDF report.

Usage
-----
python scripts/build_report.py

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

from report_builder.builder import ReportBuilder

logger = get_logger(__name__)

# ============================================================
# Default Directories
# ============================================================

REPORT_DIR = PROJECT_ROOT / "report_builder"

OUTPUT_DIR = PROJECT_ROOT / "output"

DEFAULT_OUTPUT = OUTPUT_DIR / "Taxi_Route_Recommender_Report.pdf"

# ============================================================
# Report Pipeline
# ============================================================


def build_report(
    output_file: Path,
):
    """
    Generate the final research report.
    """

    logger.info(
        "Initializing Report Builder..."
    )

    builder = ReportBuilder()

    logger.info(
        "Building report..."
    )

    builder.build()

    logger.info(
        "Exporting report..."
    )

    builder.export_pdf(
        output_file,
    )

    logger.info(
        "Research report successfully generated."
    )


# ============================================================
# CLI
# ============================================================


def parse_arguments():

    parser = argparse.ArgumentParser(

        description="Research Report Builder",

    )

    parser.add_argument(

        "--output",

        type=Path,

        default=DEFAULT_OUTPUT,

        help="Output PDF filename.",

    )

    return parser.parse_args()


# ============================================================
# Main
# ============================================================


def main():

    args = parse_arguments()

    with Timer(

        "Research Report Generation",

    ):

        build_report(

            output_file=args.output,

        )


if __name__ == "__main__":

    main()