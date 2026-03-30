# ============================================
# Lesson 10: Nested Conditions — Movie Ticket Pricer
# ============================================
#
# GOAL: Calculate ticket price with multiple discount rules.
#
# RULES:
#   Write a function ticket_price(age, is_student, day) that:
#   - Base: child (under 12) = 6, adult (12-64) = 12, senior (65+) = 8
#   - Students get 2 off the adult price (only applies to ages 12-64)
#   - On "tuesday", everyone gets 2 off their price
#   - Minimum price is always 4 (no lower)
#
# EXAMPLES:
#   ticket_price(10, False, "monday")   → 6
#   ticket_price(25, True,  "monday")   → 10
#   ticket_price(25, False, "tuesday")  → 10
#   ticket_price(25, True,  "tuesday")  → 8
#   ticket_price(70, False, "tuesday")  → 6
#   ticket_price(8,  False, "tuesday")  → 4
#
# HINTS:
#   Hint 1: First figure out the base price from age
#   Hint 2: Then apply discounts one at a time
#   Hint 3: max(price, 4) ensures minimum of 4
#
# When done, save and run: python3 exercise.py
# Then ask Claude: /learn check
# ============================================

def ticket_price(age, is_student, day):
    # YOUR CODE HERE
    pass


# --- Don't modify below this line ---
if __name__ == "__main__":
    print(ticket_price(10, False, "monday"))
    print(ticket_price(25, True,  "monday"))
    print(ticket_price(25, False, "tuesday"))
    print(ticket_price(25, True,  "tuesday"))
    print(ticket_price(70, False, "tuesday"))
    print(ticket_price(8,  False, "tuesday"))
