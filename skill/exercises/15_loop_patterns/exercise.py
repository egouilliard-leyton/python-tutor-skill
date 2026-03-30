# ============================================
# Lesson 15: Loop Patterns — Data Analyzer
# ============================================
#
# GOAL: Write 3 functions that analyze a list of numbers.
#
# FUNCTION 1: find_total(numbers)
#   - Return the sum of all numbers (don't use built-in sum())
#
# FUNCTION 2: find_max(numbers)
#   - Return the largest number (don't use built-in max())
#
# FUNCTION 3: count_above(numbers, threshold)
#   - Return how many numbers are above the threshold
#
# EXAMPLES:
#   find_total([1, 2, 3, 4, 5])     → 15
#   find_max([3, 7, 2, 9, 1])       → 9
#   count_above([1, 5, 3, 8, 2], 3) → 2  (5 and 8 are above 3)
#
# HINTS:
#   Hint 1: For total — start with 0, add each number
#   Hint 2: For max — start with the first number, compare each
#   Hint 3: For count — start with 0, add 1 when condition is met
#
# When done, save and run: python3 exercise.py
# Then ask Claude: /learn check
# ============================================

def find_total(numbers):
    # YOUR CODE HERE
    pass

def find_max(numbers):
    # YOUR CODE HERE
    pass

def count_above(numbers, threshold):
    # YOUR CODE HERE
    pass


# --- Don't modify below this line ---
if __name__ == "__main__":
    print(find_total([1, 2, 3, 4, 5]))
    print(find_max([3, 7, 2, 9, 1]))
    print(count_above([1, 5, 3, 8, 2], 3))
