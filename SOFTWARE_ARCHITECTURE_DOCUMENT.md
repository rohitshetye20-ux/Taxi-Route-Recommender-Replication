# ==============================================================================
# SOFTWARE ARCHITECTURE DOCUMENT (SAD)
#
# Taxi Route Recommender System
#
# Author  : Rohit Shetye
# Version : 1.0.0
# Date    : July 2026
# License : MIT
# ==============================================================================

# Software Architecture Document (SAD)

## Taxi Route Recommender System

---

# Document Information

| Attribute | Value |
|-----------|--------|
| Project | Taxi Route Recommender System |
| Version | 1.0.0 |
| Author | Rohit Shetye |
| Status | Final |
| Document Type | Software Architecture Document |
| Intended Audience | Developers, Researchers, Reviewers, Interviewers |

---

# 1. Purpose

This document describes the software architecture of the Taxi Route Recommender System.

It explains:

- overall architecture
- major components
- data flow
- design decisions
- deployment model
- quality attributes
- scalability considerations
- security considerations

---

# 2. Project Overview

The project is a research replication of:

> A Cost-Effective Sequential Route Recommender System for Taxi Drivers

The implementation combines:

- Graph Convolutional Networks (GCN)
- Long Short-Term Memory (LSTM)
- Sequential Recommendation
- Deep Learning
- Transportation Analytics

---

# 3. Architectural Goals

The architecture aims to achieve:

- Modularity
- Reproducibility
- Maintainability
- Testability
- Extensibility
- Deployment Readiness
- Research Transparency

---

# 4. High-Level Architecture

```
                  +------------------+
                  |   Raw Dataset    |
                  +------------------+
                           |
                           v
                  +------------------+
                  | Data Processing  |
                  +------------------+
                           |
                           v
                  +------------------+
                  | Feature Builder  |
                  +------------------+
                           |
                           v
                  +------------------+
                  | GCN + LSTM Model |
                  +------------------+
                           |
                           v
                  +------------------+
                  | Model Evaluation |
                  +------------------+
                           |
                           v
                  +------------------+
                  | Prediction Layer |
                  +------------------+
                           |
                           v
                  +------------------+
                  | Reports/Figures  |
                  +------------------+
```

---

# 5. Repository Architecture

```
configs/
data/
docs/
figures/
models/
notebooks/
output/
presentation_builder/
report_builder/
scripts/
src/
tests/
```

Each directory has a clearly defined responsibility.

---

# 6. Component Architecture

## Data Layer

Responsibilities

- Raw datasets
- Processed datasets
- Intermediate files

Input

Taxi trajectory data

Output

Processed tensors

---

## Preprocessing Layer

Responsibilities

- Cleaning
- Feature engineering
- Graph construction
- Sequence generation

---

## Model Layer

Responsibilities

- GCN
- LSTM
- Training
- Inference

---

## Evaluation Layer

Responsibilities

- Metrics
- Benchmarking
- Visualisation

---

## Reporting Layer

Responsibilities

- Figures
- Reports
- Presentation

---

# 7. Data Flow

```
Raw Data
    │
    ▼
Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
Training
    │
    ▼
Evaluation
    │
    ▼
Prediction
    │
    ▼
Report Generation
```

---

# 8. Deployment Architecture

Development

```
Developer
     │
     ▼
Git
     │
     ▼
GitHub
     │
     ▼
GitHub Actions
     │
     ▼
Docker Build
```

Execution

```
Docker Container
        │
        ▼
Python Runtime
        │
        ▼
Pipeline Scripts
        │
        ▼
Outputs
```

---

# 9. Technology Stack

## Programming

- Python 3.10

## Machine Learning

- TensorFlow
- NumPy
- Pandas
- Scikit-learn

## Visualisation

- Matplotlib

## Development

- Git
- GitHub
- Docker
- GitHub Actions

---

# 10. Design Principles

The architecture follows:

- Separation of Concerns
- Single Responsibility Principle
- Modular Design
- Reusable Components
- Configuration over Hardcoding
- Testability

---

# 11. Architectural Decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| ADR-001 | Modular folder structure | Easier maintenance |
| ADR-002 | Separate scripts and source | Clear execution flow |
| ADR-003 | Docker support | Reproducibility |
| ADR-004 | GitHub Actions | Continuous Integration |
| ADR-005 | Configuration-driven execution | Flexibility |
| ADR-006 | Comprehensive testing | Reliability |

---

# 12. Security Considerations

Current measures include:

- No secrets committed
- .gitignore
- .dockerignore
- SECURITY.md
- Dependency isolation
- Controlled Docker environment

Future improvements:

- Secret management
- Dependency scanning
- Static application security testing

---

# 13. Quality Attributes

| Attribute | Approach |
|-----------|----------|
| Maintainability | Modular architecture |
| Reliability | Automated tests |
| Reproducibility | Docker + requirements |
| Portability | Python 3.10 + Docker |
| Scalability | Modular components |
| Extensibility | Layered architecture |

---

# 14. Risks

| Risk | Mitigation |
|------|------------|
| TensorFlow compatibility | Python 3.10 environment |
| Missing datasets | Documentation |
| Dependency conflicts | requirements.txt |
| Reproducibility | Docker support |

---

# 15. Future Architecture

Planned enhancements:

- REST API
- FastAPI deployment
- Real-time inference
- GPU acceleration
- Kubernetes deployment
- Cloud-native architecture
- Experiment tracking
- Model registry

---

# 16. Traceability

| Requirement | Component |
|------------|-----------|
| Data Loading | src/data_loader.py |
| Preprocessing | scripts/preprocess.py |
| Training | scripts/train.py |
| Prediction | scripts/predict.py |
| Evaluation | scripts/evaluate.py |
| Reporting | report_builder/ |

---

# 17. Architecture Diagrams

Refer to the following diagrams in the `docs/` directory:

- Repository Architecture
- Data Pipeline
- Model Architecture
- Training Pipeline
- Inference Pipeline
- Module Dependency Graph

---

# 18. Conclusion

The Taxi Route Recommender System follows a modular and reproducible architecture that bridges academic research with modern software engineering practices.

The architecture emphasizes:

- clarity
- maintainability
- reproducibility
- automation
- extensibility

The result is a repository suitable for research, education, technical interviews, and future development.

---

# Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | July 2026 | Initial architecture document |