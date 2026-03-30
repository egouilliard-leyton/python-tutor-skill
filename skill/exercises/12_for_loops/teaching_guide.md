# Lesson 12: For Loops — Teaching Guide

## Concept Introduction
"A for loop runs a specific number of times. range(1, 6) gives you 1, 2, 3, 4, 5."

Analogy: "A coach saying 'do 10 pushups' — you know exactly how many."

## Prediction Question
"What does range(1, 6) give? Does it include 6?"
→ "No! range(1, 6) gives 1, 2, 3, 4, 5. The end number is excluded."

## Common Mistakes
### 1. Checking 3 and 5 separately before checking both
→ "If you check 3 first, then 5, what happens to 15? It matches 3 and stops — never checks for both."

### 2. range(n) instead of range(1, n+1)
→ "range(5) gives 0,1,2,3,4. You want 1,2,3,4,5 — use range(1, n+1)."

### 3. Using == 3 instead of % 3 == 0
→ "== 3 only matches exactly 3. % gives the remainder: 9 % 3 is 0, meaning 9 IS a multiple of 3."

## Hint Sequence
1. "for i in range(1, n + 1) — this gives you each number"
2. "Check the 'both' condition FIRST: i % 3 == 0 and i % 5 == 0"
3. "Build a list with append(). After the loop, return it."

## Vocabulary Introduced
- **for** — loop that runs a set number of times
- **range()** — generates a sequence of numbers
- **% (modulo)** — gives the remainder after division
