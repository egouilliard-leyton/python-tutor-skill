# ============================================
# Lesson 9: Logical Operators — Fix the Bugs!
# ============================================
#
# GOAL: This code has 3 bugs. Find and fix them all.
#
# The function should return True ONLY if:
#   - height is at least 120 cm  AND
#   - age is at least 8
#
# EXAMPLES:
#   can_ride(130, 10) → True
#   can_ride(110, 10) → False  (too short)
#   can_ride(130, 6)  → False  (too young)
#   can_ride(100, 5)  → False  (both fail)
#   can_ride(120, 8)  → True   (exactly enough)
#
# When done, save and run: python3 exercise.py
# Then ask Claude: /learn check
# ============================================

def can_ride(height, age):
    # BUG 1: The logic operator is wrong
    if height >= 120 or age >= 8:
        return True
    # BUG 2: There's a syntax error on this line
    elif height < 120 and age = 8:
        return False
    # BUG 3: This return is wrong for the remaining case
    return True


# --- Don't modify below this line ---
if __name__ == "__main__":
    print(can_ride(130, 10))   # Should be True
    print(can_ride(110, 10))   # Should be False
    print(can_ride(130, 6))    # Should be False
    print(can_ride(100, 5))    # Should be False
    print(can_ride(120, 8))    # Should be True
