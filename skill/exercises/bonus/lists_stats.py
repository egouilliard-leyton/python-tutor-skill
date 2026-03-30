# ============================================
# Bonus: List Statistics
# ============================================
#
# GOAL: Write functions to calculate statistics from a list of numbers.
#
# FUNCTION 1: median(numbers)
#   - Return the median (middle value) of a list
#   - Sort the list first!
#   - If even length, return average of two middle values
#   - Example: median([3, 1, 2]) → 2
#   - Example: median([1, 2, 3, 4]) → 2.5
#
# FUNCTION 2: mode(numbers)
#   - Return the most common value
#   - If there's a tie, return any of the most common
#   - Example: mode([1, 2, 2, 3]) → 2
#
# FUNCTION 3: range_of(numbers)
#   - Return max - min
#   - Example: range_of([10, 3, 7]) → 7
#
# HINTS:
#   Hint 1: sorted() returns a new sorted list
#   Hint 2: len(list) // 2 gives the middle index
#   Hint 3: Use a dictionary to count occurrences for mode
#   Hint 4: max() and min() work on lists
#
# When done, run: python3 lists_stats.py
# ============================================

def median(numbers):
    # YOUR CODE HERE
    pass

def mode(numbers):
    # YOUR CODE HERE
    pass

def range_of(numbers):
    # YOUR CODE HERE
    pass


# --- Don't modify below this line ---
if __name__ == "__main__":
    print(median([3, 1, 2]))
    print(median([1, 2, 3, 4]))
    print(mode([1, 2, 2, 3, 3, 3]))
    print(range_of([10, 3, 7, 1]))
