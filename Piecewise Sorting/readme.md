# Sorting a Piecewise Sorted Array

## Problem Description

You are given an array of n integers that is already piecewise sorted in ascending order.  
The array consists of m sorted pieces of equal size. Your goal is to merge these pieces and produce a fully sorted array efficiently.

Each piece has size `n/m`.

For piece i:

- Start index: `(n/m) * i`
- End index: `(n/m) * (i + 1) - 1`

Assume:

- n is divisible by m
- Each piece is already sorted internally

Required time complexity: **O(n log m)**

---

## Approach

The problem is solved using a min-heap (priority queue) to perform a k-way merge.

Steps:

1. Insert the first element of each sorted piece into a min-heap.
2. Extract the minimum element from the heap.
3. Insert the next element from the same piece into the heap.
4. Repeat until all elements are extracted.

Since the heap contains at most m elements:

- Each insertion/removal costs O(log m)
- Total operations = n

Overall complexity: O(n log m)

---

## Folder Structure

```text
Piecewise Sorting/
│
├── piecewise_sorting.py
└── readme.md
```

---

## How to Run

```bash
python assignment3.py
```

Then enter:

```
input.txt
3
```

The program will:

- Read integers from file
- Assume the array is piecewise sorted
- Merge all pieces
- Print the fully sorted output
