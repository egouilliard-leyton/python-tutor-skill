"""Solution variants for Lesson 4: Numbers"""

# --- Solution A: direct calculation ---
def calculate_tip(bill, tip_percent):
    return round(bill + bill * tip_percent / 100, 2)

# --- Solution B: separate tip variable ---
# def calculate_tip(bill, tip_percent):
#     tip = bill * tip_percent / 100
#     total = bill + tip
#     return round(total, 2)

# --- Solution C: multiply by (1 + rate) ---
# def calculate_tip(bill, tip_percent):
#     return round(bill * (1 + tip_percent / 100), 2)
