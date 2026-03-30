# Lesson 6: Booleans — Teaching Guide

## Concept Introduction
"So far Python does the same thing every time. But real programs make DECISIONS. Booleans (True/False) are the foundation. Comparisons are questions Python answers with True or False."

Analogy: "A boolean is like a light switch — ON (True) or OFF (False)."

## Key Discussion Points After Running
- **#2 (3 == 3.0):** "Python considers int 3 and float 3.0 as equal. It compares the value, not the type."
- **#3 ("hello" == "Hello"):** "Strings are case-sensitive! Capital H makes them different."
- **#6 (0 == False):** "0 is 'falsy' — Python treats it as False in boolean contexts."
- **#7 ("" == False):** "Tricky! Empty string is 'falsy' with bool() but NOT literally equal to False with ==."

## Common Mistakes
### 1. Confusing = and ==
→ "= puts a value IN a variable. == ASKS if two things are equal. We'll use both soon."

### 2. Thinking strings compare like numbers
→ "Python compares strings character by character, case matters."

## Hint Sequence
1. "Just run each line mentally — is the statement true in real life?"
2. "Watch out for case sensitivity in strings and the difference between 'falsy' and literally False"
3. "For your own comparisons, try comparing strings, numbers, or mixing types"

## Vocabulary Introduced
- **boolean** — True or False
- **comparison operator** — ==, !=, <, >, <=, >=
- **==** — "is equal to?" (different from = which assigns)
