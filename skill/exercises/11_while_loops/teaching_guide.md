# Lesson 11: While Loops — Teaching Guide

## Concept Introduction
"A while loop repeats code as long as a condition is True."

Analogy: "Eating chips: WHILE there are chips in the bag, keep eating. Bag empty? Stop."

## Prediction Question
"What happens if I write `while True: print('hello')`? (Don't run it!)"
→ "It prints forever — an infinite loop. The condition never becomes False."

## Common Mistakes
### 1. Infinite loop (forgetting n -= 1)
→ "Your loop runs forever because n never changes. You need to decrease n each time."

### 2. Off-by-one (while n >= 0 includes 0)
→ "You're including 0 in the countdown. Should it be > 0 or >= 1?"

### 3. Forgetting to add "Go!" after the loop
→ "The loop handles the numbers. 'Go!' should be added AFTER the loop ends."

## Hint Sequence
1. "Create an empty list. Use while n > 0 to keep going."
2. "Inside the loop: add n to the list, then subtract 1 from n"
3. "After the while loop ends, append 'Go!' to the list and return it"

## Vocabulary Introduced
- **while** — repeat as long as condition is True
- **infinite loop** — a loop that never ends (bad!)
- **n -= 1** — shorthand for n = n - 1
- **.append()** — add an item to the end of a list
