"""Solution variants for Lesson 8: Elif"""

# --- Solution A: elif chain top-down ---
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# --- Solution B: early returns without elif ---
# def get_grade(score):
#     if score >= 90: return "A"
#     if score >= 80: return "B"
#     if score >= 70: return "C"
#     if score >= 60: return "D"
#     return "F"
