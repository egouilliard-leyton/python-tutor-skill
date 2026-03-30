# Project 3: Number Guessing Game

Build a game where the computer picks a random number and the player
tries to guess it with hints!

## What you'll build
A program where:
1. Computer picks a random number (1 to 100)
2. Player guesses a number
3. Computer says "higher" or "lower"
4. Repeat until the player gets it right
5. Count how many guesses it took

## What you'll use
- `import random` and `random.randint()`
- `while` loops (keep guessing until correct)
- `if/elif/else` (compare guess to answer)
- `input()` and `int()` (get and convert guess)
- Variables (counter, answer, guess)

## Steps (suggested order)
1. Import random and generate a number: `answer = random.randint(1, 100)`
2. Print it (temporarily!) to test: `print(f"DEBUG: {answer}")`
3. Get one guess from the user with input() and int()
4. Compare the guess: too high, too low, or correct
5. Wrap it in a while loop: `while guess != answer:`
6. Add a guess counter (start at 0, add 1 each guess)
7. Print how many guesses when they win
8. Remove the DEBUG print!
9. Ask "Play again?" with another while loop

## Example run
```
=== Number Guessing Game ===
I'm thinking of a number between 1 and 100.

Your guess: 50
Too high! Try lower.

Your guess: 25
Too low! Try higher.

Your guess: 37
Too low! Try higher.

Your guess: 42
Correct! You got it in 4 guesses!

Play again? (yes/no): no
Thanks for playing!
```

## Bonus challenges
- Add difficulty levels (easy: 1-10, medium: 1-100, hard: 1-1000)
- Add a max guess limit (e.g., 7 tries)
- Track and display the best score across games
- Add hints: "You're getting warmer!" when closer
