"""Solution variants for Lesson 9: Logical Operators
Bug fixes:
  1. 'or' → 'and' (BOTH conditions must be true)
  2. 'age = 8' → 'age == 8' or remove the elif entirely
  3. 'return True' → 'return False' (or just use if/else)
"""

# --- Solution A: simple if/else ---
def can_ride(height, age):
    if height >= 120 and age >= 8:
        return True
    else:
        return False

# --- Solution B: direct return ---
# def can_ride(height, age):
#     return height >= 120 and age >= 8
