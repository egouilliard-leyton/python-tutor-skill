# Lesson 4: Numbers & Math — Teaching Guide

## Concept Introduction
"Python is a calculator that never makes mistakes. It handles whole numbers (integers like 42) and decimal numbers (floats like 3.14). Let's build something practical."

## Prediction Question
"What do you think `10 / 3` gives? And `10 // 3`? Try both — they're different!"

## Common Mistakes

### 1. Integer division instead of float division
```python
tip = bill * tip_percent // 100  # Loses decimal precision
```
→ "// rounds DOWN to a whole number. Use / for regular division."

### 2. Forgetting round()
```python
return bill + bill * tip_percent / 100  # 39.529999999...
```
→ "Floating point math can be messy. round(number, 2) cleans it up."

### 3. Wrong order of operations
```python
return round(bill + bill * tip_percent) / 100  # Wrong!
```
→ "Python follows PEMDAS. Use parentheses to control the order."

### 4. Tip percent as decimal
```python
return round(bill + bill * tip_percent, 2)  # If tip_percent=15, this adds 15x the bill
```
→ "15 means 15%, which is 15/100 = 0.15. Divide by 100 first."

## Hint Sequence
1. "To get 15% of a number: number * 15 / 100"
2. "Calculate tip first, then add it to the bill"
3. "round(your_total, 2) cleans up the decimal places. Return that."

## Vocabulary Introduced
- **int** — whole number (42, -7, 0)
- **float** — decimal number (3.14, 0.5)
- **operator** — math symbol: + - * / // % **
- **round()** — built-in function to round a number
