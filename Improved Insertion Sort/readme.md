# Improved Insertion Sort with Binary Search

## Overview

This assignment implements an optimized version of the classical **Insertion Sort** algorithm.  
The goal is to study how small algorithmic improvements affect performance when working with **large-scale datasets**.

Two main optimizations are introduced:

1. Using **binary search** to find the insertion position.
2. Inserting **two elements at a time** instead of one.

The performance of this improved version is compared against the standard insertion sort on very large randomly generated datasets.

---

## Problem Statement

Implement an improved insertion sort with the following features:

1. Use binary search to determine the correct position of an element.
2. Instead of inserting one element at a time:
   - Process two elements together
   - Insert the larger element first
   - Then insert the smaller element
   - Shift elements two places while inserting the larger one

Finally:

- Generate large random datasets
- Compare execution time with basic insertion sort

---

## Files

Improved Insertion Sort
│
├── improved_insertion_sort.py # Improved algorithm
├── insertion_sort.py # Basic insertion sort
└── data_generator.py # Benchmark + plotting
└── readme.md

---

## How to Run

Make sure all three files are in the same folder.

Run:

```bash
python test.py
```
