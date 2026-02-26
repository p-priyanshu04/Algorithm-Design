# Ordered Word Pair Search using Custom Hash Table

## Overview

You are given a text file containing sentences (one per line).  
Each sentence has an ID equal to its line number.

Given two words `p` and `q`, the task is to find all line IDs where the ordered pair  
`p q` appears consecutively.

A custom hash table must be implemented with **word as key** using:

h(key) = ((a \* key + b) mod p) mod m

where:

- p = 999999937
- a ∈ {1 … p−1}
- b ∈ {0 … p−1}
- m = hash table size from command line

Words must be converted to lowercase.  
Word boundaries are any non-alphanumeric characters.

---

## Input

Program takes command line arguments:

```
python assignment6.py file.txt m word1 word2
```

- file.txt → text file
- m → hash table size
- word1 → first word
- word2 → second word

---

## Output

Print line IDs where the ordered pair appears.  
One line ID per line.

---

## Folder Structure

```text
Custom Hash Text Search/
│
├── custom_hash_text_search.py
└── readme.md
```

---
