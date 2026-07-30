# Contributing to Taxi Route Recommender

First of all, thank you for your interest in contributing to this project.

This repository reproduces the research paper **"A Cost-Effective Sequential Route Recommender System for Taxi Drivers"** while extending it with modern software engineering practices, automated documentation, professional visualizations, and reproducible workflows.

Whether you are fixing bugs, improving documentation, optimizing code, or proposing new features, your contributions are greatly appreciated.

---

# Code of Conduct

By participating in this project, you agree to communicate respectfully and constructively.

Please:

- Be respectful and professional.
- Welcome constructive feedback.
- Help create an inclusive learning environment.
- Focus discussions on technical improvements.

---

# Ways to Contribute

Contributions of many kinds are welcome, including:

## Machine Learning

- Improve model implementations
- Optimize training performance
- Add evaluation metrics
- Improve preprocessing
- Experiment with new architectures

Examples:

- Graph Attention Networks (GAT)
- GraphSAGE
- Transformer-based models
- Hyperparameter optimization

---

## Software Engineering

Contributions are welcome for:

- Bug fixes
- Performance improvements
- Code refactoring
- Better modularization
- Improved configuration management
- Testing
- Logging
- Error handling

---

## Documentation

Documentation improvements are always valuable.

Examples include:

- README enhancements
- Tutorial improvements
- API documentation
- Installation guides
- Architecture explanations
- Code comments
- Usage examples

---

## Visualization

Additional technical figures are welcome.

Possible improvements include:

- Interactive diagrams
- Geographic visualizations
- Dashboard improvements
- Training visualizations
- Performance charts

---

# Development Setup

Clone the repository:

```bash
git clone https://github.com/rohitshetye20-ux/Taxi-Route-Recommender.git

cd Taxi-Route-Recommender
```

Create a virtual environment:

```bash
python -m venv taxi_tf_env
```

Activate it:

### Windows

```bash
taxi_tf_env\Scripts\activate
```

### Linux / macOS

```bash
source taxi_tf_env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Project Structure

```text
Taxi-Route-Recommender/

├── data/
├── figures/
├── notebooks/
├── outputs/
├── report/
├── report_builder/
├── presentation/
├── Presentation_Builder/
├── src/
├── docs/
├── models/
├── README.md
└── requirements.txt
```

Please keep new files organized according to the existing structure.

---

# Contribution Workflow

The recommended workflow is:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes.
5. Commit with a descriptive message.
6. Push your branch.
7. Open a Pull Request.

Example:

```bash
git checkout -b feature/improve-training-pipeline
```

---

# Pull Request Guidelines

Please ensure that your Pull Request:

- Has a clear description.
- Solves one logical problem.
- Includes documentation updates if needed.
- Does not introduce unrelated changes.
- Preserves project reproducibility.

If applicable, include:

- Screenshots
- Benchmark results
- Before/after comparisons
- References to related issues

---

# Coding Standards

Please follow these general guidelines.

## Python

- Follow PEP 8.
- Use descriptive variable names.
- Prefer modular functions.
- Avoid duplicated code.
- Add docstrings to public functions.

---

## Documentation

Documentation should:

- Be written in Markdown.
- Use consistent formatting.
- Explain *why* changes were made, not only *what* changed.
- Include figures where appropriate.

---

## Visual Assets

When adding figures:

- Use PNG format where practical.
- Choose descriptive filenames.
- Maintain consistent naming conventions.
- Update documentation if new figures are introduced.

---

# Reporting Bugs

When reporting an issue, please include:

- Operating system
- Python version
- TensorFlow version
- Error message
- Steps to reproduce
- Expected behavior
- Actual behavior

Screenshots are helpful when relevant.

---

# Feature Requests

Feature requests are welcome.

A good proposal should explain:

- The problem being solved
- Why the feature is useful
- Possible implementation ideas
- Any supporting references

---

# Research Contributions

If proposing changes to the machine learning methodology:

- Clearly distinguish them from the reproduced implementation.
- Provide references where appropriate.
- Document experimental results.
- Preserve reproducibility.

---

# Documentation Contributions

Contributions are encouraged for:

- README improvements
- Tutorials
- Architecture diagrams
- Presentation content
- Technical report updates

High-quality documentation is considered as valuable as code contributions.

---

# Testing Checklist

Before submitting a Pull Request, verify that:

- All Python files run without syntax errors.
- Existing functionality continues to work.
- Documentation builds correctly.
- Figures display correctly.
- Report generation succeeds.
- Presentation generation succeeds.

---

# Recognition

All meaningful contributions will be acknowledged through the project's GitHub history and contributor records.

Every contribution—whether code, documentation, testing, or feedback—helps improve the project.

---

# Questions

If you have questions or suggestions:

- Open a GitHub Issue.
- Start a GitHub Discussion (if enabled).
- Submit a Pull Request.
- Share improvement ideas.

---

# Thank You

Thank you for helping improve this project.

Your contributions support reproducible research, better software engineering practices, and a stronger open-source community.