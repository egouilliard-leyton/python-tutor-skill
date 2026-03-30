"""Solution variants for Lesson 7: If/Else"""

# --- Solution A: standard if/else ---
def can_vote(age):
    if age >= 18:
        return "You can vote!"
    else:
        return f"Not yet! {18 - age} more years to go."

# --- Solution B: early return ---
# def can_vote(age):
#     if age >= 18:
#         return "You can vote!"
#     return f"Not yet! {18 - age} more years to go."

# --- Solution C: ternary (advanced) ---
# def can_vote(age):
#     return "You can vote!" if age >= 18 else f"Not yet! {18 - age} more years to go."

# --- Solution D: variable for years ---
# def can_vote(age):
#     if age >= 18:
#         return "You can vote!"
#     else:
#         years_left = 18 - age
#         return "Not yet! " + str(years_left) + " more years to go."
