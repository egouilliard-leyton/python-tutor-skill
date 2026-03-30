"""Solution variants for Lesson 3: Strings"""

# --- Solution A: indexing + concatenation + lower ---
def make_username(first, last):
    return (first[0] + last).lower()

# --- Solution B: f-string ---
# def make_username(first, last):
#     return f"{first[0]}{last}".lower()

# --- Solution C: separate lowering ---
# def make_username(first, last):
#     first_initial = first[0].lower()
#     last_lower = last.lower()
#     return first_initial + last_lower

# --- Solution D: format method ---
# def make_username(first, last):
#     return "{}{}".format(first[0], last).lower()
