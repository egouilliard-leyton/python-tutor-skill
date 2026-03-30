# ============================================
# Lesson 14: Nested Loops — Multiplication Table
# ============================================
#
# GOAL: Build a multiplication table.
#
# RULES:
#   Write a function times_table(n) that:
#   - Returns a list of strings, one per row
#   - Each row shows: "i x j = result" for j from 1 to n
#   - Rows are for i from 1 to n
#
# EXAMPLES:
#   times_table(3) →
#   ["1 x 1 = 1  1 x 2 = 2  1 x 3 = 3",
#    "2 x 1 = 2  2 x 2 = 4  2 x 3 = 6",
#    "3 x 1 = 3  3 x 2 = 6  3 x 3 = 9"]
#
# HINTS:
#   Hint 1: Use two for loops — outer for rows, inner for columns
#   Hint 2: Build each row as a string, then add it to the result list
#   Hint 3: Separate entries with two spaces "  "
#
# When done, save and run: python3 exercise.py
# Then ask Claude: /learn check
# ============================================

def times_table(n):
    # YOUR CODE HERE
    pass


# --- Don't modify below this line ---
if __name__ == "__main__":
    for row in times_table(5):
        print(row)
