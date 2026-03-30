# Lesson 23: Default Parameters — Teaching Guide

## Concept Introduction
"Default parameters let you make functions flexible — they work with just the basics, but you CAN customize them."

Analogy: "Ordering a coffee. By default you get medium, hot, with no extras. But you CAN ask for large, iced, with oat milk."

## Visualization
```
  def greet(name, greeting="Hello"):
                         ^^^^^^^^
                         default value — used if you don't provide one

  greet("Charles")           → uses "Hello"
  greet("Charles", "Hey")   → uses "Hey"
```

## Prediction Question
"If I write `def f(x, y=10): return x + y`, what does `f(5)` give? What about `f(5, 20)`?"

## Common Mistakes
### 1. Putting defaults before required params
→ "`def f(x=5, y)` is an error! Defaults must come AFTER required parameters."

### 2. Thinking defaults are fixed
→ "The default is just a fallback. You can always override it when calling."

### 3. Forgetting the keyword syntax
→ "`format_message('hi', prefix='>')` skips uppercase and sets prefix directly."

## Vocabulary Introduced
- **default parameter** — a parameter with a fallback value
- **keyword argument** — passing a value by name: `f(prefix=">>")`
- **positional argument** — passing a value by position: `f("hi", True)`
