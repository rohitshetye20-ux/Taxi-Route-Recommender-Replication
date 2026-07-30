# Frequently Asked Questions (FAQ)

> **Purpose:** This document answers the most common questions about the GCN-LSTM Taxi Route Recommendation project, including repository setup, dataset preparation, model execution, troubleshooting, and reproducibility.

---

# Table of Contents

1. General Questions
2. Environment Setup
3. Dataset Questions
4. Model Questions
5. Training Questions
6. Troubleshooting
7. Performance Questions
8. Repository Questions
9. Future Development

---

# 1. General Questions

---

## Q1. What is the purpose of this repository?

This repository reproduces the experiments from the research paper:

> **A Cost-Effective Sequential Route Recommender System for Taxi Drivers**

The project demonstrates how Graph Convolution Networks (GCNs) and Long Short-Term Memory (LSTM) networks can jointly model spatial and temporal traffic patterns for taxi route recommendation.

---

## Q2. Is this the original implementation?

No.

This repository is an engineering-focused reproduction of the original implementation, including:

- Environment modernization
- Dataset reconstruction
- Dependency compatibility updates
- Comprehensive documentation
- Reproducibility improvements

---

## Q3. What programming language is used?

Python.

---

## Q4. Which deep learning framework is used?

TensorFlow 2.10 using the `compat.v1` compatibility layer to execute TensorFlow 1.x style code.

---

# 2. Environment Setup

---

## Q5. Which Python version should I use?

Recommended:

```
Python 3.10
```

Later versions may introduce compatibility issues with TensorFlow 2.10.

---

## Q6. Why doesn't TensorFlow 1.x work?

TensorFlow 1.x is no longer maintained and is difficult to install on modern Python versions.

This reproduction uses TensorFlow 2.10 with `tf.compat.v1` to preserve the original behavior.

---

## Q7. Should I use a virtual environment?

Yes.

Example:

```bash
python -m venv taxi_tf_env
```

This keeps project dependencies isolated from other Python projects.

---

# 3. Dataset Questions

---

## Q8. Why is `sample_input.npy` missing?

The original repository references `sample_input.npy`, but it is not included.

Instead, the repository provides sparse matrices that can be reconstructed into the required file.

---

## Q9. How do I recreate `sample_input.npy`?

1. Load the provided sparse matrices:

```
sample_last_dim_0.npz

sample_last_dim_1.npz

sample_last_dim_2.npz
```

2. Convert them to dense arrays.

3. Stack them along the last dimension.

4. Save the output as:

```
sample_input.npy
```

---

## Q10. How large is the reconstructed dataset?

Approximately:

```
386 MB
```

Shape:

```
(408, 82688, 3)
```

---

# 4. Model Questions

---

## Q11. What does the model predict?

The model predicts normalized future traffic demand for each road segment in the road network.

---

## Q12. Why combine GCN and LSTM?

Each component captures different information:

| Component | Purpose |
|-----------|----------|
| GCN | Spatial relationships between roads |
| Daily LSTM | Long-term temporal patterns |
| Hourly LSTM | Short-term temporal patterns |

---

## Q13. How many trainable parameters does the model have?

```
22,593
```

---

## Q14. Which optimizer is used?

RMSProp.

---

## Q15. Which loss function is used?

Training minimizes Mean Squared Error (MSE).

Evaluation reports Mean Absolute Error (MAE).

---

# 5. Training Questions

---

## Q16. How long does training take?

Training time depends on:

- CPU/GPU
- Dataset size
- Number of epochs

The sample experiment completes quickly on a standard CPU.

---

## Q17. What evaluation metric is reported?

Mean Absolute Error (MAE).

Example from this reproduction:

```
Test MAE ≈ 0.08384
```

---

## Q18. Does the project support GPU training?

The code can run on systems with compatible TensorFlow GPU installations, although this reproduction was validated on CPU.

---

# 6. Troubleshooting

---

## Q19. I get:

```
ModuleNotFoundError
```

### Solution

