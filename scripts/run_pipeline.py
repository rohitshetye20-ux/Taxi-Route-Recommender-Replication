"""
run_pipeline.py
===============

Execute the complete Taxi Route Recommender research pipeline.

This script orchestrates the full workflow, including:

1. Data preprocessing
2. Graph construction
3. Model training
4. Model evaluation
5. Prediction
6. Figure generation
7. Research report generation
8. Presentation generation

Usage
-----
python scripts/run_pipeline.py

Author:
    Rohit Shetye

Version:
    1.0.0

License:
    MIT
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

sys.path.append(str(PROJECT_ROOT))

from src.utils import get_logger

logger = get_logger(__name__)

# ============================================================
# Pipeline Definition
# ============================================================

PIPELINE = [

    ("Data Preprocessing",
     "scripts/preprocess.py"),

    ("Graph Construction",
     "scripts/build_graph.py"),

    ("Model Training",
     "scripts/train.py"),

    ("Model Evaluation",
     "scripts/evaluate.py"),

    ("Prediction",
     "scripts/predict.py"),

    ("Figure Generation",
     "scripts/generate_figures.py"),

    ("Report Generation",
     "scripts/build_report.py"),

    ("Presentation Generation",
     "scripts/build_presentation.py"),
]

# ============================================================
# Execute Script
# ============================================================


def execute(script_name, script_path):

    logger.info("=" * 70)

    logger.info("Starting: %s", script_name)

    logger.info("=" * 70)

    start = time.perf_counter()

    result = subprocess.run(

        [sys.executable, script_path],

        cwd=PROJECT_ROOT,

    )

    elapsed = time.perf_counter() - start

    if result.returncode != 0:

        logger.error(
            "%s FAILED",
            script_name,
        )

        return False

    logger.info(

        "%s completed successfully (%.2f seconds)",

        script_name,

        elapsed,

    )

    return True


# ============================================================
# Pipeline Runner
# ============================================================


def run_pipeline(skip_training=False,
                 skip_report=False,
                 skip_presentation=False):

    completed = []

    failed = []

    total_start = time.perf_counter()

    for name, script in PIPELINE:

        if skip_training and name == "Model Training":

            logger.info("Skipping Model Training")

            continue

        if skip_report and name == "Report Generation":

            logger.info("Skipping Report Generation")

            continue

        if skip_presentation and name == "Presentation Generation":

            logger.info("Skipping Presentation Generation")

            continue

        success = execute(name, script)

        if success:

            completed.append(name)

        else:

            failed.append(name)

            logger.error(

                "Pipeline stopped because '%s' failed.",

                name,

            )

            break

    total_time = time.perf_counter() - total_start

    print()

    print("=" * 80)

    print("PIPELINE SUMMARY")

    print("=" * 80)

    print(f"Completed Steps : {len(completed)}")

    print(f"Failed Steps    : {len(failed)}")

    print(f"Execution Time  : {total_time:.2f} seconds")

    print()

    if completed:

        print("Completed")

        for step in completed:

            print(f"  ✓ {step}")

        print()

    if failed:

        print("Failed")

        for step in failed:

            print(f"  ✗ {step}")

    else:

        print("Pipeline executed successfully.")

    print("=" * 80)


# ============================================================
# CLI
# ============================================================


def parse_arguments():

    parser = argparse.ArgumentParser(

        description="Taxi Route Recommender Pipeline",

    )

    parser.add_argument(

        "--skip-training",

        action="store_true",

        help="Skip model training.",

    )

    parser.add_argument(

        "--skip-report",

        action="store_true",

        help="Skip PDF report generation.",

    )

    parser.add_argument(

        "--skip-presentation",

        action="store_true",

        help="Skip PowerPoint generation.",

    )

    return parser.parse_args()


# ============================================================
# Main
# ============================================================


def main():

    args = parse_arguments()

    run_pipeline(

        skip_training=args.skip_training,

        skip_report=args.skip_report,

        skip_presentation=args.skip_presentation,

    )


if __name__ == "__main__":

    main()