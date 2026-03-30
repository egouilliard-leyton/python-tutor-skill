# ============================================
# Lesson 7: If/Else — Can You Vote?
# ============================================
#
# GOAL: Check if someone is old enough to vote.
#
# RULES:
#   Write a function can_vote(age) that:
#   - Returns "You can vote!" if age is 18 or older
#   - Returns "Not yet! X more years to go." if under 18
#     (X = the actual number of years left)
#
# EXAMPLES:
#   can_vote(20) → "You can vote!"
#   can_vote(18) → "You can vote!"
#   can_vote(15) → "Not yet! 3 more years to go."
#   can_vote(7)  → "Not yet! 11 more years to go."
#
# HINTS:
#   Hint 1: Use if and else
#   Hint 2: if age >= 18:
#
# When done, save and run: python3 exercise.py
# Then ask Claude: /learn check
# ============================================

def can_vote(age):
    # YOUR CODE HERE
    pass


# --- Don't modify below this line ---
if __name__ == "__main__":
    print(can_vote(20))
    print(can_vote(18))
    print(can_vote(15))
    print(can_vote(7))
