# Project 2: Text Adventure — Hints

## Hint 1: Structure
Think of your game as a tree — each choice splits into branches.

## Hint 2: Start with one path
Get the "left" path fully working with 2 scenes before adding "right".

## Hint 3: Handling bad input
```python
choice = input("Go [left] or [right]? ").lower()
if choice == "left":
    ...
elif choice == "right":
    ...
else:
    print("Please type 'left' or 'right'")
```

## Hint 4: Adding endings
Each leaf of your tree should print a clear ending message.
