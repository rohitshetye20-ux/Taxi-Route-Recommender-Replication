# Known Issues & Technical Debt

**Project:** Taxi Route Recommender System (Research Replication)

**Version:** v2.0.0

**Last Updated:** July 2026

---

# Purpose

This document tracks known issues, technical debt, and planned improvements for future releases. These issues do not prevent the repository from serving as a professional research replication project but represent areas for future enhancement.

---

# Issue 1 – DataPreprocessor Methods Missing

## Status

Open

## Priority

High

## Description

Several unit tests expect the `DataPreprocessor` class to expose the following methods:

- validate_dataframe()
- create_distance_category()
- remove_outliers()
- has_required_columns()
- standardize_column_names()

Currently these methods are not implemented (or no longer exist), resulting in multiple failing unit tests.

## Impact

- Unit tests fail
- No impact on repository documentation
- Does not affect GitHub repository functionality

## Planned Release

v2.1

---

# Issue 2 – Visualization Error Handling

## Status

Open

## Priority

Medium

## Description

The visualization test expects a `ValueError` when an empty history object is supplied.

Current implementation does not raise the expected exception.

## Impact

One visualization test fails.

## Planned Release

v2.1

---

# Issue 3 – Unit Test Alignment

## Status

Open

## Priority

High

## Description

Some unit tests were written before the preprocessing module reached feature parity.

The test suite should be reviewed alongside the implementation to determine whether:

- missing functionality should be implemented, or
- outdated tests should be updated.

## Planned Release

v2.1

---

# Issue 4 – Research Pipeline Integration

## Status

Planned

## Priority

Critical

## Description

The original research implementation located in:

original_repo/script/

has not yet been integrated with the modern project structure.

This will be completed during the research replication phase.

## Planned Release

v3.0

---

# Future Roadmap

## v2.1

- Complete preprocessing utilities
- Pass unit tests
- Improve CI coverage

## v2.2

- Improve documentation
- Increase test coverage
- Add performance benchmarks

## v3.0

- Execute full research pipeline
- Reproduce published results
- Compare metrics with original paper
- Publish reproducibility report

---

# Notes

Repository infrastructure is considered complete for Version 2.0.

Remaining work focuses primarily on:

- research execution
- feature completion
- scientific validation
