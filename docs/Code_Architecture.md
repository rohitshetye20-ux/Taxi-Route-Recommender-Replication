# Code Architecture

> **Purpose:** This document describes the software architecture of the GCN-LSTM Taxi Route Recommendation system, explaining the responsibilities of each module, the interaction between components, and the complete execution flow from data loading to prediction.

---

# Table of Contents

1. Architecture Overview
2. Repository Layers
3. Core Modules
4. Execution Flow
5. Class Architecture
6. Function Architecture
7. Data Flow
8. TensorFlow Computational Graph
9. Design Decisions
10. Extension Points
11. Summary

---

# 1. Architecture Overview

The project follows a layered architecture that separates data processing, graph operations, neural network construction, training, and evaluation.

```
                    User / Notebook
                           │
                           ▼
              Final_Experiment_Reproduction.ipynb
                           │
                           ▼
                   gcn_lstm_split.py
                           │
      ┌────────────────────┼────────────────────┐
      │                    │                    │
      ▼                    ▼                    ▼
   myutil.py          gcn/utils.py       gcn/layers.py
      │                    │                    │
      └────────────────────┼────────────────────┘
                           ▼
                   TensorFlow Graph
                           ▼
                    Training Engine
                           ▼
                    Prediction Engine
                           ▼
                      Evaluation
```

The notebook orchestrates the workflow, while `gcn_lstm_split.py` serves as the central controller coordinating data loading, model creation, training, and evaluation.

---

# 2. Repository Layers

## Presentation Layer

**Purpose**

Provides the interface used to execute experiments.

**Components**

- Final_Experiment_Reproduction.ipynb
- README.md
- Documentation

Responsibilities:

- Run experiments
- Display outputs
- Visualize results
- Explain implementation

---

## Application Layer

Main execution logic.

Primary module:

```
gcn_lstm_split.py
```

Responsibilities:

- Load data
- Build model
- Execute training
- Perform inference
- Calculate loss
- Generate predictions

---

## Utility Layer

Contains helper modules.

```
myutil.py
```

Responsibilities:

- Dataset loading
- Time slicing
- Weather feature preparation
- Preprocessing

```
gcn/utils.py
```

Responsibilities:

- Feed dictionary creation
- Graph preprocessing
- Sparse matrix utilities

---

## Model Layer

```
gcn/layers.py
```

Responsibilities:

- Graph Convolution Layer
- Weight initialization
- Forward propagation

---

## Framework Layer

TensorFlow 2.10 (compat.v1)

Responsibilities:

- Computational graph
- Session execution
- Optimizer
- Variables
- Placeholders

---

# 3. Core Modules

## gcn_lstm_split.py

The primary module of the repository.

Major responsibilities:

- Dataset preparation
- Model construction
- Training loop
- Validation
- Prediction
- Performance evaluation

Important elements:

```
get_data()

GCNLSTM_SPLIT

train_test()
```

---

## myutil.py

Provides reusable preprocessing utilities.

Typical operations:

- Data normalization
- Time window generation
- Feature preparation
- Dataset partitioning

---

## gcn/utils.py

Contains graph-related helper functions.

Examples:

```
construct_feed_dict()

preprocess_adj()

normalize_adj()
```

---

## gcn/layers.py

Defines Graph Convolution layers.

Responsibilities:

- Graph propagation
- Weight multiplication
- Activation
- Dropout

---

# 4. Execution Flow

The complete execution sequence is shown below.

```
Notebook

↓

Load Dataset

↓

Preprocess Data

↓

Construct Graph

↓

Initialize Model

↓

Build TensorFlow Graph

↓

Train Model

↓

Validate

↓

Predict

↓

Evaluate MAE
```

---

# 5. Class Architecture

## GCNLSTM_SPLIT

The central class responsible for constructing the neural network.

### Inputs

```
Traffic Features

Weather Features

Adjacency Matrix
```

### Internal Components

```
Graph Convolution

↓

Daily LSTM

↓

Hourly LSTM

↓

Concatenation

↓

Dense Layers

↓

Prediction
```

### Outputs

```
Predicted Traffic Demand
```

---

# 6. Function Architecture

## get_data()

Purpose

Loads and prepares the dataset.

Inputs

- ratios
- interested_clocks
- prior_days
- prior_hours
- usesample

Returns

Dictionary containing:

```
train_x_day

train_x_hour

train_y

validation

test

adjacency matrix
```

---

## GCNLSTM_SPLIT.__init__()

Purpose

Constructs the complete neural network.

Major tasks

- Create placeholders
- Build GCN
- Build LSTM
- Create dense layers
- Define optimizer
- Define loss

---

## train_test()

Purpose

Executes model training and evaluation.

Workflow

```
Initialize Session

↓

Initialize Variables

↓

Construct Feed Dictionary

↓

Training Loop

↓

Validation

↓

Early Stopping

↓

Prediction

↓

MAE Calculation
```

Returns

```
Predictions

Labels

MAE

Training Loss

Validation Loss
```

---

## construct_feed_dict()

Purpose

Maps NumPy arrays to TensorFlow placeholders.

Provides:

- Daily traffic tensor
- Hourly traffic tensor
- Weather tensors
- Labels
- Adjacency matrix

---

# 7. Data Flow

The following illustrates how data moves through the system.

```
Sparse Matrices

↓

sample_input.npy

↓

get_data()

↓

Train / Validation / Test

↓

Feed Dictionary

↓

GCN

↓

LSTM

↓

Dense Layers

↓

Predictions

↓

MAE
```

---

# 8. TensorFlow Computational Graph

The project uses TensorFlow's graph execution model.

```
Placeholders

↓

Graph Convolution

↓

LSTM

↓

Dense

↓

Loss

↓

Optimizer

↓

Train Operation
```

Primary TensorFlow components:

- Placeholders
- Variables
- Session
- RMSProp Optimizer
- Dynamic RNN
- Computational Graph

---

# 9. Design Decisions

The implementation adopts several important architectural choices.

### Modular Design

Each module performs a single responsibility.

### Separation of Concerns

Data loading is isolated from model construction and evaluation.

### Graph-Based Learning

Road segments are modeled as graph nodes, enabling spatial relationship learning.

### Temporal Modeling

Separate LSTM components capture daily and hourly traffic patterns.

### Compatibility Layer

TensorFlow 2.10 executes the original TensorFlow 1.x implementation through `compat.v1`, preserving the original model behavior.

---

# 10. Extension Points

Potential enhancements include:

- Replace Graph Convolution with Graph Attention Networks (GAT)
- Replace LSTM with Transformer-based sequence models
- Add experiment tracking (e.g., MLflow)
- Implement configurable YAML/JSON-based hyperparameters
- Export trained models using ONNX
- Provide a REST API for inference
- Containerize the project with Docker

---

# 11. Summary

The repository follows a layered, modular architecture:

- **Presentation Layer** manages notebooks and documentation.
- **Application Layer** orchestrates the end-to-end workflow.
- **Utility Layer** handles preprocessing and graph utilities.
- **Model Layer** implements Graph Convolution and sequence learning.
- **Framework Layer** executes the computational graph using TensorFlow.

This separation improves maintainability, readability, and reproducibility while preserving the structure of the original research implementation.

---

# Document Information

| Item | Value |
|------|-------|
| Document | Code Architecture |
| Version | 1.0 |
| Status | Complete |
| Author | Rohit |
| Purpose | Describe the internal software architecture and execution flow |

