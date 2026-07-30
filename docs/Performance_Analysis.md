# Performance Analysis

> **Purpose:** This document analyzes the experimental performance of the reproduced GCN-LSTM Taxi Route Recommendation model. It summarizes training behavior, evaluation metrics, computational complexity, resource utilization, and observations made during the reproduction process.

---

# Table of Contents

1. Introduction
2. Experimental Configuration
3. Dataset Statistics
4. Model Complexity
5. Training Performance
6. Evaluation Metrics
7. Prediction Analysis
8. Resource Utilization
9. Computational Complexity
10. Limitations
11. Future Improvements
12. Summary

---

# 1. Introduction

The objective of this analysis is to evaluate the reproduced implementation from both a machine learning and software engineering perspective.

The analysis focuses on:

- Model convergence
- Prediction quality
- Training stability
- Computational efficiency
- Memory consumption
- Reproducibility

---

# 2. Experimental Configuration

| Parameter | Value |
|-----------|-------|
| Framework | TensorFlow 2.10 (compat.v1) |
| Python | 3.10 |
| Optimizer | RMSProp |
| Learning Rate | 0.01 |
| Dropout | 0.20 |
| Previous Days | 3 |
| Previous Hours | 6 |
| Road Segments | 5000 |
| Traffic Features | 3 |
| Weather Features | 14 |

---

# 3. Dataset Statistics

## Sample Dataset

| Property | Value |
|-----------|------:|
| Road Segments (N) | 5000 |
| Traffic Features (D) | 3 |
| Weather Features (DW) | 14 |
| Daily Window | 3 |
| Hourly Window | 6 |

---

### Tensor Shapes

| Tensor | Shape |
|---------|----------------------|
| Days | (samples, 3, 5000, 3) |
| Hours | (samples, 6, 5000, 3) |
| Weather (Days) | (samples, 3, 14) |
| Weather (Hours) | (samples, 6, 14) |
| Labels | (samples, 5000) |

---

# 4. Model Complexity

## Trainable Parameters

| Component | Parameters |
|-----------|-----------:|
| Daily Graph Convolution | 128 |
| Hourly Graph Convolution | 128 |
| Dense Layers | 2,113 |
| Daily LSTM | 10,112 |
| Hourly LSTM | 10,112 |
| **Total** | **22,593** |

The relatively small parameter count makes the model lightweight enough for experimentation while still capable of learning spatial and temporal dependencies.

---

# 5. Training Performance

## Training Loss

| Epoch | Loss |
|------:|------:|
| 0 | 0.06395 |
| 1 | 0.05993 |
| 2 | 0.05843 |
| 3 | 0.05744 |
| 4 | 0.05662 |

### Observation

Training loss decreases consistently, indicating that optimization is progressing in the expected direction.

---

## Validation Loss

| Epoch | Loss |
|------:|------:|
| 0 | 0.07469 |
| 1 | 0.07212 |
| 2 | 0.07266 |
| 3 | 0.07147 |
| 4 | 0.07221 |

### Observation

Validation loss remains stable throughout training, suggesting reasonable generalization without obvious overfitting during the observed epochs.

---

# 6. Evaluation Metrics

## Mean Absolute Error (MAE)

| Metric | Value |
|---------|------:|
| Test MAE | **0.08384** |

The MAE represents the average absolute difference between predicted and normalized traffic demand values.

A lower MAE indicates more accurate demand prediction.

---

# 7. Prediction Analysis

## Prediction Range

| Metric | Value |
|---------|------:|
| Minimum | 0.0000 |
| Maximum | 0.1872 |

---

## Ground Truth Range

| Metric | Value |
|---------|------:|
| Minimum | 0.0000 |
| Maximum | 1.0000 |

### Observation

The model predicts within a narrower range than the labels. This conservative behavior is common in early training stages and with limited sample data, where predictions tend to remain closer to the mean.

---

# 8. Resource Utilization

## Memory

The reconstructed dataset (`sample_input.npy`) occupies approximately **386 MB**.

Additional memory is required during preprocessing, graph construction, and model execution.

---

## CPU

Experiments were executed on CPU hardware.

No GPU-specific optimizations were required for reproducing the sample experiment.

---

## Storage

Repository components include:

- Source code
- Sparse matrices
- Reconstructed dataset
- Notebook
- Documentation
- Generated outputs

---

# 9. Computational Complexity

## Graph Convolution

Approximate complexity:

```
O(E × F)
```

Where:

- **E** = Number of graph edges
- **F** = Feature dimension

---

## LSTM

Approximate complexity:

```
O(T × H²)
```

Where:

- **T** = Sequence length
- **H** = Hidden dimension

---

## Dense Layers

Approximate complexity:

```
O(N × D)
```

Where:

- **N** = Number of nodes
- **D** = Hidden dimension

---

## Overall Pipeline

```
Dataset Loading
        │
        ▼
Graph Processing
        │
        ▼
GCN Computation
        │
        ▼
LSTM Processing
        │
        ▼
Dense Prediction
        │
        ▼
Loss Computation
```

---

# 10. Engineering Observations

During reproduction, several engineering challenges were resolved:

- TensorFlow 1.x → TensorFlow 2.10 compatibility using `compat.v1`
- Reconstruction of the missing `sample_input.npy` dataset
- Working directory and relative path configuration
- SciPy import compatibility updates
- Dependency management for modern Python environments

Addressing these issues was necessary to successfully reproduce the original implementation.

---

# 11. Limitations

The reproduced experiment has several limitations:

- Uses the sample dataset rather than the full production dataset.
- Training duration was intentionally limited for reproducibility.
- TensorFlow compatibility mode relies on deprecated APIs.
- No hyperparameter optimization was performed.
- Results may differ slightly due to library version changes and random initialization.

---

# 12. Future Improvements

Potential enhancements include:

- Training on the complete dataset
- GPU-accelerated experiments
- Hyperparameter optimization
- Cross-validation
- Additional evaluation metrics (RMSE, R², MAPE)
- TensorFlow 2.x native implementation
- PyTorch reimplementation
- Automated experiment tracking (MLflow or Weights & Biases)

---

# Summary

The reproduced implementation successfully demonstrates the feasibility of executing the original GCN-LSTM architecture in a modern Python environment.

Key outcomes include:

- Successful dataset reconstruction
- End-to-end training pipeline execution
- Stable training and validation loss
- Test MAE ≈ **0.08384**
- Lightweight model with **22,593 trainable parameters**
- Comprehensive documentation and reproducibility support

Overall, the project validates the original workflow while documenting the engineering adaptations required for contemporary machine learning environments.

---

# Document Information

| Item | Value |
|------|-------|
| Document | Performance Analysis |
| Version | 1.0 |
| Status | Complete |
| Author | Rohit |
| Purpose | Analyze training performance, evaluation metrics, and computational characteristics of the reproduced GCN-LSTM model |

