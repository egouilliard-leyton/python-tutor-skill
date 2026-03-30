# Project 1: Mad Libs Generator

Build a fill-in-the-blank story game! Ask the user for different types
of words and plug them into a funny story template.

## What you'll build
A program that:
1. Asks the user for words (nouns, verbs, adjectives, etc.)
2. Plugs those words into a story template
3. Prints the completed (usually hilarious) story

## What you'll use
- `print()` to display text
- Variables to store the user's words
- `input()` to ask for words
- f-strings to build the final story

## Steps (suggested order)
1. Write a story template with blanks (just print it with placeholder words first)
2. Replace each placeholder with an `input()` call that asks for the right type of word
3. Store each answer in a variable with a clear name
4. Print the completed story using f-strings
5. Test it — make sure it reads like a (funny) sentence

## Example run
```
=== Mad Libs: The Adventure ===

Give me a noun: dragon
Give me an adjective: sparkly
Give me a verb (past tense): danced
Give me a place: supermarket
Give me a food: pizza

Here's your story:

One day, a sparkly dragon danced all the way to the supermarket.
When it arrived, it ordered a giant pizza and everyone cheered!
```

## Bonus challenges
- Add 3+ different story templates and let the user pick one
- Save the completed story to a .txt file
- Let the user play again without restarting the program
