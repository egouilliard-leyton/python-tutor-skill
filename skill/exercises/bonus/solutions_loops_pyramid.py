"""Solution variants for Bonus: Pyramid Builder"""

# --- Approach 1: Manual spacing ---

def build_pyramid(n):
    rows = []
    for i in range(n):
        spaces = " " * (n - 1 - i)
        stars = "*" * (2 * i + 1)
        rows.append(spaces + stars + spaces)
    return rows


# --- Approach 2: Using str.center() ---

def build_pyramid_v2(n):
    width = 2 * n - 1
    rows = []
    for i in range(n):
        stars = "*" * (2 * i + 1)
        rows.append(stars.center(width))
    return rows
