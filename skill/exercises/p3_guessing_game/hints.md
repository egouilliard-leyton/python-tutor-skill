# Project 3: Guessing Game — Hints

## Hint 1: Start without the loop
Get one guess working first (steps 1-4), then add the while loop.

## Hint 2: The while loop structure
```python
while guess != answer:
    guess = int(input("Your guess: "))
    # compare and print hint
```

## Hint 3: Counting guesses
```python
count = 0
while guess != answer:
    count += 1
    # ...
print(f"You got it in {count} guesses!")
```

## Hint 4: Play again
```python
play = "yes"
while play == "yes":
    # ... entire game ...
    play = input("Play again? (yes/no): ")
```
