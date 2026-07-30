# Scripts

> Automation layer for the **Taxi Route Recommender System** project.

The `scripts/` package contains command-line entry points that orchestrate the complete machine learning and research workflow. Each script performs a specific stage of the pipeline while delegating implementation details to the reusable modules in the `src/` package.

---

## Purpose

The scripts automate the entire project lifecycle, including:

- Data preprocessing
- Transportation graph construction
- Model training
- Model evaluation
- Route prediction
- Figure generation
- Research report generation
- PowerPoint presentation generation
- End-to-end pipeline execution

---

# Directory Structure

```text
scripts/
│
├── __init__.py
├── preprocess.py
├── build_graph.py
├── train.py
├── evaluate.py
├── predict.py
├── generate_figures.py
├── build_report.py
├── build_presentation.py
├── run_pipeline.py
└── README.md
```

---

# Execution Order

The recommended execution sequence is:

```text
Raw Dataset
      │
      ▼
preprocess.py
      │
      ▼
build_graph.py
      │
      ▼
train.py
      │
      ▼
evaluate.py
      │
      ▼
predict.py
      │
      ▼
generate_figures.py
      │
      ▼
build_report.py
      │
      ▼
build_presentation.py
```

For most users, the complete workflow can be executed using:

```bash
python scripts/run_pipeline.py
```

---

# Script Reference

## preprocess.py

**Purpose**

Preprocess the raw taxi trip dataset.

### Responsibilities

- Load raw CSV data
- Handle missing values
- Remove duplicates
- Standardize column names
- Export cleaned dataset

### Example

```bash
python scripts/preprocess.py
```

---

## build_graph.py

**Purpose**

Construct the transportation graph.

### Responsibilities

- Load processed dataset
- Build graph representation
- Generate adjacency matrix
- Export GraphML
- Save graph statistics

### Example

```bash
python scripts/build_graph.py
```

---

## train.py

**Purpose**

Train the GCN-LSTM model.

### Responsibilities

- Load graph data
- Build model
- Train model
- Save trained model
- Export training history

### Example

```bash
python scripts/train.py
```

---

## evaluate.py

**Purpose**

Evaluate the trained model.

### Responsibilities

- Load trained model
- Evaluate test dataset
- Compute metrics
- Export evaluation report

### Example

```bash
python scripts/evaluate.py
```

---

## predict.py

**Purpose**

Generate predictions using the trained model.

### Responsibilities

- Load trained model
- Perform inference
- Export prediction results

### Example

```bash
python scripts/predict.py
```

---

## generate_figures.py

**Purpose**

Generate publication-quality figures.

### Responsibilities

- Training history plot
- Prediction visualization
- Correlation heatmap
- Confusion matrix
- Export figures

### Example

```bash
python scripts/generate_figures.py
```

---

## build_report.py

**Purpose**

Generate the final research report.

### Responsibilities

- Build report from Markdown
- Compile chapters
- Export PDF

### Example

```bash
python scripts/build_report.py
```

---

## build_presentation.py

**Purpose**

Generate the final PowerPoint presentation.

### Responsibilities

- Build slides
- Embed figures
- Apply layouts
- Export PPTX

### Example

```bash
python scripts/build_presentation.py
```

---

## run_pipeline.py

**Purpose**

Execute the complete research workflow.

### Responsibilities

- Run every stage in sequence
- Display execution summary
- Stop on failure
- Measure execution time

### Example

Run the full workflow:

```bash
python scripts/run_pipeline.py
```

Skip model training:

```bash
python scripts/run_pipeline.py --skip-training
```

Skip report generation:

```bash
python scripts/run_pipeline.py --skip-report
```

Skip presentation generation:

```bash
python scripts/run_pipeline.py --skip-presentation
```

---

# Inputs and Outputs

| Script | Input | Output |
|---------|-------|--------|
| preprocess.py | Raw CSV | Processed CSV |
| build_graph.py | Processed CSV | GraphML, Adjacency Matrix |
| train.py | Graph | Trained Model |
| evaluate.py | Model, Test Dataset | Evaluation Metrics |
| predict.py | Model, Dataset | Predictions |
| generate_figures.py | Training History, Metrics | PNG Figures |
| build_report.py | Markdown Chapters | PDF Report |
| build_presentation.py | Markdown Slides, Figures | PPTX Presentation |
| run_pipeline.py | Entire Project | Complete Workflow |

---

# Dependencies

Install project dependencies before running any script.

```bash
pip install -r requirements.txt
```

---

# Logging

Every script provides:

- Informative progress messages
- Execution timing
- Error reporting
- Completion summary

This makes long-running workflows easier to monitor and debug.

---

# Best Practices

- Run scripts from the project root directory.
- Execute `preprocess.py` before `build_graph.py`.
- Train a model before evaluation or prediction.
- Regenerate figures after model training if outputs have changed.
- Use `run_pipeline.py` for full reproducibility.

---

# Troubleshooting

## ModuleNotFoundError

Ensure the project root is the current working directory.

```bash
cd TaxiRouteReplication
```

---

## Missing Data Files

Verify that required datasets are present in the `data/` directory.

---

## Missing Model

Run the training stage before evaluation or prediction.

```bash
python scripts/train.py
```

---

## Permission Errors

Ensure the application has write access to:

- `output/`
- `models/`
- `figures/`

---

# Future Improvements

Potential enhancements include:

- Configuration file support
- Parallel execution
- Hyperparameter search
- Experiment tracking
- Distributed training
- Docker integration
- CI/CD pipeline automation

---

# Author

**Rohit Shetye**

---

# License

This project is licensed under the MIT License.