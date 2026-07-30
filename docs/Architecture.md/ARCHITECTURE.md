# System Architecture

## Project

**Reproduction of "A Cost-Effective Sequential Route Recommender System for Taxi Drivers"**

---

# Table of Contents

1. Project Overview
2. Repository Architecture
3. High-Level System Architecture
4. Repository Modules
5. Module Dependency Graph
6. Data Flow Architecture
7. Model Architecture
8. Training Pipeline
9. Inference Pipeline
10. Directory Structure
11. Design Decisions
12. Engineering Observations
13. Future Improvements

---

# 1. Project Overview

## Objective

The objective of this project is to reproduce the experiments presented in the paper:

> **A Cost-Effective Sequential Route Recommender System for Taxi Drivers**

The proposed framework combines

- Graph Convolutional Networks (GCN)
- Long Short-Term Memory Networks (LSTM)

to learn

- Spatial road relationships
- Temporal traffic patterns

and predict future road demand for taxi route recommendation.

---

# 2. Repository Architecture

The repository is organized into multiple independent modules.

```

```
                    +----------------------+
                    |   Dataset (.npz)     |
                    +----------+-----------+
                               |
                               |
                     Dataset Reconstruction
                               |
                               |
                               ▼
                     sample_input.npy
                               |
                               |
                     get_data()
                               |
         +---------------------+---------------------+
         |                     |                     |
         |                     |                     |
   Training Set          Validation Set        Test Set
         |                     |                     |
         +---------------------+---------------------+
                               |
                               |
                     GCNLSTM_SPLIT
                               |
               +---------------+---------------+
               |                               |
        Graph Convolution                 Weather Features
               |                               |
               +---------------+---------------+
                               |
                              LSTM
                               |
                          Dense Layers
                               |
                         Demand Prediction
```

---

# 3. High-Level System Architecture

The complete system consists of six logical layers.

```

```
Raw Data

↓

Sparse Feature Files

↓

Dataset Reconstruction

↓

Data Preprocessing

↓

GCN-LSTM Model

↓

Prediction
```

---

# Layer 1 — Data Storage

Responsible for storing

- Road network
- Historical traffic
- Weather information

Files

```

data/
sample_input/
```

---

# Layer 2 — Data Processing

Implemented in

```

gcn_lstm_split.py

myutil.py
```

Responsibilities

- Load data
- Normalize adjacency matrix
- Generate time slices
- Split datasets
- Weather integration

---

# Layer 3 — Graph Processing

Implemented inside

```

gcn/

layers.py

models.py

utils.py
```

Responsibilities

- Graph convolution
- Adjacency preprocessing
- Graph feature propagation

---

# Layer 4 — Temporal Modeling

Uses

TensorFlow Dynamic RNN

LSTM

Responsibilities

- Learn temporal dependency
- Capture historical traffic trends

---

# Layer 5 — Prediction

Dense neural network

Output

Traffic demand probability

---

# Layer 6 — Route Recommendation

Implemented in

```

path_searching_application.py
```

Uses

- predicted demand
- road graph

to search for optimal taxi routes.

---

# 4. Repository Modules

| Module | Responsibility |
|---------|----------------|
| gcn_lstm_split.py | Main model implementation |
| myutil.py | Utility functions |
| path_searching_application.py | Route search |
| gcn/layers.py | Graph layers |
| gcn/models.py | Graph models |
| gcn/utils.py | Graph utilities |
| gcn/inits.py | Weight initialization |
| gcn/metrics.py | Loss and accuracy |

---

# 5. Module Dependency Graph

```

```
gcn_lstm_split.py

│

├── myutil.py

├── numpy

├── pandas

├── scipy

├── sklearn

├── tensorflow.compat.v1

└── gcn

├── inits.py

├── layers.py

├── models.py

├── utils.py

└── metrics.py
```

The project follows a modular architecture where the primary model delegates graph-specific functionality to the `gcn` package while relying on `myutil.py` for dataset preparation.

---

# 6. Data Flow Architecture

The complete data flow is shown below.

```

```
Sparse Feature Matrices (.npz)

↓

Reconstructed Dataset

↓

sample_input.npy

↓

get_data()

↓

Road Sampling

↓

Time Slicing

↓

Weather Features

↓

Train Validation Test Split

↓

Model Input
```

Input tensors

| Tensor | Description |
|---------|-------------|
| train_x_day | Previous daily observations |
| train_x_hour | Previous hourly observations |
| train_weather_day | Daily weather |
| train_weather_hour | Hourly weather |
| train_y | Target labels |

---

# 7. Model Architecture

The model consists of four major stages.

```

```
Traffic Features

↓

Graph Convolution

↓

LSTM

↓

Dense Layer

↓

Prediction
```

## Graph Convolution

Purpose

Learn spatial relationships between adjacent roads.

Input

```
N × D
```

Output

```
N × Hidden
```

---

## LSTM

Purpose

Learn temporal traffic evolution.

Input

Sequential graph features

Output

Hidden temporal representation.

---

## Dense Network

Converts temporal features into

```
Predicted demand

0–1
```

---

# 8. Training Pipeline

```

```
Initialize Model

↓

Initialize Variables

↓

Feed Dictionary

↓

Forward Pass

↓

Loss Calculation

↓

Backpropagation

↓

Parameter Update

↓

Validation

↓

Early Stopping

↓

Prediction
```

Optimizer

RMSProp

Loss

Mean Absolute Error

---

# 9. Inference Pipeline

```

```
Load Model

↓

Load Test Data

↓

Forward Pass

↓

Predicted Demand

↓

Route Recommendation
```

---

# 10. Directory Structure

```

TaxiRouteReplication_Portfolio/

docs/

figures/

outputs/

report/

scripts/

notebooks/

original_repo/
```

---

# 11. Design Decisions

The original implementation makes several notable architectural choices:

- TensorFlow 1.x graph execution
- Modular separation of graph utilities
- Sparse adjacency representation
- Combined spatial-temporal learning
- Weather feature fusion
- Relative file paths for data loading

---

# 12. Engineering Observations

During reproduction, several engineering considerations became apparent:

- Legacy TensorFlow APIs require compatibility mode.
- The project assumes execution from specific working directories because it relies on relative paths.
- Dataset reconstruction is necessary because the released repository distributes sparse feature matrices instead of a prebuilt `sample_input.npy`.
- The codebase cleanly separates graph processing, temporal modeling, utilities, and route search, making it easier to analyze each component independently.

---

# 13. Future Improvements

Potential enhancements include:

- TensorFlow 2.x migration
- PyTorch Geometric implementation
- Configuration-driven experiments
- Docker-based environment
- Continuous Integration (CI)
- Automated experiment tracking
- Interactive visualization dashboard

---

# Conclusion

The reproduced repository follows a modular architecture that combines graph neural networks and recurrent neural networks to capture both spatial and temporal dependencies in taxi demand prediction. Despite relying on legacy TensorFlow 1.x APIs, the separation of concerns across data processing, graph computation, temporal modeling, and route recommendation provides a clear and extensible design that supports reproducible experimentation.
