# Lesson 20: Nested Structures — Teaching Guide

## Concept Introduction
"Real data is nested — a list of student dicts, a dict of lists. This is how actual programs store information."

Analogy: "A filing cabinet: drawers (list) contain folders (dicts) which contain papers (values)."

## Visualization
```
students = [
    {"name": "Alice", "grade": 85},  ← students[0]
    {"name": "Bob",   "grade": 72},  ← students[1]
]

students[0]["name"]  → "Alice"
students[1]["grade"] → 72
```

## Vocabulary Introduced
- **nested** — data structures inside other data structures
- **list of dicts** — the most common pattern in real programs
