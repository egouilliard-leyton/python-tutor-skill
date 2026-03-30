# Lesson 25: Function Composition — Teaching Guide

## Concept Introduction
"Small functions that each do ONE thing can be chained together to do BIG things. This is the heart of good programming."

Analogy: "An assembly line — each station does one job, passes the result to the next."

## Visualization
```
  "  Hi hi Hello hello  "
         │
    clean_text()
         │
  "hi hi hello hello"
         │
    extract_words()
         │
  ["hi", "hi", "hello", "hello"]
         │
    count_unique()
         │
         2
```

## Prediction Question
"If I write `process_text('the the the')`, what do I get? Walk through each step."

## Common Mistakes
### 1. Not passing the result of one function to the next
→ "Each function takes INPUT and gives OUTPUT. Feed the output of one into the input of the next."

### 2. Forgetting that clean_text lowercases
→ "'Hi' and 'hi' become the same word after lowercasing — that's the point!"

### 3. Trying to do everything in process_text
→ "Don't rewrite the logic. CALL the other functions — that's composition!"

## Vocabulary Introduced
- **function composition** — using the output of one function as the input to another
- **pipeline** — a series of functions applied in sequence
- **set** — a collection with no duplicates
