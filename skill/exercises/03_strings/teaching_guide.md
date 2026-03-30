# Lesson 3: Strings — Teaching Guide

## Concept Introduction
"Strings are text — anything inside quotes. Python can slice them, combine them, change their case, and much more. Let's build something real with strings."

Analogy: "A string is literally a 'string' of characters, like beads on a necklace. Each bead has a position number, starting at 0."

## Prediction Question
"What do you think `'Charles'[0]` gives you? What about `'Charles'[1]`?"

## Common Mistakes

### 1. Forgetting .lower()
```python
return first[0] + last  # "CGouilliard" not "cgouilliard"
```
→ "It works for lowercase input but try JEAN DUPONT — what happens?"

### 2. Using first[1] thinking it's the first character
```python
return first[1] + last  # "h" not "C"
```
→ "Python counts from 0, not 1. first[0] is the FIRST character."

### 3. Using print instead of return
```python
def make_username(first, last):
    print(first[0] + last)  # Prints but returns None
```
→ "print() shows text on screen but doesn't give a value back. Use return so the function can be used by other code."

### 4. Applying .lower() to only one part
```python
return first[0].lower() + last  # Misses uppercase last name
```
→ "What happens if the last name is also uppercase? Where should .lower() go?"

## Hint Sequence
1. "You need three operations: get one character, combine strings, and change case"
2. "first[0] gives the first letter. The + operator joins strings together"
3. "Almost! Apply .lower() to the whole result: (first[0] + last).lower()"

## If Stuck (3+ attempts)
"Let's break it into pieces. First, just get the first letter: `print('Charles'[0])`. Got it? Now combine it with a last name using +."

## Vocabulary Introduced
- **index** — position of a character (starts at 0)
- **concatenation** — joining strings with +
- **.lower()** — method that makes text lowercase
- **return** — sends a value back from a function
