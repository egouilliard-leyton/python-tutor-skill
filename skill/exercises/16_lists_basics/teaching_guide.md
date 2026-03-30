# Lesson 16: Lists Basics — Teaching Guide

## Concept Introduction
"So far every variable holds ONE thing. A list holds MANY things in order — like a shopping list."

Analogy: "A numbered list on paper. Item 0 is at the top."

## Visualization
```
  fruits = ["apple", "banana", "cherry"]
  Index:    0          1          2

  fruits[0]  → "apple"
  fruits[-1] → "cherry"  (last item)
  len(fruits) → 3
```

## Prediction Question
"If `my_list = [10, 20, 30]`, what does `my_list[1]` give? Not 10!"

## Common Mistakes
### 1. Forgetting lists start at index 0
→ "my_list[1] is the SECOND item. First is my_list[0]."

### 2. Using parentheses instead of brackets
→ "(a, b, c) is a tuple, not a list. Use [a, b, c]."

## Vocabulary Introduced
- **list** — ordered collection of items in square brackets
- **index** — position number (starts at 0)
- **len()** — returns how many items in a list
