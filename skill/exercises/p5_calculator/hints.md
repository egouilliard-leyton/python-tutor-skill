# Project 5: Calculator — Hints

## Hint 1: Writing a math function
```python
def add(a, b):
    return a + b
```

## Hint 2: Getting numbers from user
```python
a = float(input("First number: "))
b = float(input("Second number: "))
```

## Hint 3: Division by zero check
```python
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b
```

## Hint 4: The menu loop
```python
while True:
    print("\n1. Add  2. Subtract  3. Multiply  4. Divide  5. Quit")
    choice = input("Choice: ")
    if choice == "5":
        print("Goodbye!")
        break
    a = float(input("First number: "))
    b = float(input("Second number: "))
    if choice == "1":
        print(f"Result: {add(a, b)}")
```
