# API Reference

> **Purpose:** This document provides detailed documentation for the public functions, classes, and utilities used throughout the GCN-LSTM Taxi Route Recommendation repository.

---

# Table of Contents

1. Module Overview
2. Main Modules
3. gcn_lstm_split.py
4. myutil.py
5. gcn/utils.py
6. gcn/layers.py
7. Data Dictionary
8. Tensor Shapes
9. Call Graph
10. Extension Guidelines

---

# 1. Module Overview

The repository is organized into four primary implementation modules.

| Module | Responsibility |
|---------|---------------|
| gcn_lstm_split.py | Main model construction and experiment execution |
| myutil.py | Dataset preprocessing and feature engineering |
| gcn/utils.py | Graph utilities and TensorFlow feed dictionary construction |
| gcn/layers.py | Graph Convolution implementation |

---

# 2. Module Relationships

```
Notebook
    │
    ▼
gcn_lstm_split.py
    │
    ├──────────────┐
    │              │
    ▼              ▼
myutil.py     gcn/utils.py
    │              │
    └──────┬───────┘
           ▼
     gcn/layers.py
```

---

# 3. gcn_lstm_split.py

---

## get_data()

### Purpose

Loads the traffic dataset, reconstructs temporal windows, prepares weather features, and splits the dataset into training, validation, and testing sets.

---

### Signature

```python
get_data(
    ratios,
    interested_clocks,
    prior_days,
    prior_hours,
    usesample=True
)
```

---

### Parameters

| Parameter | Type | Description |
|------------|------|-------------|
| ratios | list | Train/validation/test split ratios |
| interested_clocks | list | Hours selected for prediction |
| prior_days | int | Number of previous days |
| prior_hours | int | Number of previous hours |
| usesample | bool | Use sample dataset |

---

### Returns

Dictionary containing:

```python
{
    train_x_day,
    train_x_hour,
    train_x_weather_day,
    train_x_weather_hour,
    train_y,

    val_x_day,
    val_x_hour,
    val_y,

    test_x_day,
    test_x_hour,
    test_y,

    adj,

    N,
    D,
    DW
}
```

---

### Example

```python
data = get_data(
    ratios=[0.65,0.10,0.25],
    interested_clocks=[8,9,10],
    prior_days=3,
    prior_hours=6,
    usesample=True
)
```

---

## GCNLSTM_SPLIT

### Purpose

Main neural network model.

Implements:

- Graph Convolution
- Daily LSTM
- Hourly LSTM
- Dense Prediction Network

---

### Constructor

```python
GCNLSTM_SPLIT(
    N,
    n_days,
    n_hours,
    input_dim,
    weather_dim,
    days_gc_dims,
    hours_gc_dims,
    days_lstm_dims,
    hours_lstm_dims,
    dense_dims,
    learning_rate=0.01,
    dropout=0.2,
    act=tf.nn.relu
)
```

---

### Parameters

| Parameter | Description |
|------------|-------------|
| N | Number of road segments |
| n_days | Previous days |
| n_hours | Previous hours |
| input_dim | Traffic feature dimension |
| weather_dim | Weather feature dimension |
| days_gc_dims | Daily GCN hidden units |
| hours_gc_dims | Hourly GCN hidden units |
| days_lstm_dims | Daily LSTM units |
| hours_lstm_dims | Hourly LSTM units |
| dense_dims | Dense network architecture |
| learning_rate | RMSProp learning rate |
| dropout | Dropout probability |
| act | Activation function |

---

### Internal Components

```
Input

↓

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

---

### Important Attributes

| Attribute | Purpose |
|------------|----------|
| input_days | Daily traffic placeholder |
| input_hours | Hourly traffic placeholder |
| weather_input_days | Daily weather placeholder |
| weather_input_hours | Hourly weather placeholder |
| support | Adjacency matrix |
| label | Ground truth |
| output | Prediction |
| loss | Mean Squared Error |
| optimizer | RMSProp |
| train_op | Training operation |
| mae | Evaluation metric |

---

## train_test()

### Purpose

Runs complete training and evaluation.

---

### Signature

```python
train_test(
    model,
    data,
    flags
)
```

---

### Workflow

```
Initialize Session

