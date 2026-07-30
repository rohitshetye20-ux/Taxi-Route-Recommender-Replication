# Experiment Log

> **Purpose:** This document provides a chronological record of the experimental process undertaken to reproduce the GCN-LSTM Taxi Route Recommendation system. It documents setup decisions, debugging efforts, engineering challenges, intermediate findings, and final outcomes.

---

# Experiment Information

| Item | Value |
|------|-------|
| Project | Taxi Route Recommendation using GCN-LSTM |
| Paper | A Cost-Effective Sequential Route Recommender System for Taxi Drivers |
| Objective | Reproduce the original implementation |
| Framework | TensorFlow 2.10 (compat.v1) |
| Python | 3.10 |
| Status | Successfully Reproduced |

---

# Experiment Timeline

## Phase 1 — Repository Investigation

### Objective

Understand the repository structure before executing any code.

### Activities

- Cloned the original repository.
- Reviewed the project layout.
- Identified major source files.
- Mapped the relationship between data, model, and utilities.
- Located the primary training script (`gcn_lstm_split.py`).

### Outcome

Repository architecture successfully understood.

---

## Phase 2 — Environment Setup

### Objective

Create a compatible execution environment.

### Activities

- Installed Python 3.10.
- Created a dedicated virtual environment.
- Installed TensorFlow 2.10.
- Installed supporting scientific libraries:
  - NumPy
  - SciPy
  - Pandas
  - scikit-learn
  - NetworkX
  - Matplotlib
  - Jupyter

### Challenges

TensorFlow 1.x was incompatible with modern Python versions.

### Resolution

Executed the project using TensorFlow 2.10 with the `compat.v1` compatibility layer.

---

## Phase 3 — Dependency Resolution

### Objective

Resolve compatibility issues preventing execution.

### Issues Encountered

- TensorFlow API changes
- SciPy import changes
- Missing modules
- Package version conflicts
- Relative import errors

### Engineering Actions

- Updated deprecated imports.
- Corrected module paths.
- Verified package compatibility.
- Standardized the execution environment.

### Outcome

Project imported successfully.

---

## Phase 4 — Dataset Investigation

### Objective

Validate dataset availability.

### Observation

The repository referenced:

```
sample_input.npy
```

This file was missing.

### Investigation

Examined the available files.

Found:

- sample_last_dim_0.npz
- sample_last_dim_1.npz
- sample_last_dim_2.npz

### Conclusion

The missing dataset could be reconstructed from the provided sparse matrices.

---

## Phase 5 — Dataset Reconstruction

### Objective

Recreate the missing dataset.

### Activities

- Loaded sparse matrices.
- Converted them into dense arrays.
- Combined feature channels.
- Saved the reconstructed dataset.

### Result

Generated:

```
sample_input.npy
```

### Dataset Characteristics

| Property | Value |
|-----------|------:|
| Shape | (408, 82688, 3) |
| Size | ~386 MB |
| Data Type | float32 |

### Outcome

The original data pipeline became executable.

---

## Phase 6 — Data Pipeline Analysis

### Objective

Understand preprocessing before training.

### Investigated Functions

- `get_data()`
- Temporal slicing
- Weather feature generation
- Dataset partitioning
- Adjacency loading

### Validation

Confirmed:

```
N = 5000

D = 3

DW = 14
```

Generated tensors for:

- Daily sequences
- Hourly sequences
- Labels
- Weather features

### Outcome

Data pipeline successfully validated.

---

## Phase 7 — Model Architecture Analysis

### Objective

Reverse engineer the neural network.

### Findings

The model consists of:

```
Graph Convolution

↓

Daily LSTM

↓

Hourly LSTM

↓

Dense Layers

↓

Prediction
```

### Model Statistics

| Metric | Value |
|----------|------:|
| Trainable Parameters | 22,593 |

### Outcome

Architecture successfully documented.

---

## Phase 8 — Training Pipeline

### Objective

Execute the original training workflow.

### Activities

- Initialized TensorFlow graph.
- Constructed feed dictionaries.
- Executed training loop.
- Recorded losses.
- Generated predictions.

### Training Output

| Epoch | Training Loss | Validation Loss |
|------:|--------------:|----------------:|
| 0 | 0.06395 | 0.07469 |
| 1 | 0.05993 | 0.07212 |
| 2 | 0.05843 | 0.07266 |
| 3 | 0.05744 | 0.07147 |
| 4 | 0.05662 | 0.07221 |

### Observation

Training converged smoothly with stable validation performance.

---

## Phase 9 — Model Evaluation

### Objective

Evaluate prediction quality.

### Metric

Mean Absolute Error (MAE)

### Result

```
Test MAE = 0.08384
```

### Prediction Range

```
0.0000

↓

0.1872
```

### Label Range

```
0.0000

↓

1.0000
```

### Outcome

Model successfully produced valid predictions.

---

## Phase 10 — Documentation

### Objective

Transform the reproduction into a professional engineering portfolio.

### Documentation Produced

- README
- Project Overview
- Repository Guide
- Reproducibility Guide
- Code Architecture
- API Reference
- Architecture Analysis
- Data Pipeline
- Experiment Report
- Performance Analysis
- Challenges
- Lessons Learned

### Outcome

Repository documentation significantly expanded beyond the original implementation.

---

# Key Engineering Challenges

| Challenge | Resolution |
|-----------|------------|
| Missing dataset | Reconstructed `sample_input.npy` |
| TensorFlow compatibility | Used TensorFlow 2.10 `compat.v1` |
| SciPy API changes | Updated imports |
| Relative path issues | Corrected working directory |
| Module import errors | Adjusted Python path |

---

# Lessons from the Reproduction

- Academic repositories often require substantial engineering effort before experiments can be reproduced.
- Environment configuration is as important as model implementation.
- Thorough documentation improves maintainability and reproducibility.
- Understanding the data pipeline is essential before analyzing the model.
- Small compatibility issues can prevent successful execution despite correct logic.

---

# Final Outcome

## Successfully Completed

- Repository investigation
- Environment setup
- Dependency resolution
- Dataset reconstruction
- Data preprocessing
- Model analysis
- Training execution
- Evaluation
- Performance analysis
- Professional documentation

---

# Overall Assessment

| Area | Status |
|------|--------|
| Environment Setup | ✅ Complete |
| Dataset Reconstruction | ✅ Complete |
| Data Pipeline | ✅ Complete |
| Model Construction | ✅ Complete |
| Training | ✅ Complete |
| Evaluation | ✅ Complete |
| Documentation | ✅ Complete |
| Experiment Reproduction | ✅ Successful |

---

# Conclusion

The reproduction successfully executed the original GCN-LSTM Taxi Route Recommendation pipeline within a modern Python environment. In addition to reproducing the published workflow, the project documented the engineering adaptations required to address missing datasets, dependency changes, and framework compatibility, resulting in a reproducible and portfolio-ready implementation.

---

# Document Information

| Item | Value |
|------|-------|
| Document | Experiment Log |
| Version | 1.0 |
| Status | Complete |
| Author | Rohit |
| Purpose | Chronological engineering log of the reproduction process |

