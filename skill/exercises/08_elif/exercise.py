# ============================================
# Lesson 8: Elif Chains — Grade Calculator
# ============================================
#
# GOAL: Convert a score to a letter grade.
#
# RULES:
#   Write a function get_grade(score) that returns:
#   - "A" for 90-100
#   - "B" for 80-89
#   - "C" for 70-79
#   - "D" for 60-69
#   - "F" for below 60
#
# EXAMPLES:
#   get_grade(95) → "A"
#   get_grade(83) → "B"
#   get_grade(71) → "C"
#   get_grade(65) → "D"
#   get_grade(45) → "F"
#
# HINTS:
#   Hint 1: Start with the highest: if score >= 90
#   Hint 2: Use elif for each next range
#
# When done, save and run: python3 exercise.py
# Then ask Claude: /learn check
# ============================================

def get_grade(score):
    # YOUR CODE HERE
    pass


# --- Don't modify below this line ---
if __name__ == "__main__":
    print(get_grade(95))
    print(get_grade(83))
    print(get_grade(71))
    print(get_grade(65))
    print(get_grade(45))
