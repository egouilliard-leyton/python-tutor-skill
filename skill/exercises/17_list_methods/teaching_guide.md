# Lesson 17: List Methods — Teaching Guide

## Concept Introduction
"Lists have built-in superpowers: add, remove, sort, slice."

Analogy: "Like a playlist app — add songs, remove songs, shuffle, play just the top 3."

## Common Mistakes
### 1. Using .sort() instead of sorted()
→ ".sort() modifies the original and returns None. sorted() returns a new list."

### 2. Forgetting to check before .remove()
→ ".remove() crashes if the item doesn't exist. Check with `if song in playlist` first."

### 3. Slicing confusion
→ "playlist[:3] means 'from the start, take 3'. It never crashes even if there are fewer."

## Vocabulary Introduced
- **.append()** — add item to end of list
- **.remove()** — remove first occurrence of item
- **slicing** — list[start:end] gets a portion
- **sorted()** — returns a new sorted copy
