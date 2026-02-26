# Bridge Edge Detection in Undirected Graph (Bottleneck Edges)

## Overview

In an undirected unweighted graph, an edge is called a bottleneck edge (bridge)  
if removing it splits the graph into two disconnected components.

This program identifies all such bridge edges using BFS-based traversal.

---

## Input

The program takes a file name from the command line:

```
python bridge_detection.py graph.txt
```

The file must contain two integers per line representing an edge:

u v

Each line represents an undirected edge between nodes u and v.

---

## Output

Print all bridge edges in the format:

v1 v2

Where:

- v1 < v2
- One edge per line

---

## Folder Structure

```text
graph-bridge-detection/
│
├── bridge_detection.py
└── readme.md
```

---
