# Lesson 7: If/Else — Teaching Guide

## Concept Introduction
"Now Python can make decisions! 'if' runs code only when something is True. 'else' is the backup plan."

Analogy: "A fork in the road — if the bridge is open, go straight. Otherwise, take the detour."

## Prediction Question
"If age is 18 and we write `if age >= 18:` — does it go into the if or the else? What about age = 17?"

## Common Mistakes

### 1. Missing colon after if
```python
if age >= 18  # SyntaxError
```
→ "Every if/else line ends with a colon. It's Python's way of saying 'here's what follows'."

### 2. Using = instead of >=
```python
if age = 18:  # SyntaxError
```
→ "= assigns, == checks equality, >= checks greater-or-equal. You want >=."

### 3. Wrong indentation
```python
if age >= 18:
return "You can vote!"  # IndentationError
```
→ "Everything INSIDE the if block must be indented (4 spaces or Tab)."

### 4. Forgetting to calculate years left
```python
return "Not yet! More years to go."  # Missing the number
```
→ "How many years? 18 - age gives you the answer."

## Hint Sequence
1. "Use if and else — check if age is at least 18"
2. "if age >= 18: return the success message. else: return the waiting message."
3. "For the years remaining: 18 - age. Put it in your f-string."

## Vocabulary Introduced
- **if** — runs code only when condition is True
- **else** — runs code when the if condition is False
- **condition** — expression that evaluates to True or False
- **indentation** — spaces at the start of a line that group code together
