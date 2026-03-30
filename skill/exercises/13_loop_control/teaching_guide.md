# Lesson 13: Break & Continue — Teaching Guide

## Concept Introduction
"break = emergency exit from a loop. continue = skip this one, move to the next."

## The Three Bugs
1. **continue should be break** for "quit" — we want to STOP, not skip
2. **break should be continue** for short passwords — we want to SKIP, not stop
3. **print(pw) should be valid.append(pw)** — we need to collect, not just print

## Teaching Approach
"Run it first. Compare the output to what's expected. Which passwords appear that shouldn't? Which are missing?"

## Vocabulary Introduced
- **break** — exit the loop entirely
- **continue** — skip to the next iteration
