# ============================================
# Lesson 3: Strings — Username Generator
# ============================================
#
# GOAL: Build a username from a first and last name.
#
# RULES:
#   Write a function make_username(first, last) that:
#   - Takes first name and last name
#   - Returns: first letter of first name + full last name
#   - All lowercase
#
# EXAMPLES:
#   make_username("Charles", "Gouilliard") → "cgouilliard"
#   make_username("Ada", "Lovelace")       → "alovelace"
#   make_username("JEAN", "DUPONT")        → "jdupont"
#
# HINTS:
#   Hint 1: Get the first character with name[0]
#   Hint 2: Join strings with +
#   Hint 3: Make lowercase with .lower()
#
# When done, save and run: python3 exercise.py
# Then ask Claude: /learn check
# ============================================

def make_username(first, last):
    # YOUR CODE HERE
    pass


# --- Don't modify below this line ---
if __name__ == "__main__":
    print(make_username("Charles", "Gouilliard"))
    print(make_username("Ada", "Lovelace"))
    print(make_username("JEAN", "DUPONT"))
