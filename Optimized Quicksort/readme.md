# Optimized QuickSort with Hybrid Insertion Sort

## Overview

This assignment implements an optimized version of the QuickSort algorithm with the following enhancements:

- Pivot chosen as the median of three randomly selected elements
- Hybrid approach using Insertion Sort for small subarrays
- Stack usage kept close to O(log n) through recursive partitioning
- Reads the full dataset of integers from an input file
- Sorts the data in-place using the optimized algorithm

The goal is to study practical performance improvements and memory behavior of QuickSort on large datasets.

---

## Problem Statement

### Pivot Selection

- Randomly select three indices from the current subarray
- Choose the median of their values as the pivot

### Stack Space Constraint

- Maintain worst-case stack usage close to O(log n) by recursive partitioning

### Hybrid Sorting Strategy

- For small subarrays, use Insertion Sort instead of QuickSort
- Threshold chosen experimentally (based on when insertion sort becomes faster)

---

## Folder Structure

```text
Optimized Quicksort/
│
├── optimized_quicksort.py
└── readme.md
```
