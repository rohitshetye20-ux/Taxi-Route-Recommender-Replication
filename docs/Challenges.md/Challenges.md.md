# Engineering Challenges & Solutions

## Project

**Reproduction of "A Cost-Effective Sequential Route Recommender System for Taxi Drivers"**

---

# Table of Contents

1. Introduction
2. Environment Challenges
3. Dependency Challenges
4. Repository Challenges
5. Dataset Challenges
6. Model Challenges
7. Training Challenges
8. Lessons from Debugging
9. Summary

---

# 1. Introduction

Reproducing legacy research repositories is significantly more challenging than training modern machine learning models. Although the official implementation was publicly available, several issues prevented immediate execution.

This document records the major engineering challenges encountered during the reproduction process, the investigation performed to identify each root cause, and the implemented solutions.

---

# 2. Environment Challenges

---

## Challenge 1 — Unsupported Python Version

### Problem

The project failed to execute using Python 3.13.

### Root Cause

TensorFlow 2.10, the final TensorFlow release supporting TensorFlow 1.x compatibility mode, does not support Python 3.13.

### Investigation

Importing TensorFlow produced module compatibility errors.

### Solution

Installed Python 3.10 and created an isolated virtual environment.

```
Python 3.10

Virtual Environment

taxi_tf_env
```

### Lesson Learned

Legacy research code frequently depends on older Python versions.

---

## Challenge 2 — TensorFlow Import Failure

### Problem

```
ModuleNotFoundError

No module named tensorflow
```

### Root Cause

TensorFlow had not been installed inside the virtual environment.

### Solution

Installed

```
tensorflow==2.10.1
```

and verified the active Jupyter kernel used the same environment.

### Lesson Learned

Always verify the Python interpreter used by Jupyter.

---

# 3. Dependency Challenges

---

## Challenge 3 — NumPy Compatibility

### Problem

```
_ARRAY_API not found
```

```
numpy.core.umath failed to import
```

### Root Cause

TensorFlow 2.10 was compiled against NumPy 1.x while the environment contained NumPy 2.x.

### Solution

Downgraded

```
NumPy

2.x

↓

1.23.5
```

### Lesson Learned

Binary compatibility is critical for compiled scientific libraries.

---

## Challenge 4 — SciPy Import Error

### Problem

```
ModuleNotFoundError

scipy.sparse.linalg.eigen.arpack
```

### Root Cause

The import path used by the repository was removed in newer SciPy releases.

### Solution

Installed a compatible SciPy version and updated imports where required.

### Lesson Learned

Scientific libraries evolve and older import paths may no longer exist.

---

# 4. Repository Challenges

---

## Challenge 5 — Module Import Failure

### Problem

```
ModuleNotFoundError

myutil
```

### Root Cause

The repository's script directory was not present in the Python path.

### Solution

Added

```
script/
```

to

```
sys.path
```

before importing project modules.

### Lesson Learned

Research repositories often assume execution from a specific working directory.

---

## Challenge 6 — Relative Path Issues

### Problem

```
FileNotFoundError

sample_input.npy
```

### Root Cause

The repository uses relative paths.

```
../data/
```

which depend on the current working directory.

### Investigation

Verified

```
os.getcwd()
```

and changed into the expected repository location.

### Solution

Executed notebooks from the repository root before importing modules.

### Lesson Learned

Relative paths are a common source of reproducibility issues.

---

# 5. Dataset Challenges

---

## Challenge 7 — Missing Dataset

### Problem

The repository expected

```
sample_input.npy
```

which was not included.

### Root Cause

Only sparse matrices were distributed.

```
sample_last_dim_0.npz

sample_last_dim_1.npz

sample_last_dim_2.npz
```

### Investigation

Reviewed the README and inspected the data directory.

### Solution

Reconstructed

```
sample_input.npy
```

by stacking the sparse matrices into a dense tensor.

Result

```
Shape

(408, 82688, 3)
```

### Lesson Learned

Missing intermediate datasets are common in academic repositories.

---

## Challenge 8 — Working Directory Validation

### Problem

Even after reconstruction, the dataset could not be located.

### Root Cause

The notebook executed from an unexpected directory.

### Solution

Changed the working directory before loading data.

### Lesson Learned

Always validate

```
os.getcwd()
```

when reproducing experiments.

---

# 6. Model Challenges

---

## Challenge 9 — Constructor Mismatch

### Problem

```
unexpected keyword argument
mode
```

### Root Cause

The model constructor differed from assumptions made during notebook development.

### Investigation

Used

```
inspect.signature()
```

to determine the correct parameters.

### Solution

Updated the model initialization accordingly.

### Lesson Learned

Inspect the actual implementation rather than relying solely on documentation.

---

## Challenge 10 — Deprecated TensorFlow APIs

### Problem

Warnings related to

```
dynamic_rnn

RMSProp

Ones()
```

### Root Cause

The repository relies on TensorFlow 1.x APIs.

### Solution

Executed using

```
tensorflow.compat.v1
```

### Lesson Learned

Warnings are not always failures but should be documented.

---

# 7. Training Challenges

---

## Challenge 11 — Feed Dictionary Construction

### Problem

Training required manually constructing TensorFlow feed dictionaries.

### Investigation

Examined the

```
train_test()
```

implementation.

### Solution

Used the project's helper functions exactly as intended.

### Lesson Learned

Understanding the training pipeline is essential for successful reproduction.

---

## Challenge 12 — Parameter Inspection

### Problem

Modern TensorFlow objects differed from older examples.

```
.value
```

caused errors.

### Solution

Updated parameter counting logic to use native integer dimensions.

### Lesson Learned

Framework APIs evolve over time.

---

# 8. Lessons from Debugging

The reproduction process emphasized several engineering principles.

- Carefully read repository documentation before execution.
- Verify environment compatibility.
- Maintain isolated virtual environments.
- Validate working directories.
- Inspect source code when documentation is incomplete.
- Reconstruct missing datasets rather than bypassing errors.
- Record every fix to improve reproducibility.

---

# 9. Summary

The experiment was successfully reproduced after resolving challenges related to:

| Category | Status |
|-----------|--------|
| Python Compatibility | ✅ |
| TensorFlow Installation | ✅ |
| NumPy Compatibility | ✅ |
| SciPy Compatibility | ✅ |
| Repository Imports | ✅ |
| Dataset Reconstruction | ✅ |
| Relative Paths | ✅ |
| Model Initialization | ✅ |
| Training Pipeline | ✅ |
| Evaluation | ✅ |

The successful resolution of these issues resulted in a fully reproducible execution environment capable of training and evaluating the original GCN-LSTM implementation on the released sample dataset.
