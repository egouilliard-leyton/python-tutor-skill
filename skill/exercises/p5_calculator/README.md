# Project 5: Calculator

Build a menu-driven calculator that uses functions for each operation!

## What you'll build
A program where:
1. User sees a menu: Add, Subtract, Multiply, Divide, Quit
2. User picks an operation
3. User enters two numbers
4. Program shows the result
5. Loop until the user quits

## What you'll use
- Functions (one per math operation)
- Parameters and return values
- `while` loops (keep showing the menu)
- `input()` and `float()` (get and convert numbers)
- `if/elif/else` (handle menu choices)

## Steps (suggested order)
1. Write `add(a, b)` — return a + b
2. Write `subtract(a, b)` — return a - b
3. Write `multiply(a, b)` — return a * b
4. Write `divide(a, b)` — return a / b (watch out for zero!)
5. Write the main menu loop
6. Get two numbers from the user with input() and float()
7. Call the right function and print the result
8. Handle division by zero with an if check

## Example run
```
=== Calculator ===
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Choice: 1
First number: 10
Second number: 3
10.0 + 3.0 = 13.0

Choice: 4
First number: 10
Second number: 0
Cannot divide by zero!

Choice: 5
Goodbye!
```

## Bonus challenges
- Add a power function (exponentiation)
- Add a history feature that shows past calculations
- Let the user use the previous result as input ("ans")
- Add square root (only needs one number!)
