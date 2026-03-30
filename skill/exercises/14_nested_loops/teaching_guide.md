# Lesson 14: Nested Loops — Teaching Guide

## Concept Introduction
"A loop inside a loop. The inner loop runs completely for each step of the outer loop."

Analogy: "A clock: the minute hand (inner) goes all the way around for each hour (outer)."

## Visualization
```
Outer i=1: Inner j=1,2,3 → "1x1=1  1x2=2  1x3=3"
Outer i=2: Inner j=1,2,3 → "2x1=2  2x2=4  2x3=6"
Outer i=3: Inner j=1,2,3 → "3x1=3  3x2=6  3x3=9"
```

## Hint Sequence
1. "You need two for loops — one inside the other"
2. "Outer loop: for i in range(1, n+1). Inner loop: for j in range(1, n+1)"
3. "Build each row as a string inside the inner loop, then append the finished row"

## Vocabulary Introduced
- **nested loop** — a loop inside another loop