↓

Initialize Variables

↓

Training Loop

↓

Validation

↓

Early Stopping

↓

Prediction

↓

MAE
```

---

### Returns

```python
(
predictions,
labels,
test_mae,
train_losses,
validation_losses,
label_range,
prediction_range
)
```

---

# 4. myutil.py

This module contains preprocessing utilities.

---

## normalize()

### Purpose

Normalizes traffic values.

---

### Input

```python
numpy.ndarray
```

---

### Output

```python
Normalized array
```

---

## generate_time_slices()

### Purpose

Creates historical windows.

Example:

```
Previous 3 Days

+

Previous 6 Hours
```

---

## part_data_time_slice()

### Purpose

Splits the complete dataset into temporal sequences.

---

### Output

```
Daily tensors

Hourly tensors

Labels
```

---

# 5. gcn/utils.py

---

## construct_feed_dict()

### Purpose

Maps NumPy arrays to TensorFlow placeholders.

---

### Inputs

```
Traffic

Weather

Labels

Adjacency Matrix
```

---

### Output

```
TensorFlow Feed Dictionary
```

---

## preprocess_adj()

### Purpose

Normalizes adjacency matrices before graph convolution.

---

## normalize_adj()

### Purpose

Computes normalized graph Laplacian.

---

## sparse_to_tuple()

### Purpose

Converts sparse matrices into TensorFlow-compatible tuples.

---

# 6. gcn/layers.py

---

## GraphConvolution

### Purpose

Graph Neural Network layer.

---

### Forward Pass

```
Input Features

↓

Weight Matrix

↓

Graph Propagation

↓

Bias

↓

Activation
```

---

### Inputs

```
Node Features

Adjacency Matrix
```

---

### Output

```
Hidden Representation
```

---

# 7. Data Dictionary

| Variable | Meaning |
|------------|----------|
| N | Number of roads |
| D | Traffic feature dimension |
| DW | Weather feature dimension |
| train_x_day | Daily training tensor |
| train_x_hour | Hourly training tensor |
| train_y | Training labels |
| val_x_day | Validation tensor |
| test_x_day | Test tensor |
| adj | Road network adjacency matrix |

---

# 8. Tensor Shapes

Typical sample dataset.

| Tensor | Shape |
|----------|----------------|
| Days | (samples, 3, 5000, 3) |
| Hours | (samples, 6, 5000, 3) |
| Weather Days | (samples, 3, 14) |
| Weather Hours | (samples, 6, 14) |
| Labels | (samples, 5000) |
| Adjacency | (5000,5000) |

---

# 9. Call Graph

```
Notebook

↓

get_data()

↓

GCNLSTM_SPLIT()

↓

construct_feed_dict()

↓

train_test()

↓

Prediction

↓

MAE
```

---

# 10. Extension Guidelines

Developers wishing to extend the project may consider:

### New Graph Layers

Replace

```
GraphConvolution
```

with

- Graph Attention Network (GAT)
- GraphSAGE
- Chebyshev Convolution

---

### Sequence Models

Replace

```
LSTM
```

with

- GRU
- Transformer
- Temporal Convolution Network

---

### Optimizers

Current:

```
RMSProp
```

Possible alternatives:

- Adam
- AdamW
- SGD

---

### Experiment Tracking

Recommended additions:

- TensorBoard
- MLflow
- Weights & Biases

---

# API Summary

| Component | Description |
|------------|-------------|
| get_data() | Dataset preparation |
| GCNLSTM_SPLIT | Neural network model |
| train_test() | Training and evaluation |
| construct_feed_dict() | TensorFlow input mapping |
| normalize() | Feature normalization |
| preprocess_adj() | Graph normalization |
| GraphConvolution | Graph learning layer |

---

# Document Information

| Item | Value |
|------|-------|
| Document | API Reference |
| Version | 1.0 |
| Status | Complete |
| Author | Rohit |
| Purpose | Developer reference for repository APIs |

