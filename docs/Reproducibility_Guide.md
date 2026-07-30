# Reproducibility Guide

> **Purpose:** This guide provides step-by-step instructions for reproducing the experiments performed in this repository, including environment setup, dataset preparation, model training, evaluation, and troubleshooting.

---

# Table of Contents

1. Introduction
2. System Requirements
3. Repository Structure
4. Environment Setup
5. Dependency Installation
6. Dataset Preparation
7. Working Directory Configuration
8. Running the Experiments
9. Expected Outputs
10. Troubleshooting
11. Verification Checklist
12. Reproducibility Notes

---

# 1. Introduction

This repository reproduces the experiments described in the research paper:

> **A Cost-Effective Sequential Route Recommender System for Taxi Drivers**

The implementation was originally developed using **TensorFlow 1.x**. This reproduction uses **TensorFlow 2.10** with the **compat.v1** API to maintain compatibility while running in a modern Python environment.

---

# 2. System Requirements

## Operating System

- Windows 10 / 11
- Ubuntu 20.04+
- macOS (untested)

---

## Python Version

```text
Python 3.10.x
```

> Python 3.11+ may introduce compatibility issues with TensorFlow 2.10.

---

## Recommended Hardware

| Component | Recommended |
|------------|-------------|
| CPU | Intel i5 / Ryzen 5 or better |
| RAM | 16 GB |
| Storage | 5 GB free |
| GPU | Optional (CUDA-compatible) |

---

# 3. Repository Structure

```
TaxiRouteReplication/

├── README.md
├── docs/
├── notebooks/
├── outputs/
├── report/
├── figures/
├── original_repo/
│
├── data/
│
└── results/
```

---

# 4. Environment Setup

## Step 1 — Create a Virtual Environment

```bash
python -m venv taxi_tf_env
```

---

## Step 2 — Activate the Environment

### Windows

```bash
taxi_tf_env\Scripts\activate
```

### Linux / macOS

```bash
source taxi_tf_env/bin/activate
```

---

# 5. Install Dependencies

Install the required packages:

```bash
pip install tensorflow==2.10
pip install numpy
pip install scipy
pip install pandas
pip install scikit-learn
pip install matplotlib
pip install networkx
pip install jupyter
```

Verify the installation:

```bash
python -c "import tensorflow as tf; print(tf.__version__)"
```

Expected output:

```text
2.10.0
```

---

# 6. Dataset Preparation

The original repository references:

```
sample_input.npy
```

This file is **not included** in the repository.

Instead, reconstruct it using the provided sparse matrices:

```
sample_last_dim_0.npz
sample_last_dim_1.npz
sample_last_dim_2.npz
```

The reconstruction process creates:

```
data/sample_input/sample_input.npy
```

Expected file size:

```
≈386 MB
```

Expected shape:

```python
(408, 82688, 3)
```

---

# 7. Working Directory Configuration

Before importing project modules, ensure the current working directory is:

```
Taxi-Route-Recommender/script
```

Example:

```python
import os
os.chdir("../original_repo/Taxi-Route-Recommender/script")
```

Verify:

```python
import os
print(os.getcwd())
```

---

# 8. Running the Experiments

## Step 1 — Import the Model

```python
from gcn_lstm_split import get_data
from gcn_lstm_split import GCNLSTM_SPLIT
```

---

## Step 2 — Load the Dataset

```python
data = get_data(
    ratios=[0.65,0.10,0.25],
    interested_clocks=[8,9,10],
    prior_days=3,
    prior_hours=6,
    usesample=True
)
```

Expected keys:

```python
print(data.keys())
```

---

## Step 3 — Build the Model

```python
model = GCNLSTM_SPLIT(
    N=data["N"],
    n_days=3,
    n_hours=6,
    input_dim=data["D"],
    weather_dim=data["DW"],
    days_gc_dims=[32],
    hours_gc_dims=[32],
    days_lstm_dims=[32],
    hours_lstm_dims=[32],
    dense_dims=[32,1]
)
```

---

## Step 4 — Train the Model

Execute the training loop using the provided `train_test()` function.

Expected output:

```
training step 0
training step 1
...
```

---

## Step 5 — Evaluate

Typical metrics:

```
Test MAE

Training Loss

Validation Loss
```

---

# 9. Expected Outputs

Dataset:

```
N = 5000
D = 3
DW = 14
```

Training:

```
Training Loss ↓
Validation Loss ↓
```

Prediction:

```
Prediction Range:
0.0 – 0.18 (approx.)

Label Range:
0.0 – 1.0
```

Evaluation:

```
Mean Absolute Error (MAE)
```

---

# 10. Common Issues and Solutions

## Issue 1 — Missing `sample_input.npy`

**Error**

```text
FileNotFoundError
```

**Solution**

Reconstruct `sample_input.npy` from the provided sparse matrices.

---

## Issue 2 — `ModuleNotFoundError: myutil`

**Cause**

Incorrect working directory.

**Solution**

Change to:

```
original_repo/Taxi-Route-Recommender/script
```

---

## Issue 3 — `get_data` Not Defined

**Cause**

The module was not imported.

**Solution**

```python
from gcn_lstm_split import get_data
```

---

## Issue 4 — SciPy Import Error

**Error**

```text
scipy.sparse.linalg.eigen.arpack
```

**Solution**

Update the import to:

```python
from scipy.sparse.linalg import eigsh
```

---

## Issue 5 — TensorFlow Warnings

Warnings related to:

```
dynamic_rnn

compat.v1

RMSProp
```

These are expected because the repository uses TensorFlow 1.x APIs through TensorFlow 2.x compatibility mode.

---

## Issue 6 — Relative Path Errors

Verify the working directory before running the notebook.

```python
import os
print(os.getcwd())
```

---

# 11. Verification Checklist

Before running the experiments:

- [ ] Python 3.10 installed
- [ ] Virtual environment activated
- [ ] TensorFlow 2.10 installed
- [ ] Required Python packages installed
- [ ] Working directory verified
- [ ] `sample_input.npy` reconstructed
- [ ] Notebook imports succeed
- [ ] Dataset loads correctly
- [ ] Model initializes
- [ ] Training completes
- [ ] Predictions generated
- [ ] MAE calculated

---

# 12. Reproducibility Notes

This reproduction successfully demonstrated:

- Repository setup
- Dataset reconstruction
- Environment migration
- Model execution
- Training pipeline reproduction
- Inference pipeline execution
- Performance evaluation

The repository was adapted to modern software versions while preserving the original model architecture and experimental workflow.

---

# Document Information

| Item | Value |
|------|-------|
| Document | Reproducibility Guide |
| Version | 1.0 |
| Status | Complete |
| Author | Rohit |
| Purpose | Enable reproducible execution of the project |

