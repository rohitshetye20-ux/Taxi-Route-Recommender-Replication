# Experiment Reproduction

## Project

**Reproduction of "A Cost-Effective Sequential Route Recommender System for Taxi Drivers"**

---

# Table of Contents

1. Objective
2. Experimental Environment
3. Repository Preparation
4. Dataset Preparation
5. Model Configuration
6. Training Procedure
7. Evaluation Procedure
8. Experimental Results
9. Reproducibility Guide
10. Observations
11. Limitations
12. Future Work

---

# 1. Objective

The goal of this experiment is to reproduce the Graph Convolutional Network (GCN) and Long Short-Term Memory (LSTM) model proposed in the research paper for taxi route recommendation.

The reproduction process includes:

- Environment setup
- Dependency resolution
- Dataset reconstruction
- Model execution
- Training
- Evaluation
- Result verification

---

# 2. Experimental Environment

## Hardware

| Component | Value |
|----------|-------|
| Operating System | Windows 11 Home |
| CPU | AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx (2.10 GHz) |
| RAM | 8 GB RAM |
| GPU | CPU Execution |

---

## Software

| Software | Version |
|----------|----------|
| Python | 3.10 |
| TensorFlow | 2.10.1 (compat.v1 mode) |
| NumPy | 1.23.5 |
| SciPy | 1.10.1 |
| Pandas | 2.x |
| Jupyter Notebook | Latest |

---

# 3. Repository Preparation

The original repository required several modifications before execution.

## Environment Fixes

Completed:

- Installed Python 3.10
- Created isolated virtual environment
- Installed TensorFlow 2.10.1
- Downgraded NumPy to 1.23.5
- Installed compatible SciPy version
- Configured Jupyter kernel
- Added repository `script` directory to the Python path

---

## Dataset Reconstruction

The repository expected:

```

sample_input.npy

```

However, only sparse feature matrices were provided.

The dataset was reconstructed from:

```

sample_last_dim_0.npz
sample_last_dim_1.npz
sample_last_dim_2.npz

```

Result:

```

Shape:
(408, 82688, 3)

Size:
386 MB

```

---

# 4. Dataset Preparation

The reconstructed dataset was loaded using:

```

get_data()

```

Configuration:

| Parameter | Value |
|-----------|------:|
| Train Ratio | 0.65 |
| Validation Ratio | 0.10 |
| Test Ratio | 0.25 |
| Prior Days | 3 |
| Prior Hours | 6 *(Paper configuration may differ; adjust if reproducing another setting.)* |
| Sample Roads | 5000 |

Returned tensors included:

- train_x_day
- train_x_hour
- train_weather_day
- train_weather_hour
- train_y
- validation tensors
- test tensors
- adjacency matrix

---

# 5. Model Configuration

The GCNLSTM model was initialized with:

| Hyperparameter | Value |
|----------------|------:|
| Input Dimension | 3 |
| Weather Dimension | 14 |
| Number of Roads | 5000 |
| Prior Days | 3 |
| Prior Hours | 6 |
| Learning Rate | 0.01 |
| Dropout | 0.20 |

Model Components:

- Graph Convolution Layer
- LSTM Layer (Daily)
- LSTM Layer (Hourly)
- Dense Layers
- RMSProp Optimizer

Total Trainable Parameters:

```

22,593

```

---

# 6. Training Procedure

Training followed the official implementation.

Workflow:

```

Load Data

↓

Build Graph

↓

Initialize Variables

↓

Construct Feed Dictionary

↓

Forward Pass

↓

Loss Computation

↓

Optimizer Step

↓

Validation

↓

Repeat

```

Optimizer:

```

RMSProp

```

Loss Function:

```

Mean Absolute Error (MAE)

```

Early stopping was supported by the original implementation.

---

# 7. Evaluation Procedure

After training, predictions were generated using the test dataset.

Evaluation steps:

1. Forward pass
2. Prediction clipping
3. Mean Absolute Error calculation
4. Comparison with ground truth labels

---

# 8. Experimental Results

## Dataset Summary

| Item | Value |
|------|------:|
| Number of Roads | 5000 |
| Feature Channels | 3 |
| Weather Features | 14 |

---

## Training Summary

Example training log:

```

training step 0
training step 1
training step 2
training step 3
training step 4

```

---

## Evaluation Metrics

| Metric | Value |
|---------|-------|
| Test MAE | 0.0838 |
| Prediction Range | 0.0 – 0.1872 |
| Label Range | 0.0 – 1.0 |

These results indicate that the model successfully executed and produced demand predictions on the sample dataset.

---

# 9. Reproducibility Guide

To reproduce the experiment:

1. Clone the repository.
2. Create a Python 3.10 environment.
3. Install the required dependencies.
4. Reconstruct `sample_input.npy` from the sparse matrices.
5. Ensure the working directory matches the repository layout.
6. Load the dataset using `get_data()`.
7. Build the `GCNLSTM_SPLIT` model.
8. Train the model.
9. Evaluate the trained model on the test set.

---

# 10. Observations

Key observations during reproduction:

- TensorFlow 1.x compatibility mode was required.
- Relative file paths depended on the current working directory.
- Dataset reconstruction was necessary before execution.
- The modular implementation simplified debugging and analysis.
- The sample dataset enabled validation of the complete training pipeline.

---

# 11. Limitations

The reproduced experiment has the following limitations:

- Executed on the released sample dataset rather than the complete research dataset.
- CPU-only execution.
- TensorFlow 1.x architecture relies on deprecated APIs.
- Results are representative of the sample data and may not match the original paper's full-scale experiments exactly.

---

# 12. Future Work

Potential extensions include:

- Migration to TensorFlow 2.x
- PyTorch Geometric implementation
- Hyperparameter optimization
- Automated experiment tracking
- Docker-based reproducibility
- Integration with real-time traffic data

---

# Conclusion

The complete experiment reproduction was successfully performed using the official implementation and released sample data. Legacy dependency issues were resolved, the missing dataset was reconstructed, and the GCN-LSTM model was trained and evaluated successfully. The project demonstrates a reproducible workflow for analyzing and executing a research-grade deep learning model for taxi route recommendation.
