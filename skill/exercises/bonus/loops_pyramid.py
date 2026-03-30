# ============================================
# Bonus: Pyramid Builder
# ============================================
#
# GOAL: Use loops and string operations to build a pyramid.
#
# FUNCTION: build_pyramid(n)
#   - Return a list of strings forming a pyramid with n rows
#   - Each row has an odd number of stars, centered
#
# EXAMPLES:
#   build_pyramid(1) → ["*"]
#   build_pyramid(2) → [" * ", "***"]
#   build_pyramid(3) → ["  *  ", " *** ", "*****"]
#   build_pyramid(4) → ["   *   ", "  ***  ", " ***** ", "*******"]
#
# PATTERN:
#   Row 0: 1 star,  (n-1) spaces on each side
#   Row 1: 3 stars, (n-2) spaces on each side
#   Row i: (2*i+1) stars, (n-1-i) spaces on each side
#
# HINTS:
#   Hint 1: "*" * 5 gives "*****"
#   Hint 2: " " * 3 gives "   "
#   Hint 3: Build each row as: spaces + stars + spaces
#
# When done, run: python3 loops_pyramid.py
# ============================================

def build_pyramid(n):
    # YOUR CODE HERE
    pass


# --- Don't modify below this line ---
if __name__ == "__main__":
    for row in build_pyramid(5):
        print(f"|{row}|")
