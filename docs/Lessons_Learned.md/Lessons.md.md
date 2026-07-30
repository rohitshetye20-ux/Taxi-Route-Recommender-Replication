# Lessons Learned

## Project

**Reproduction of "A Cost-Effective Sequential Route Recommender System for Taxi Drivers"**

---

# Table of Contents

1. Introduction
2. Technical Skills Developed
3. Research Skills Developed
4. Software Engineering Skills Developed
5. Machine Learning Insights
6. Challenges That Improved My Skills
7. Key Takeaways
8. Future Learning Goals
9. Personal Reflection

---

# 1. Introduction

This project was much more than executing an existing repository. It involved understanding a legacy research implementation, resolving compatibility issues, reconstructing missing datasets, analyzing model architecture, and successfully reproducing the training and evaluation pipeline.

The experience strengthened both my machine learning knowledge and my software engineering skills.

---

# 2. Technical Skills Developed

## Environment Management

Before this project, I had limited experience working with legacy machine learning environments.

During reproduction, I learned how to:

- Create isolated virtual environments
- Select compatible Python versions
- Manage TensorFlow dependencies
- Resolve package conflicts
- Configure Jupyter kernels correctly

These skills are essential when reproducing research repositories or maintaining production machine learning systems.

---

## Dependency Debugging

One of the biggest learning experiences was resolving compatibility issues between scientific libraries.

Examples included:

- TensorFlow and Python version compatibility
- TensorFlow and NumPy compatibility
- SciPy API changes
- Module import issues
- Package version conflicts

Instead of reinstalling packages blindly, I learned to investigate the root cause of each issue before applying a fix.

---

## Working with Legacy Code

The original repository was implemented using TensorFlow 1.x APIs.

This project helped me understand:

- TensorFlow graph execution
- Placeholders
- Sessions
- Feed dictionaries
- Static computational graphs

Although modern TensorFlow uses eager execution, understanding graph-based execution provides valuable insight into the evolution of deep learning frameworks.

---

# 3. Research Skills Developed

## Reading Research Code

Initially, the repository structure appeared difficult to understand.

By carefully analyzing each module, I learned how to:

- Read unfamiliar codebases
- Identify the role of each file
- Trace function calls
- Understand data flow
- Connect implementation details to concepts described in the research paper

This significantly improved my ability to interpret academic code.

---

## Reproducibility

One of the most important lessons from this project is that reproducibility extends beyond downloading a repository.

Successful reproduction required:

- Correct software versions
- Dataset preparation
- Working directory management
- Dependency fixes
- Verification of outputs

I now appreciate why reproducibility is considered a core principle of scientific research.

---

# 4. Software Engineering Skills Developed

## Debugging Methodology

Rather than attempting random fixes, I adopted a structured debugging process.

Typical workflow:

1. Read the error message carefully
2. Identify the failing component
3. Inspect the source code
4. Verify assumptions
5. Apply the smallest possible fix
6. Test the solution
7. Document the outcome

This systematic approach reduced repeated mistakes and made troubleshooting more efficient.

---

## Code Organization

The project demonstrated the value of modular software design.

Responsibilities were separated into:

- Data loading
- Utility functions
- Graph operations
- Neural network layers
- Training
- Route recommendation

This organization made the repository easier to analyze and debug.

---

## Documentation

Writing detailed documentation for each stage of reproduction reinforced the importance of clear technical communication.

Good documentation enables:

- Easier onboarding
- Better collaboration
- Improved reproducibility
- Faster debugging
- Long-term maintainability

---

# 5. Machine Learning Insights

The project provided practical understanding of several machine learning concepts.

## Graph Neural Networks

I learned how Graph Convolutional Networks model spatial relationships between connected road segments instead of treating them as independent observations.

---

## Sequential Learning

The LSTM component demonstrated how temporal dependencies can improve prediction by incorporating historical traffic information.

---

## Feature Fusion

The model combines multiple sources of information:

- Spatial road network
- Historical traffic demand
- Weather information

This highlighted the importance of integrating heterogeneous data sources in real-world prediction systems.

---

## Model Evaluation

The reproduction process reinforced the importance of evaluating models using independent test data and quantitative metrics such as Mean Absolute Error (MAE).

---

# 6. Challenges That Improved My Skills

Several engineering challenges significantly strengthened my technical abilities.

These included:

- Resolving TensorFlow installation issues
- Managing Python version compatibility
- Fixing NumPy incompatibilities
- Handling SciPy API changes
- Correcting module import paths
- Reconstructing missing datasets
- Understanding relative file paths
- Inspecting model architecture
- Executing the complete training pipeline

Each issue improved my confidence in debugging complex machine learning projects.

---

# 7. Key Takeaways

The most important lessons from this project are:

- Environment reproducibility is as important as model implementation.
- Reading source code is often necessary when documentation is incomplete.
- Legacy machine learning projects require careful dependency management.
- Systematic debugging is more effective than trial-and-error.
- Documentation is an essential engineering skill.
- Reproducing research code provides deeper understanding than simply reading a paper.

---

# 8. Future Learning Goals

This project has motivated me to continue developing expertise in:

- Modern Graph Neural Networks
- PyTorch Geometric
- TensorFlow 2.x migration
- Docker for reproducible environments
- MLOps and experiment tracking
- Cloud-based machine learning deployment
- Real-time traffic prediction systems

---

# 9. Personal Reflection

This project represented a transition from simply using machine learning libraries to understanding how complex research systems are built, organized, and reproduced.

Beyond reproducing published results, I gained experience in software engineering, debugging, dependency management, documentation, and technical communication.

Completing this reproduction has increased my confidence in approaching unfamiliar codebases and solving engineering problems systematically. The experience has prepared me to contribute more effectively to machine learning projects in both research and industry settings.

---

# Conclusion

Reproducing the GCN-LSTM taxi route recommendation system was a valuable learning experience that combined machine learning theory, software engineering, and practical debugging. The project strengthened my ability to analyze complex repositories, resolve technical challenges, and communicate engineering work clearly—skills that are directly applicable to professional ML engineering and data science roles.
