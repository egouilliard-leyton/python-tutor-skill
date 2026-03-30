# Project 2: Text Adventure Game

Build a choose-your-own-adventure game! The player reads a story and
makes choices that lead to different outcomes.

## What you'll build
A program where:
1. You describe a scene
2. The player chooses what to do
3. Different choices lead to different paths
4. There are at least 3 endings (win, lose, secret)

## What you'll use
- `print()` to tell the story
- `input()` to get the player's choice
- `if/elif/else` to branch the story
- Nested conditions for multi-level decisions
- `and/or` for complex conditions

## Steps (suggested order)
1. Write the opening scene and print it
2. Ask for the first choice (e.g., "Go left or right?")
3. Use if/elif/else to go to different scenes
4. Add a second decision point inside each branch
5. Create at least 3 different endings
6. Add a play-again loop (while loop preview!)

## Example run
```
=== The Mysterious Cave ===

You stand at the entrance of a dark cave.
A faint glow comes from the left passage.
Strange sounds come from the right.

Do you go [left] or [right]? left

You follow the glow and find a room full of crystals!
There's a small crystal and a large crystal.

Do you take the [small] crystal or the [large] crystal? large

The large crystal is too heavy! It crumbles in your hands
and the cave starts shaking...

GAME OVER - You scored 0 points!
```

## Bonus challenges
- Add an inventory system (store items in variables)
- Make some choices depend on previous choices
- Add a health or score system
- Add at least 5 different rooms
