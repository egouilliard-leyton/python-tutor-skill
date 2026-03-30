# Lesson 22: Parameters & Return — Teaching Guide

## Concept Introduction
"Parameters are inputs to a function. Return is the output. Think of a function like a machine: stuff goes in, stuff comes out."

Analogy: "A vending machine — you put in a coin (parameter), press a button, and get a drink back (return value)."

## Visualization
```
  convert_f_to_c(212)
       │
       ▼
  ┌──────────────────┐
  │ (212 - 32) * 5/9 │
  │ = 100.0           │
  └──────────────────┘
       │
       ▼
     100.0  ← returned value
```

## Prediction Question
"If I write `result = convert_f_to_c(32)`, what is result? And what about `convert_f_to_c(-40)`?"

## Common Mistakes
### 1. Printing instead of returning
→ "If you print inside the function, the caller gets None. Use return!"

### 2. Forgetting to round
→ "The formula gives lots of decimals. round(value, 1) keeps just one."

### 3. Not calling the helper functions in convert_temp
→ "Don't repeat the formula — call convert_f_to_c or convert_c_to_f!"

## Vocabulary Introduced
- **parameter** — variable listed in a function definition
- **argument** — actual value passed when calling a function
- **return value** — the result a function sends back
- **round()** — built-in function to limit decimal places
