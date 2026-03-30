# Lesson 24: Scope — Teaching Guide

## Concept Introduction
"Every variable has a 'home' — the place where it was created. A variable inside a function can't be seen outside it."

Analogy: "Your bedroom vs the living room. Your stuff in your room is private (local). The living room stuff is shared (global)."

## Visualization
```
  GLOBAL SCOPE          FUNCTION SCOPE
  ┌───────────┐         ┌───────────┐
  │ y = "hi"  │         │ y = "bye" │  ← different y!
  │ z = 42    │ ──can── │ (can see   │
  │           │  read→  │  z = 42)   │
  └───────────┘         └───────────┘
                        y disappears when
                        function ends
```

## Prediction Question
"If I write `x = 5` outside a function, and `x = 10` inside it, then print x outside — what do I get?"

## Common Mistakes
### 1. Thinking a function changes a global variable
→ "Assignment inside a function creates a LOCAL variable with the same name. The global is untouched."

### 2. Confusing mutation with reassignment
→ "`list.append()` changes the original list (mutation). `list = [new]` creates a new local variable (reassignment)."

### 3. Using `global` keyword
→ "You CAN use `global x` to modify a global, but it's almost always better to use parameters and return values."

## Vocabulary Introduced
- **local scope** — variables created inside a function
- **global scope** — variables created outside all functions
- **shadowing** — a local variable with the same name as a global one
- **mutation** — changing an object in place (e.g., list.append)
