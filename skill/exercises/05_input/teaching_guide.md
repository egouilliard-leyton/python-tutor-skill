# Lesson 5: User Input — Teaching Guide

## Concept Introduction
"So far, everything in your programs is hardcoded. Real programs talk to the user! input() pauses and waits for them to type something."

Analogy: "input() is like asking a question — you ask, then wait for the answer."

## Prediction Question
"If I write `x = input('Type a number: ')` and type 5, what type is x? A number or text?"

Answer: "It's ALWAYS text (a string). That's the #1 gotcha with input()."

## Common Mistakes

### 1. Forgetting int() conversion
```python
age = 2026 - birth_year  # TypeError: str - str
```
→ "input() always returns a string. '2010' is text, not a number. Wrap it: int(birth_year)"

### 2. Converting the wrong thing
```python
name = int(input("Name? "))  # Crashes on "Charles"
```
→ "Only convert things that should be numbers. Names stay as strings."

### 3. Missing the prompt string
```python
name = input()  # Works but user sees no question
```
→ "Put your question inside input(): input('What is your name? ') — the space after ? makes it look nicer."

### 4. Math on strings
```python
age = "2026" - birth_year  # Both are strings, can't subtract
```
→ "2026 should be a number (no quotes), and birth_year needs int()"

## Hint Sequence
1. "input('question') asks a question and saves the answer"
2. "input() returns text. Use int() to convert birth year to a number"
3. "age = 2026 - int(birth_year), then print with an f-string"

## Vocabulary Introduced
- **input()** — asks user to type something, returns it as a string
- **type conversion** — changing data from one type to another (str → int)
- **int()** — converts text to a whole number
- **str()** — converts a number to text
