# Model Reference

> **Purpose:** This document provides a comprehensive technical reference for the GCN-LSTM model implemented in this repository. It describes the network architecture, layer composition, tensor dimensions, trainable parameters, mathematical operations, and execution flow.

---

# Table of Contents

1. Model Overview
2. Model Objectives
3. Architecture Summary
4. Input Specification
5. Graph Convolution Network
6. Temporal Learning (LSTM)
7. Dense Prediction Network
8. Loss Function
9. Optimizer
10. Trainable Parameters
11. Tensor Shapes
12. Forward Pass
13. Training Pipeline
14. Inference Pipeline
15. Hyperparameters
16. Computational Complexity
17. Advantages
18. Limitations
19. Future Improvements

---

# 1. Model Overview

The repository implements a hybrid neural network that combines:

- Graph Convolution Network (GCN)
- Long Short-Term Memory (LSTM)
- Fully Connected Neural Network

The model predicts future taxi demand for every road segment by jointly learning spatial and temporal traffic patterns.

---

# 2. Model Objectives

The model learns three complementary relationships:

### Spatial Dependencies

Road segments influence neighboring roads.

Captured using:

```
Graph Convolution
```

---

### Daily Temporal Patterns

Traffic tends to repeat daily.

Captured using:

```
Daily LSTM
```

---

### Hourly Temporal Patterns

Traffic changes throughout the day.

Captured using:

```
Hourly LSTM
```

---

# 3. Overall Architecture

```
                 Historical Traffic Data
                           │
                           ▼
                  Feature Extraction
                           │
                           ▼
                 Graph Convolution Layer
                  (Daily + Hourly)
                           │
                           ▼
             Daily LSTM        Hourly LSTM
                    │             │
                    └──────┬──────┘
                           ▼
                   Feature Concatenation
                           │
                           ▼
                    Fully Connected
                           │
                           ▼
                   Traffic Prediction
```

---

# 4. Input Specification

## Daily Traffic

Shape

```
(batch_size,
3,
5000,
3)
```

Meaning

```
3 previous days

5000 road segments

3 traffic features
```

---

## Hourly Traffic

Shape

```
(batch_size,
6,
5000,
3)
```

Meaning

```
6 previous hours

5000 roads

3 features
```

---

## Weather Features

Daily

```
(batch_size,
3,
14)
```

Hourly

```
(batch_size,
6,
14)
```

---

## Adjacency Matrix

Shape

```
5000 × 5000
```

Represents the road network graph.

---

# 5. Graph Convolution Network

## Purpose

Extract spatial relationships between road segments.

Unlike traditional CNNs operating on grids, the GCN aggregates information from connected road segments.

---

## Inputs

```
Traffic Features

+

Adjacency Matrix
```

---

## Output

```
Spatial Feature Representation
```

---

## Layer Dimensions

Daily

```
3

↓

32
```

Hourly

```
3

↓

32
```

---

## Trainable Parameters

| Layer | Parameters |
|---------|-----------:|
| Daily GCN | 128 |
| Hourly GCN | 128 |

---

# 6. LSTM Network

Two independent LSTM branches capture temporal information.

---

## Daily LSTM

Purpose

Capture long-term periodic behavior.

Input

```
Previous 3 Days
```

Output

```
Hidden Representation
```

---

## Hourly LSTM

Purpose

Capture short-term dynamics.

Input

```
Previous 6 Hours
```

Output

```
Hidden Representation
```

---

## LSTM Parameters

| Layer | Parameters |
|---------|-----------:|
| Daily LSTM | 10,112 |
| Hourly LSTM | 10,112 |

---

# 7. Dense Prediction Network

Outputs from both LSTMs are concatenated.

```
Daily Features

+

Hourly Features

↓

Dense Layer

↓

Output Layer
```

---

## Dimensions

```
64

↓

32

↓

1
```

---

## Parameters

| Layer | Parameters |
|---------|-----------:|
| Dense Network | 2,113 |

---

# 8. Loss Function

Training minimizes the prediction error using Mean Squared Error (MSE).

