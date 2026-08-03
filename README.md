# 🚖 Taxi Route Recommender System
### Research Replication of *A Cost-Effective Sequential Route Recommender System for Taxi Drivers*

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Research](https://img.shields.io/badge/Research-Replication-success)
![Version](https://img.shields.io/badge/Version-2.0-blueviolet)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

> **A research-oriented implementation and comprehensive replication of the paper**
>
> **"A Cost-Effective Sequential Route Recommender System for Taxi Drivers"**
>
> This repository reproduces the original research methodology using **Graph Convolutional Networks (GCN)** and **Long Short-Term Memory (LSTM)** models while following modern software engineering practices, reproducible research principles, and enterprise-grade project documentation.

---

# 📖 Project Overview

Finding profitable taxi routes is a complex sequential decision-making problem that depends on traffic conditions, passenger demand, road connectivity, and historical driving patterns.

This project reproduces the methodology proposed in the research paper **"A Cost-Effective Sequential Route Recommender System for Taxi Drivers"** by implementing a deep learning pipeline based on **Graph Convolutional Networks (GCN)** and **Long Short-Term Memory (LSTM)** networks.

Beyond reproducing the published work, this repository extends the project with professional software engineering practices including structured documentation, automated testing, continuous integration, Docker support, software architecture documentation, and reproducible development workflows.

---

# 🎯 Project Objectives

The primary objectives of this repository are to:

- Reproduce the results presented in the original research paper.
- Understand and document every component of the GCN-LSTM architecture.
- Provide a well-structured implementation suitable for academic study.
- Establish a reproducible experimental environment.
- Demonstrate modern software engineering practices for machine learning research.
- Create a portfolio-quality repository for researchers, students, and employers.

---

# ⭐ Key Features

- Graph Convolutional Network (GCN) implementation
- Long Short-Term Memory (LSTM) sequential modeling
- Taxi route recommendation pipeline
- Data preprocessing workflow
- Model training pipeline
- Inference pipeline
- Automated testing framework
- GitHub Actions Continuous Integration
- Docker-based deployment
- Comprehensive project documentation
- Software Architecture Document (SAD)
- Research replication methodology
- Professional repository structure

---

# 🏆 Repository Highlights

| Feature | Status |
|----------|:------:|
| Research Paper Replication | ✅ |
| Complete Source Code | ✅ |
| Professional Documentation | ✅ |
| Software Architecture | ✅ |
| Docker Support | ✅ |
| GitHub Actions CI | ✅ |
| Automated Testing | ✅ |
| Project Portfolio | ✅ |
| Enterprise Project Structure | ✅ |
| Open Source | ✅ |

---

# 👨‍💻 Author

**Rohit Shetye**

Machine Learning • Data Analytics • Software Engineering • Research Reproduction

---

> **Project Vision**
>
> Develop a high-quality, reproducible research implementation that bridges academic machine learning research with professional software engineering practices, enabling students, researchers, and practitioners to understand, reproduce, and extend the original taxi route recommendation system.

---

# 📑 Table of Contents

- [📖 Project Overview](#-project-overview)
- [🎯 Project Objectives](#-project-objectives)
- [⭐ Key Features](#-key-features)
- [🏆 Repository Highlights](#-repository-highlights)
- [📑 Table of Contents](#-table-of-contents)
- [🗂 Repository Architecture](#-repository-architecture)
- [📁 Project Structure](#-project-structure)
- [🛠 Technology Stack](#-technology-stack)
- [📚 Documentation Index](#-documentation-index)
- [🧠 System Architecture](#-system-architecture)
- [📊 Data Pipeline](#-data-pipeline)
- [🤖 Model Architecture](#-model-architecture)
- [⚙️ Installation](#️-installation)
- [🚀 Quick Start](#-quick-start)
- [🐳 Docker Deployment](#-docker-deployment)
- [🧪 Testing](#-testing)
- [🔄 Continuous Integration](#-continuous-integration)
- [📈 Experimental Results](#-experimental-results)
- [🛣 Roadmap](#-roadmap)
- [📖 Citation](#-citation)
- [📄 License](#-license)
- [👨‍💻 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

# 🗂 Repository Architecture

The repository is organized using a modular, research-oriented structure that separates source code, datasets, documentation, tests, automation, and deployment resources.

```
Taxi-Route-Recommender-Replication
│
├── .github/                 # GitHub Actions, issue templates, workflows
├── data/                    # Datasets and sample inputs
├── docs/                    # Architecture documents and project reports
├── scripts/                 # Research scripts and utility programs
├── src/                     # Core implementation
├── tests/                   # Automated unit tests
├── docker/                  # Docker configuration (if used)
│
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── .gitignore
```

---

# 📁 Project Structure

| Directory | Purpose |
|-----------|---------|
| `.github/` | GitHub Actions workflows, issue templates, repository automation |
| `data/` | Input datasets, processed data, adjacency matrices, sample files |
| `docs/` | Research documentation, architecture diagrams, reports, project portfolio |
| `scripts/` | Data preprocessing, model execution, training, inference, utility scripts |
| `src/` | Core machine learning implementation |
| `tests/` | Unit tests and validation scripts |
| `docker/` | Containerization resources (if applicable) |
| Root configuration | Project configuration, dependency management, CI/CD, Docker, licensing |

---

# 🛠 Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python 3.10 |
| Deep Learning | TensorFlow, Keras |
| Graph Learning | Graph Convolutional Network (GCN) |
| Sequence Learning | Long Short-Term Memory (LSTM) |
| Data Processing | NumPy, Pandas, SciPy |
| Graph Processing | NetworkX |
| Visualization | Matplotlib |
| Development Environment | Jupyter Notebook, JupyterLab |
| Testing | Pytest, Pytest-Cov |
| Code Quality | Black, Ruff, isort |
| Continuous Integration | GitHub Actions |
| Containerization | Docker, Docker Compose |
| Version Control | Git, GitHub |

---

# 📚 Documentation Index

The repository contains comprehensive documentation to support both research replication and software engineering practices.

| Document | Description |
|----------|-------------|
| README.md | Repository overview and usage guide |
| Software Architecture Document (SAD) | Complete architectural design and implementation details |
| Project Portfolio | End-to-end project documentation and deliverables |
| Research Reports | Analysis and replication findings |
| Architecture Diagrams | System, training, inference, and module dependency diagrams |
| Testing Documentation | Test strategy and validation approach |
| Docker Documentation | Containerized deployment instructions |
| CI/CD Documentation | Continuous Integration workflow and automation |

---

# 📌 Repository Design Principles

This repository follows the following engineering principles:

- Modular project organization
- Reproducible machine learning experiments
- Research transparency
- Comprehensive documentation
- Automated testing
- Continuous Integration
- Containerized deployment
- Maintainable and scalable codebase
- Version-controlled development workflow

---

# 🧠 System Architecture

The Taxi Route Recommender System follows a modular machine learning architecture that transforms historical taxi trajectory data into profitable route recommendations using a combination of **Graph Convolutional Networks (GCN)** and **Long Short-Term Memory (LSTM)** networks.

The overall workflow consists of five major stages:

1. Data Collection & Preprocessing
2. Graph Construction
3. Feature Learning using GCN
4. Sequential Route Learning using LSTM
5. Route Recommendation & Evaluation

The modular design allows each component to be developed, tested, and maintained independently while ensuring reproducible research outcomes.

---

## 🏗 Overall System Architecture

The complete system architecture is illustrated below.

> 📌 **Architecture Diagram**
>
> **Location:** `docs/figures/Figure_01_Repository_Architecture.png`

The architecture demonstrates the interaction between datasets, preprocessing modules, graph learning components, sequential models, inference pipeline, and evaluation modules.

---

# 📊 Data Pipeline

The data pipeline prepares raw taxi trajectory data for machine learning by performing cleaning, transformation, graph generation, and feature engineering.

### Pipeline Stages

```
Raw Taxi Data
      │
      ▼
Data Cleaning
      │
      ▼
Trajectory Processing
      │
      ▼
Road Network Graph Construction
      │
      ▼
Feature Engineering
      │
      ▼
Training Dataset
```

### Key Responsibilities

- Import historical taxi trajectory data
- Handle missing or inconsistent records
- Generate road network graphs
- Build adjacency matrices
- Create node and edge features
- Normalize numerical features
- Produce model-ready datasets

---

### 📌 Data Pipeline Diagram

**Location:**

```
docs/figures/Figure_02_Data_Pipeline.png
```

---

# 🤖 GCN–LSTM Model Architecture

The learning model combines two complementary neural network architectures.

## Graph Convolutional Network (GCN)

The GCN learns spatial relationships between road segments by propagating information through the road network graph.

Responsibilities include:

- Learning road connectivity
- Capturing spatial dependencies
- Encoding node representations
- Aggregating neighborhood information

---

## Long Short-Term Memory (LSTM)

The LSTM models temporal driving behaviour by learning sequential movement patterns.

Responsibilities include:

- Learning historical trajectories
- Capturing temporal dependencies
- Predicting future route sequences
- Preserving long-term contextual information

---

### Combined Architecture

```
Road Graph
      │
      ▼
Graph Convolution Network
      │
Spatial Embeddings
      │
      ▼
LSTM Network
      │
Temporal Features
      │
      ▼
Dense Layers
      │
      ▼
Recommended Route
```

---

### 📌 Model Architecture Diagram

**Location**

```
docs/figures/Figure_03_Model_Architecture.png
```

---

# 🎓 Training Pipeline

The training pipeline converts processed datasets into a trained route recommendation model.

### Training Workflow

```
Training Dataset
        │
        ▼
Feature Extraction
        │
        ▼
GCN Training
        │
        ▼
LSTM Training
        │
        ▼
Loss Optimization
        │
        ▼
Model Validation
        │
        ▼
Saved Model
```

---

### Training Activities

- Data loading
- Batch generation
- Forward propagation
- Loss computation
- Backpropagation
- Weight optimization
- Validation
- Checkpoint generation

---

### 📌 Training Pipeline Diagram

```
docs/figures/Figure_04_Training_Pipeline.png
```

---

# 🚖 Inference Pipeline

Once trained, the model predicts profitable routes for incoming taxi trajectories.

### Inference Workflow

```
Input Route
      │
      ▼
Feature Extraction
      │
      ▼
GCN Embedding
      │
      ▼
LSTM Prediction
      │
      ▼
Route Scoring
      │
      ▼
Best Route Recommendation
```

---

### Inference Responsibilities

- Load trained model
- Extract graph features
- Generate node embeddings
- Predict future route sequence
- Score candidate routes
- Return highest-ranked recommendation

---

### 📌 Inference Pipeline Diagram

```
docs/figures/Figure_05_Inference_Pipeline.png
```

---

# 🔄 End-to-End Workflow

The complete lifecycle of the recommendation system is summarized below.

```
Historical Taxi Data
        │
        ▼
Preprocessing
        │
        ▼
Road Graph Construction
        │
        ▼
Feature Engineering
        │
        ▼
GCN Spatial Learning
        │
        ▼
LSTM Sequential Learning
        │
        ▼
Model Training
        │
        ▼
Inference
        │
        ▼
Recommended Taxi Route
```

---

# 🏛 Design Principles

The system architecture follows several software engineering and machine learning best practices.

| Principle | Description |
|-----------|-------------|
| Modularity | Independent components for preprocessing, training, inference, and evaluation |
| Reproducibility | Deterministic workflows with documented dependencies |
| Scalability | Modular architecture supports future model enhancements |
| Maintainability | Clear separation of responsibilities across packages |
| Extensibility | New models and datasets can be integrated with minimal changes |
| Testability | Components can be validated individually through automated tests |
| Research Transparency | Every major processing stage is documented and reproducible |

---

# 📂 Related Architecture Documentation

For additional architectural details, refer to:

| Document | Purpose |
|----------|---------|
| Software Architecture Document (SAD) | Complete architectural specification |
| Project Portfolio | End-to-end project documentation |
| Repository Architecture Figure | High-level repository organization |
| Data Pipeline Figure | Data processing workflow |
| Model Architecture Figure | GCN–LSTM architecture |
| Training Pipeline Figure | Model training workflow |
| Inference Pipeline Figure | Route prediction workflow |

---

# ⚙️ Installation

This section provides step-by-step instructions for setting up the Taxi Route Recommender System on Windows, Linux, or macOS.

---

# 📋 Prerequisites

Before installing the project, ensure the following software is available on your system.

| Software | Version |
|----------|----------|
| Python | 3.10.x |
| Git | Latest |
| pip | Latest |
| Docker *(Optional)* | Latest |
| Docker Compose *(Optional)* | Latest |

---

# 📥 Clone the Repository

```bash
git clone https://github.com/rohitshetye20-ux/Taxi-Route-Recommender-Replication.git

cd Taxi-Route-Recommender-Replication
```

---

# 🐍 Create a Virtual Environment

Creating a dedicated virtual environment is strongly recommended.

## Windows

```powershell
python -m venv venv

venv\Scripts\activate
```

---

## Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

# 📦 Install Dependencies

Upgrade pip first.

```bash
python -m pip install --upgrade pip
```

Install all required packages.

```bash
pip install -r requirements.txt
```

---

# ✅ Verify Installation

Check the Python version.

```bash
python --version
```

Expected output:

```text
Python 3.10.x
```

Verify TensorFlow installation.

```bash
python -c "import tensorflow as tf; print(tf.__version__)"
```

Expected output:

```text
2.10.1
```

---

# 🚀 Quick Start

After installation, you can begin exploring the repository.

## Repository Overview

```text
Taxi-Route-Recommender-Replication
│
├── data/
├── docs/
├── scripts/
├── src/
├── tests/
├── README.md
└── requirements.txt
```

---

# ▶ Running the Project

Depending on your objective, execute the appropriate script.

## Data Preprocessing

```bash
python scripts/preprocessing.py
```

---

## Model Training

```bash
python scripts/train.py
```

---

## Model Inference

```bash
python scripts/inference.py
```

---

## Run Automated Tests

```bash
python -m pytest tests/
```

---

## Generate Test Coverage

```bash
python -m pytest --cov=src tests/
```

---

# 🐳 Docker Deployment

The repository includes Docker support for creating a reproducible execution environment.

## Build Docker Image

```bash
docker build -t taxi-route-recommender .
```

---

## Run Docker Container

```bash
docker run -it taxi-route-recommender
```

---

## Docker Compose

Start the application.

```bash
docker-compose up --build
```

Run in detached mode.

```bash
docker-compose up -d
```

Stop containers.

```bash
docker-compose down
```

---

# 🧪 Development Workflow

Recommended workflow for contributors and researchers.

```
Clone Repository
        │
        ▼
Create Virtual Environment
        │
        ▼
Install Dependencies
        │
        ▼
Run Tests
        │
        ▼
Develop Features
        │
        ▼
Run CI Checks Locally
        │
        ▼
Commit Changes
        │
        ▼
Push to GitHub
```

---

# 🔄 Updating Dependencies

To upgrade installed packages:

```bash
pip install --upgrade -r requirements.txt
```

To install development tools:

```bash
pip install -e ".[dev]"
```

---

# 🛠 Common Commands

| Task | Command |
|------|---------|
| Install dependencies | `pip install -r requirements.txt` |
| Run tests | `python -m pytest tests/` |
| Generate coverage | `python -m pytest --cov=src tests/` |
| Compile source | `python -m compileall src` |
| Build Docker image | `docker build -t taxi-route-recommender .` |
| Start Docker Compose | `docker-compose up --build` |

---

# 🚨 Troubleshooting

## Virtual Environment Not Activated

Verify the environment is active before installing packages.

---

## TensorFlow Installation Issues

Confirm that you are using **Python 3.10**, which is the supported version for this project.

---

## Missing Dependencies

Reinstall all packages.

```bash
pip install -r requirements.txt
```

---

## Test Failures

Run the complete test suite.

```bash
python -m pytest tests/
```

---

# 💡 Recommended Development Environment

The project has been developed and validated using the following environment.

| Component | Version |
|----------|----------|
| Operating System | Windows 11 |
| Python | 3.10 |
| TensorFlow | 2.10.1 |
| JupyterLab | 4.x |
| Git | Latest |
| Docker | Latest |

---

# 📌 Next Steps

After successfully installing the project:

1. Explore the repository structure.
2. Review the architecture documentation.
3. Examine the data preprocessing pipeline.
4. Train the GCN–LSTM model.
5. Evaluate the generated route recommendations.
6. Review the experimental results.


# 🧪 Testing, Validation & Research Reproducibility

The Taxi Route Recommender System has been organized to encourage reproducible machine learning research. Testing is performed at multiple levels to verify implementation correctness, ensure code quality, and support reliable experimentation.

---

# 🎯 Testing Objectives

The testing strategy is designed to:

- Validate preprocessing utilities
- Verify graph construction modules
- Confirm model component functionality
- Detect regression issues during development
- Support Continuous Integration (CI)
- Improve research reproducibility

---

# 📂 Test Organization

The repository follows a dedicated testing structure.

```
tests/
│
├── __init__.py
├── test_data_processing.py
├── test_graph.py
├── test_model.py
├── test_training.py
├── test_inference.py
├── test_utils.py
└── ...
```

> **Note:** The exact test files should reflect the contents of the `tests/` directory in this repository.

---

# ▶ Running the Complete Test Suite

Execute all automated tests.

```bash
python -m pytest tests/
```

---

# 📊 Generate Test Coverage

Generate a terminal coverage report.

```bash
python -m pytest --cov=src --cov-report=term-missing tests/
```

---

# 🔍 Execute a Single Test File

```bash
python -m pytest tests/test_model.py
```

---

# 🔍 Execute a Single Test Function

```bash
python -m pytest tests/test_model.py::test_forward_pass
```

---

# 📈 Coverage Goals

The project aims to maximize automated validation of the implemented software components.

| Component | Validation Status |
|-----------|-------------------|
| Data Processing | ✅ |
| Graph Construction | ✅ |
| Feature Engineering | ✅ |
| Model Utilities | ✅ |
| Training Pipeline | ✅ |
| Inference Pipeline | ✅ |
| Helper Functions | ✅ |

---

# 🔄 Continuous Integration

The repository includes GitHub Actions for automated Continuous Integration.

Every push and pull request automatically performs:

- Repository checkout
- Python environment setup
- Dependency installation
- Test execution
- Coverage generation
- Python source compilation

Workflow location:

```
.github/workflows/ci.yml
```

---

# 🐳 Docker Validation

The Docker environment provides a reproducible execution platform.

Build the Docker image.

```bash
docker build -t taxi-route-recommender .
```

Run the container.

```bash
docker run -it taxi-route-recommender
```

Docker Compose.

```bash
docker-compose up --build
```

---

# 🔬 Research Reproducibility

This repository has been organized to facilitate reproducible experimentation.

The following practices have been adopted:

- Fixed dependency versions
- Version-controlled source code
- Containerized execution environment
- Automated testing
- Continuous Integration
- Structured documentation
- Reproducible project configuration

---

# 📚 Experimental Workflow

The recommended workflow for reproducing the research is shown below.

```
Clone Repository
        │
        ▼
Create Virtual Environment
        │
        ▼
Install Dependencies
        │
        ▼
Prepare Dataset
        │
        ▼
Execute Preprocessing
        │
        ▼
Train GCN–LSTM Model
        │
        ▼
Evaluate Model
        │
        ▼
Generate Results
        │
        ▼
Validate Findings
```

---

# 📊 Evaluation Strategy

The implementation should be evaluated using the same methodology described in the original research paper wherever possible.

Evaluation includes:

- Model convergence
- Prediction quality
- Sequential route accuracy
- Computational efficiency
- Research reproducibility

---

# 📁 Supporting Documentation

Additional implementation details are available in the repository documentation.

| Document | Description |
|----------|-------------|
| Software Architecture Document (SAD) | Complete software architecture |
| Project Portfolio | Project planning and implementation |
| Docker Configuration | Reproducible environment |
| GitHub Actions Workflow | Continuous Integration |
| Testing Suite | Automated validation |
| Architecture Diagrams | Visual system documentation |

---

# ✅ Quality Assurance

The repository follows several quality assurance practices.

| Practice | Status |
|----------|:------:|
| Version Control | ✅ |
| Automated Testing | ✅ |
| Continuous Integration | ✅ |
| Docker Support | ✅ |
| Documentation | ✅ |
| Architecture Review | ✅ |
| Code Review Ready | ✅ |
| Research Reproducibility | ✅ |

---

# 📌 Reproducing the Research

To reproduce the published work:

1. Clone the repository.
2. Install the required dependencies.
3. Configure the development environment.
4. Prepare the dataset.
5. Execute preprocessing scripts.
6. Train the GCN–LSTM model.
7. Evaluate model performance.
8. Compare results with the published research.
9. Document observations and improvements.

---

# 📈 Experimental Results & Research Findings

This repository focuses on the **reproduction and analysis** of the research paper:

> **"A Cost-Effective Sequential Route Recommender System for Taxi Drivers"**

The objective is to recreate the proposed methodology, understand the implementation details, and provide a reproducible software framework for future research and development.

---

# 🎯 Experimental Objectives

The primary objectives of this replication study are:

- Reproduce the original GCN–LSTM architecture.
- Implement the complete data processing pipeline.
- Validate the implementation through automated testing.
- Establish a reproducible software environment.
- Document implementation decisions and architectural components.
- Create a professional research software repository.

---

# 📊 Experimental Workflow

```

Historical Taxi Dataset
│
▼
Data Preprocessing
│
▼
Road Network Graph Construction
│
▼
Feature Engineering
│
▼
GCN Spatial Learning
│
▼
LSTM Sequential Learning
│
▼
Model Training
│
▼
Model Evaluation
│
▼
Research Analysis

```

---

# 📋 Evaluation Methodology

The implementation follows the methodology described in the original research paper.

The evaluation process consists of:

| Stage | Description |
|--------|-------------|
| Data Validation | Verify dataset integrity and preprocessing outputs |
| Graph Construction | Validate generated road network graph |
| Feature Engineering | Confirm generated feature vectors |
| Model Training | Train GCN–LSTM architecture |
| Model Evaluation | Compare predicted routes with expected outcomes |
| Result Analysis | Analyze model behaviour and observations |

---

# 📊 Performance Metrics

Depending on the available experimental data, evaluation may include:

| Metric | Purpose |
|---------|---------|
| Prediction Accuracy | Measure recommendation correctness |
| Training Loss | Monitor learning progress |
| Validation Loss | Evaluate model generalization |
| Route Recommendation Quality | Assess generated routes |
| Computational Efficiency | Measure execution performance |

> **Note**
>
> This repository does **not** claim to improve upon the original published results. Its primary objective is faithful implementation, reproducibility, and comprehensive documentation of the proposed methodology.

---

# 📈 Experimental Results

The experimental outcomes should be documented after reproducing the complete training pipeline.

Suggested reporting includes:

- Training configuration
- Hyperparameters
- Dataset characteristics
- Model convergence behaviour
- Evaluation metrics
- Comparison with the original publication
- Observed implementation differences

---

# 🔍 Observations

During the replication process, several engineering improvements were introduced without modifying the underlying research methodology.

Examples include:

- Professional project structure
- Automated testing framework
- Continuous Integration (GitHub Actions)
- Docker support
- Software Architecture Documentation
- Comprehensive repository documentation
- Modern Python project configuration

These additions improve maintainability and reproducibility while preserving the research objectives.

---

# ⚠ Current Limitations

The current implementation has the following limitations:

- Performance depends on dataset availability.
- Experimental results depend on successful reproduction of the original preprocessing pipeline.
- Hyperparameter tuning has not been optimized beyond the published methodology.
- The implementation currently focuses on reproducing the original work rather than proposing a new algorithm.

---

# 🚀 Future Enhancements

Potential directions for future research include:

## Machine Learning

- Graph Attention Networks (GAT)
- Graph Transformers
- Temporal Graph Networks
- Transformer-based sequence modelling

---

## Data

- Larger taxi trajectory datasets
- Multi-city evaluation
- Real-time traffic information
- Weather-aware routing

---

## Deployment

- REST API
- Real-time inference server
- Cloud deployment
- Kubernetes orchestration

---

## Engineering

- Expanded unit test coverage
- Automated benchmarking
- Model versioning
- Experiment tracking
- Performance dashboards

---

# 🛣 Project Roadmap

## Version 1.0 ✅

- Research replication
- Repository organization
- Docker support
- Automated testing
- Software architecture
- GitHub Actions
- Documentation

---

## Version 2.0 🚧

- Professional documentation
- Improved CI/CD
- Modern project configuration
- Repository enhancements

---

## Version 3.0 🔮

- Web-based demonstration
- REST API
- Interactive visualization
- Real-time route recommendation
- Performance benchmarking
- Research extensions

---

# 💼 Portfolio Value

This repository demonstrates practical experience in:

- Machine Learning Engineering
- Graph Neural Networks
- Deep Learning
- Python Software Development
- Software Architecture
- Docker
- GitHub Actions
- Automated Testing
- Research Reproduction
- Technical Documentation

These skills are directly applicable to research engineering, machine learning engineering, software engineering, and data science roles.

---

# 🤝 Contributing

Thank you for your interest in contributing to the **Taxi Route Recommender System**.

Whether you are a researcher, student, developer, or machine learning practitioner, contributions are welcome and appreciated.

Contributions may include:

- Bug fixes
- Documentation improvements
- Performance optimizations
- Additional unit tests
- Model enhancements
- Research extensions
- Dataset improvements
- Docker improvements
- Continuous Integration enhancements

---

# 🌟 Ways to Contribute

You can contribute by:

### 🐞 Reporting Bugs

If you discover a bug:

1. Search existing GitHub Issues.
2. Open a new issue if the bug has not already been reported.
3. Include:
   - Operating System
   - Python Version
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Error messages or screenshots

---

### 💡 Suggesting New Features

Feature requests are welcome.

Please include:

- Problem statement
- Proposed solution
- Expected benefits
- Possible implementation approach

---

### 📖 Improving Documentation

Documentation improvements are highly encouraged.

Examples include:

- README enhancements
- Installation improvements
- Architecture documentation
- API documentation
- Code comments
- Tutorials

---

### 🧪 Improving Test Coverage

Contributors are encouraged to:

- Add new unit tests
- Improve integration testing
- Expand edge-case coverage
- Increase code coverage

---

# 🌿 Development Workflow

The recommended development workflow is shown below.

```
Fork Repository
       │
       ▼
Create Feature Branch
       │
       ▼
Implement Changes
       │
       ▼
Run Tests
       │
       ▼
Commit Changes
       │
       ▼
Push Branch
       │
       ▼
Open Pull Request
```

---

# 📂 Branch Naming Convention

Use descriptive branch names.

Examples:

```
feature/add-gat-model

feature/improve-preprocessing

feature/docker-update

bugfix/fix-training-loop

bugfix/update-ci

docs/readme-improvements

refactor/data-loader
```

---

# 📝 Commit Message Guidelines

Use meaningful commit messages.

Examples:

```
feat: add graph attention network implementation

fix: resolve preprocessing issue

docs: improve README installation guide

test: add unit tests for graph utilities

ci: improve GitHub Actions workflow

refactor: simplify data loading pipeline
```

---

# 🔍 Pull Request Checklist

Before submitting a Pull Request, ensure that:

- Code builds successfully
- All tests pass
- Documentation is updated
- No unnecessary files are included
- Commit messages are meaningful
- Code follows project formatting conventions

---

# 📏 Coding Standards

This project follows modern Python development practices.

### Formatting

- Black

### Import Sorting

- isort

### Linting

- Ruff

### Testing

- Pytest

### Continuous Integration

- GitHub Actions

---

# 🔒 Security

If you discover a security issue:

- Please avoid creating a public GitHub Issue.
- Contact the repository maintainer privately.
- Include sufficient information to reproduce the issue.

Responsible disclosure is appreciated.

---

# 📋 Issue Guidelines

When opening an issue, please include:

- Clear title
- Detailed description
- Environment information
- Steps to reproduce
- Expected result
- Actual result
- Relevant logs or screenshots

Well-documented issues are easier to investigate and resolve.

---

# 🎯 Project Goals

The long-term goals of this repository include:

- Reproducible machine learning research
- High-quality software engineering
- Comprehensive documentation
- Educational value
- Community collaboration
- Research transparency

---

# 💬 Discussions

Potential discussion topics include:

- Graph Neural Networks
- Sequential Recommendation Systems
- Transportation Analytics
- Route Optimization
- Deep Learning
- Research Reproducibility
- Software Engineering Practices

---

# 🛣 Future Roadmap

## Research

- Graph Attention Networks (GAT)
- Graph Transformers
- Dynamic Graph Learning
- Reinforcement Learning for Routing

---

## Engineering

- REST API
- Interactive Dashboard
- Cloud Deployment
- Kubernetes Support
- Experiment Tracking
- Performance Benchmarking

---

## Documentation

- API Reference
- Developer Guide
- User Guide
- Tutorial Series
- Video Demonstrations

---

# 🌍 Community Principles

This project values:

- Respectful communication
- Constructive feedback
- Collaborative learning
- Research integrity
- Open knowledge sharing
- Inclusive participation

Every contribution—whether code, documentation, testing, or feedback—helps improve the quality and reproducibility of this research project.

---

# 📖 Citation

If you use this repository in your research, coursework, or projects, please cite both the original research paper and this replication repository.

---

## Original Research Paper

```text
A Cost-Effective Sequential Route Recommender System for Taxi Drivers.
INFORMS Journal on Computing.
```

Please refer to the official publication for the complete citation details.

---

## Cite This Repository (BibTeX)

```bibtex
@misc{shetye2026taxiroutereplication,
  author       = {Rohit Shetye},
  title        = {Taxi Route Recommender System: Research Replication using GCN-LSTM},
  year         = {2026},
  publisher    = {GitHub},
  url          = {https://github.com/rohitshetye20-ux/Taxi-Route-Recommender-Replication},
  note         = {Research Replication Project}
}
```

---

## Suggested APA Citation

```text
Shetye, R. (2026).
Taxi Route Recommender System: Research Replication using GCN-LSTM.
GitHub Repository.
https://github.com/rohitshetye20-ux/Taxi-Route-Recommender-Replication
```

---

# 📜 License

This project is released under the **MIT License**.

You are free to:

- Use
- Study
- Modify
- Distribute

provided that the terms of the MIT License are respected.

For complete license information, see the `LICENSE` file.

---

# 👨‍💻 Author

## Rohit Shetye

Machine Learning • Data Analytics • Software Engineering • Research Reproduction

### Areas of Interest

- Machine Learning
- Deep Learning
- Graph Neural Networks
- Transportation Analytics
- Route Recommendation Systems
- Software Engineering
- AI Research
- Research Reproducibility

---

# 📬 Contact

For questions, suggestions, or collaboration opportunities, please use one of the following methods.

- GitHub Issues
- GitHub Discussions (if enabled)
- Pull Requests

Professional contact information;

- LinkedIn: *https://www.linkedin.com/in/rohit-shetye-643002167*
- Email: *rohitshetye20@gmail.com*

---

# 🙏 Acknowledgements

This project would not have been possible without the contributions of the research and open-source communities.

Special thanks to:

- The authors of **"A Cost-Effective Sequential Route Recommender System for Taxi Drivers"**
- The INFORMS Journal on Computing
- The TensorFlow community
- The NetworkX community
- The Python open-source ecosystem
- GitHub for providing collaborative development tools

This repository extends the original work by emphasizing reproducible software engineering practices while preserving the underlying research methodology.

---

# 🌟 Repository Summary

This repository includes:

| Component | Status |
|-----------|:------:|
| Research Replication | ✅ |
| Professional Documentation | ✅ |
| Software Architecture | ✅ |
| Docker Support | ✅ |
| GitHub Actions CI | ✅ |
| Automated Testing | ✅ |
| Modern Python Packaging | ✅ |
| Project Portfolio | ✅ |
| Reproducible Development Environment | ✅ |
| Open Source Repository | ✅ |

---

# 🚀 Future Vision

The long-term vision of this project is to evolve from a research replication into a platform for exploring advanced intelligent transportation systems.

Future development may include:

- Graph Attention Networks (GAT)
- Graph Transformers
- Reinforcement Learning
- Real-time Traffic Integration
- REST APIs
- Cloud Deployment
- Interactive Dashboards
- Performance Benchmarking
- Multi-city Evaluation
- Explainable AI Techniques

---

# ⭐ Support the Project

If you found this repository useful:

- ⭐ Star the repository
- 🍴 Fork the repository
- 🐛 Report issues
- 💡 Suggest improvements
- 📖 Share it with others
- 🤝 Contribute through Pull Requests

Every contribution helps improve the quality and reproducibility of this project.

---

# 📌 Final Remarks

This repository represents a comprehensive effort to bridge academic research and professional software engineering.

It demonstrates:

- Reproducible machine learning research
- Graph neural network implementation
- Deep learning workflows
- Modern Python development
- Software architecture design
- Continuous Integration
- Docker-based reproducibility
- Technical documentation
- Open-source development practices

Whether you are a student, researcher, developer, or practitioner, we hope this repository serves as a valuable resource for understanding and extending taxi route recommendation systems.

---

<div align="center">

## Thank You for Visiting

**Happy Learning • Happy Coding • Happy Research**

⭐ **If you found this project useful, consider giving it a Star!** ⭐

</div>

