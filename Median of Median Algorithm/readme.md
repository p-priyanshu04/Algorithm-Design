# Linear-Time Selection of k Taxpayers Closest to Median Income

## Overview

This assignment solves the following problem:

Given a dataset of individuals with:

- unique ID
- total income
- tax paid

We must find the IDs of the **k taxpayers whose income is closest to the median income**.

The solution must run in **linear time O(n)** even in the worst case.

This is achieved using the **Median of Medians (deterministic selection)** algorithm.

---

## Problem Requirements

- Input file contains one record per line:

  id total_income tax_paid

- Program takes two command line arguments:
  1. filename containing the dataset
  2. value of k

- Output:
  IDs of k taxpayers whose income is closest to median income  
  (one ID per line)

---

## Approach

1. Extract all incomes
2. Compute median using Median-of-Medians selection (worst-case O(n))
3. Compute distance of each income from median
4. Select k smallest distances using linear-time selection
5. Print corresponding IDs

This guarantees **O(n)** worst-case time.

---

## Folder Structure

```text
assignment-04-median-taxpayers/
│
├── assignment4.py
└── readme.md
```

---

## How to Run

```
python median_of_medians.py data.txt k
```
