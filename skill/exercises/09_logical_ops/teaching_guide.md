# Lesson 9: Logical Operators — Teaching Guide

## Concept Introduction
"Sometimes one condition isn't enough. 'and' means BOTH must be true. 'or' means AT LEAST ONE."

## The Three Bugs
1. **`or` should be `and`** — BOTH height AND age must pass, not just one
2. **`age = 8` should be `age == 8`** — = assigns, == compares (or better: remove the elif entirely)
3. **Final `return True` should be `return False`** — if we get past the if, the person can't ride

## Teaching Approach
Don't tell them the bugs. Ask:
1. "Run it. What output do you get? What SHOULD it be?"
2. "Look at line with `or` — if someone is 200cm tall but age 2, should they ride?"
3. "Python says SyntaxError on the elif line — look at the `=` sign carefully"
4. "If neither condition fully passes, should the function return True or False?"

## Vocabulary Introduced
- **and** — both conditions must be True
- **or** — at least one must be True
- **not** — flips True to False
