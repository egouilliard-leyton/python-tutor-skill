# Lesson 15: Loop Patterns — Teaching Guide

## Concept Introduction
"There are 3 patterns every programmer uses constantly: counting, accumulating, and searching. Master these and you can solve almost any loop problem."

## The Three Patterns
1. **Accumulator**: start at 0, add each value → total
2. **Search for max**: start with first item, compare each → biggest
3. **Counter**: start at 0, add 1 when condition met → count

## Hint Sequence
### find_total
1. "Start total at 0. Loop through the list adding each number."
2. "total = 0, then for each n: total += n"

### find_max
1. "Start with the first number. Compare each one — keep the bigger."
2. "biggest = numbers[0], then for each n: if n > biggest: biggest = n"

### count_above
1. "Start count at 0. For each number, check if it's above threshold."
2. "count = 0, then for each n: if n > threshold: count += 1"

## Vocabulary Introduced
- **accumulator** — variable that builds up a value across loop iterations
- **counter** — variable that counts how many times something happens
- **+=** — shorthand for "add to": total += 5 means total = total + 5