Verify:

- Virtual environment is activated
- Required packages are installed
- Current working directory is correct

---

## Q20. I get:

```
FileNotFoundError

sample_input.npy
```

### Solution

Reconstruct the missing dataset or verify its location.

---

## Q21. I get:

```
No module named
scipy.sparse.linalg.eigen.arpack
```

### Solution

Update the import to:

```python
from scipy.sparse.linalg import eigsh
```

---

## Q22. TensorFlow prints deprecation warnings.

Is that normal?

Yes.

The repository relies on TensorFlow 1.x APIs executed through TensorFlow 2.x compatibility mode.

Warnings do not necessarily indicate incorrect execution.

---

## Q23. The notebook cannot locate project files.

### Solution

Verify the working directory:

```python
import os

print(os.getcwd())
```

Ensure it points to the repository's `script` directory before importing project modules.

---

# 7. Performance Questions

---

## Q24. Is the reproduced MAE expected to match the paper exactly?

Not necessarily.

Small differences may arise from:

- Dependency versions
- Random initialization
- Numerical precision
- Hardware differences
- Sample versus full dataset

---

## Q25. Why are predictions limited to a smaller range than labels?

The reproduced experiment uses the sample dataset and a limited training configuration.

Predictions often remain conservative during early training and may not span the full label range.

---

# 8. Repository Questions

---

## Q26. Which notebook should I run?

```
Final_Experiment_Reproduction.ipynb
```

This notebook reproduces the complete experimental workflow.

---

## Q27. Where can I find the architecture explanation?

See:

```
docs/Architecture.md

docs/Code_Architecture.md

docs/Model_Reference.md
```

---

## Q28. Where are the experiment results documented?

See:

```
docs/Experiment.md

docs/Experiment_Log.md

docs/Performance_Analysis.md
```

---

## Q29. How can I reproduce the experiments?

Follow the steps in:

```
docs/Reproducibility_Guide.md
```

---

# 9. Future Development

---

## Q30. Can this project be upgraded?

Yes.

Potential improvements include:

- Native TensorFlow 2.x implementation
- PyTorch implementation
- Graph Attention Networks (GAT)
- Transformer-based temporal models
- Experiment tracking
- Docker support
- REST API deployment
- Cloud-based inference

---

## Q31. Can this repository be used for learning?

Yes.

The project is suitable for studying:

- Graph Neural Networks
- Time-series forecasting
- TensorFlow compatibility
- Research reproduction
- Machine Learning engineering
- Experiment reproducibility

---

## Q32. Can I contribute?

Contributions are welcome.

Suggested areas include:

- Documentation improvements
- Bug fixes
- Performance optimization
- TensorFlow 2.x migration
- Additional experiments
- Unit tests
- Visualization enhancements

Please include clear descriptions and reproducible changes with any contribution.

---

# Quick Reference

| Question | Answer |
|----------|--------|
| Python Version | 3.10 |
| Framework | TensorFlow 2.10 (`compat.v1`) |
| Model | GCN + Daily LSTM + Hourly LSTM |
| Optimizer | RMSProp |
| Loss | Mean Squared Error |
| Evaluation Metric | Mean Absolute Error |
| Trainable Parameters | 22,593 |
| Sample Dataset Size | ~386 MB |
| Main Notebook | `Final_Experiment_Reproduction.ipynb` |

---

# Additional Documentation

For more details, refer to:

- `README.md`
- `Project_Overview.md`
- `Repository_Guide.md`
- `Reproducibility_Guide.md`
- `Architecture.md`
- `Code_Architecture.md`
- `API_Reference.md`
- `Model_Reference.md`
- `Performance_Analysis.md`
- `Experiment_Log.md`
- `Future_Work.md`

---

# Document Information

| Item | Value |
|------|-------|
| Document | Frequently Asked Questions (FAQ) |
| Version | 1.0 |
| Status | Complete |
| Author | Rohit |
| Purpose | Answer common questions about the repository, experiments, and reproduction process |

