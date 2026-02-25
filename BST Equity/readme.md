# BST Equity — Highest Equity Non-Leaf Nodes

## Overview

This assignment builds a Binary Search Tree (BST) from a list of integers and computes the **equity** of each non-leaf node.

Equity of a node measures how balanced its left and right subtrees are using:

Equity(i) = 1 − | (avg(left)/max(left)) − (avg(right)/max(right)) |

Special cases:

- Leaf nodes → equity = 1
- Empty subtree → equity treated as 1

Goal:  
Find the non-leaf node(s) with the **maximum equity value**.

If multiple nodes have the same maximum equity, print all.

---

## Input

Program takes input file name from command line.

File contains one integer per line.

```
python assignment5.py data.txt
```

---

## Output

Print:
node_value equity

One node per line for all nodes having maximum equity.

---

## Folder Structure

```text
BST Equity/
│
├── bst.py
└── readme.md
```
