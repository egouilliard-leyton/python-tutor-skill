# ============================================
# Lesson 24: Scope — Predict the Output
# ============================================
#
# GOAL: Understand where variables live (local vs global).
#
# RULES:
#   - For each example, predict what will be printed
#   - Write your prediction as a comment
#   - Then run the file to check if you were right
#   - Try to get ALL of them correct!
#
# When done, ask Claude: /learn check
# ============================================

# Write your prediction next to each one, then run to verify.

# --- Example 1: Local variable ---
# My prediction: ___
def example1():
    x = 10
    return x

print("1:", example1())

# --- Example 2: Same name, different scope ---
# My prediction for 2a: ___
# My prediction for 2b: ___
y = "global"

def example2():
    y = "local"
    return y

print("2a:", example2())
print("2b:", y)

# --- Example 3: Reading a global variable ---
# My prediction: ___
z = 42

def example3():
    return z

print("3:", example3())

# --- Example 4: Function parameter vs global ---
# My prediction: ___
name = "Charles"

def example4(name):
    return f"Hello, {name}!"

print("4:", example4("World"))

# --- Example 5: Variable only exists inside function ---
# My prediction: ___
def example5():
    secret = "hidden"
    return "done"

example5()
try:
    print("5:", secret)
except NameError:
    print("5: NameError — 'secret' doesn't exist here!")

# --- Example 6: Mutable objects (lists) are tricky! ---
# My prediction for 6a: ___
# My prediction for 6b: ___
fruits = ["apple", "banana"]

def example6(items):
    items.append("cherry")
    return len(items)

print("6a:", example6(fruits))
print("6b:", fruits)

# --- Example 7: Reassignment vs mutation ---
# My prediction for 7a: ___
# My prediction for 7b: ___
numbers = [1, 2, 3]

def example7(nums):
    nums = [10, 20, 30]
    return nums

print("7a:", example7(numbers))
print("7b:", numbers)

# --- YOUR TURN ---
# Write 2 scope examples of your own below!
# Make one that shows local scope and one that shows
# the difference between mutation and reassignment.