```
Prediction

↓

Ground Truth

↓

Mean Squared Error
```

The repository also reports Mean Absolute Error (MAE) for evaluation.

---

# 9. Optimizer

Optimizer

```
RMSProp
```

Learning Rate

```
0.01
```

Dropout

```
0.20
```

Activation

```
ReLU
```

---

# 10. Trainable Parameters

| Component | Parameters |
|------------|-----------:|
| Daily GCN | 128 |
| Hourly GCN | 128 |
| Daily LSTM | 10,112 |
| Hourly LSTM | 10,112 |
| Dense Layers | 2,113 |
| **Total** | **22,593** |

---

# 11. Tensor Shapes

| Tensor | Shape |
|----------|----------------|
| Input Days | (B,3,5000,3) |
| Input Hours | (B,6,5000,3) |
| Weather Days | (B,3,14) |
| Weather Hours | (B,6,14) |
| Labels | (B,5000) |
| Adjacency | (5000,5000) |

Where **B** is the batch size.

---

# 12. Forward Pass

```
Traffic Input
        │
        ▼
Graph Convolution
        │
        ▼
Daily LSTM
        │
        ▼
Hourly LSTM
        │
        ▼
Concatenate Features
        │
        ▼
Dense Layer
        │
        ▼
Prediction
```

---

# 13. Training Pipeline

```
Load Dataset
      │
      ▼
Construct Feed Dictionary
      │
      ▼
Forward Pass
      │
      ▼
Loss Computation
      │
      ▼
Backpropagation
      │
      ▼
RMSProp Update
```

---

# 14. Inference Pipeline

```
Historical Traffic
        │
        ▼
Feature Extraction
        │
        ▼
Graph Convolution
        │
        ▼
LSTM
        │
        ▼
Dense Prediction
        │
        ▼
Predicted Demand
```

---

# 15. Hyperparameters

| Hyperparameter | Value |
|---------------|------:|
| Prior Days | 3 |
| Prior Hours | 6 |
| Traffic Features | 3 |
| Weather Features | 14 |
| Learning Rate | 0.01 |
| Dropout | 0.20 |
| Activation | ReLU |
| Optimizer | RMSProp |

---

# 16. Computational Complexity

| Component | Complexity |
|-----------|------------|
| Graph Convolution | O(E × F) |
| Daily LSTM | O(T × H²) |
| Hourly LSTM | O(T × H²) |
| Dense Layers | O(N × D) |

Where:

- **E** = Number of graph edges
- **F** = Feature dimension
- **T** = Sequence length
- **H** = Hidden size
- **N** = Number of road segments
- **D** = Hidden dimension

---

# 17. Advantages

- Joint spatial-temporal learning
- Lightweight architecture (22,593 parameters)
- Graph-aware traffic modeling
- Weather feature integration
- End-to-end trainable
- Reproducible within a modern TensorFlow environment

---

# 18. Limitations

- Uses TensorFlow 1.x APIs through `compat.v1`
- Fixed graph structure
- Limited hyperparameter exploration
- Sample dataset for reproduction
- No uncertainty estimation
- CPU-focused reproduction

---

# 19. Future Improvements

Potential enhancements include:

- Graph Attention Networks (GAT)
- GraphSAGE
- Transformer-based temporal modeling
- PyTorch implementation
- TensorFlow 2.x native migration
- Mixed-precision training
- Multi-GPU support
- Hyperparameter optimization
- Model export (ONNX)

---

# Key Takeaways

- The model combines **Graph Convolution** and **LSTM** to capture both spatial and temporal dependencies.
- Training uses **RMSProp** with **MSE** loss, while **MAE** is used for evaluation.
- The reproduced implementation contains **22,593 trainable parameters**, making it compact yet expressive.
- The architecture was successfully reproduced and executed using TensorFlow 2.10 in compatibility mode.

---

# Document Information

| Item | Value |
|------|-------|
| Document | Model Reference |
| Version | 1.0 |
| Status | Complete |
| Author | Rohit |
| Purpose | Technical specification of the GCN-LSTM model implementation |

