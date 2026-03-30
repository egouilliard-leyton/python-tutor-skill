# Lesson 2: Variables — Teaching Guide

## Concept Introduction
"So far, we typed text directly into print(). But what if you want to use the same value multiple times? That's what variables are for — named containers that hold values."

Analogy: "Think of a variable like a labeled box. You put something in, write a name on the box, and later you find it by name."

## Prediction Question
"If I write `name = 'Charles'` and then `print(name)` — what do you think gets printed? The word 'name' or 'Charles'?"

## Common Mistakes

### 1. Putting quotes around numbers
```python
age = "16"  # This is a string, not a number
```
→ "This works for now, but later when we do math with age, it'll break. Numbers don't need quotes."

### 2. Forgetting f in f-string
```python
print("Name: {name}")  # Prints literal {name}
```
→ "Without the f before the quotes, Python doesn't know to substitute the variable. Add the f!"

### 3. Using = instead of == later
→ Don't mention this yet. It comes in lesson 6.

### 4. Spaces around = sign
```python
name="Charles"  # Works but not PEP8 style
```
→ Don't correct this in week 1. Only mention style from week 3+.

## Hint Sequence
1. "A variable stores a value with a name. Try: name = \"Charles\""
2. "To print a variable with text, use f-strings: print(f\"Name: {name}\")"
3. "Create all three variables first, then add three print() lines using f-strings"

## After Success
"You now have named containers for data. This is huge — almost every program in existence uses variables. Next we'll learn about strings — the text type."

## Vocabulary Introduced
- **variable** — a name that stores a value
- **assignment** — giving a value to a variable with =
- **f-string** — a string starting with f that can include {variables}
- **integer** — a whole number (no decimal)
