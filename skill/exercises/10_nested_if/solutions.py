"""Solution variants for Lesson 10: Nested Conditions"""

# --- Solution A: step-by-step ---
def ticket_price(age, is_student, day):
    if age < 12:
        price = 6
    elif age >= 65:
        price = 8
    else:
        price = 12
        if is_student:
            price -= 2
    if day == "tuesday":
        price -= 2
    return max(price, 4)

# --- Solution B: all-in-one ---
# def ticket_price(age, is_student, day):
#     price = 6 if age < 12 else (8 if age >= 65 else (10 if is_student else 12))
#     if day == "tuesday":
#         price -= 2
#     return max(price, 4)
