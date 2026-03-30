# ============================================
# Lesson 12: For Loops — FizzBuzz
# ============================================
#
# GOAL: The classic FizzBuzz challenge!
#
# RULES:
#   Write a function fizzbuzz(n) that returns a list where:
#   - For multiples of 3: "Fizz"
#   - For multiples of 5: "Buzz"
#   - For multiples of both 3 and 5: "FizzBuzz"
#   - For everything else: the number itself
#   - Count from 1 to n (inclusive)
#
# EXAMPLES:
#   fizzbuzz(5)  → [1, 2, "Fizz", 4, "Buzz"]
#   fizzbuzz(15) → [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
#                   11, "Fizz", 13, 14, "FizzBuzz"]
#
# HINTS:
#   Hint 1: Use for i in range(1, n + 1)
#   Hint 2: Check "both" first (% 3 == 0 and % 5 == 0)
#   Hint 3: The % operator gives the remainder: 9 % 3 → 0
#
# When done, save and run: python3 exercise.py
# Then ask Claude: /learn check
# ============================================

def fizzbuzz(n):
    # YOUR CODE HERE
    pass


# --- Don't modify below this line ---
if __name__ == "__main__":
    print(fizzbuzz(15))
