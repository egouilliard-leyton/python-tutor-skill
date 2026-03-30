# ============================================
# Lesson 4: Numbers & Math — Tip Calculator
# ============================================
#
# GOAL: Calculate the total bill including tip.
#
# RULES:
#   Write a function calculate_tip(bill, tip_percent) that:
#   - Calculates the tip amount
#   - Returns the total (bill + tip) rounded to 2 decimal places
#   - tip_percent is a whole number (15 means 15%)
#
# EXAMPLES:
#   calculate_tip(50.00, 15)  → 57.5
#   calculate_tip(100.00, 20) → 120.0
#   calculate_tip(33.50, 18)  → 39.53
#
# HINTS:
#   Hint 1: 15% of something = something * 15 / 100
#   Hint 2: round(number, 2) rounds to 2 decimal places
#
# When done, save and run: python3 exercise.py
# Then ask Claude: /learn check
# ============================================

def calculate_tip(bill, tip_percent):
    # YOUR CODE HERE
    pass


# --- Don't modify below this line ---
if __name__ == "__main__":
    print(calculate_tip(50.00, 15))
    print(calculate_tip(100.00, 20))
    print(calculate_tip(33.50, 18))
