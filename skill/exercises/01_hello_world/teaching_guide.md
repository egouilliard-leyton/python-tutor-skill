# Lesson 1: Hello World — Teaching Guide

## Concept Introduction
"Every programmer in history started with the same thing: making the computer say 'Hello, World!' It's a tradition. Let's do it."

Show: `print("Hello, World!")` — explain that print() is how Python talks to you.

## Prediction Question
"What do you think happens if you forget the quotes? Try: `print(Hello)` — what do you think Python will say?"

## Common Mistakes

### 1. Missing quotes
```python
print(Hello, World!)  # NameError
```
→ "Python thinks Hello is a variable name, not text. Wrap it in quotes to make it a string."

### 2. Missing parentheses
```python
print "Hello, World!"  # SyntaxError
```
→ "In Python 3, print needs parentheses. It's print(), not just print."

### 3. Mismatched quotes
```python
print("Hello, World!')  # SyntaxError
```
→ "You started with a double quote but ended with a single quote. They need to match."

### 4. Forgetting to save before running
→ "Make sure you save (Ctrl+S) before running python3 exercise.py"

## Hint Sequence
1. "print() needs parentheses with text inside quotes"
2. "Write: print(\"Hello, World!\") — make sure the quotes match"
3. "You need three separate print() lines, one for each message"

## After Success
"You just wrote and ran your first Python program. Every developer in the world started exactly where you are right now. From here, it only gets more interesting."

## Vocabulary Introduced
- **print()** — a built-in function that displays text on screen
- **string** — text data, anything inside quotes
- **syntax** — the rules for how Python code must be written
