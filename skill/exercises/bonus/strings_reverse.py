# ============================================
# Bonus: String Reversal & Palindromes
# ============================================
#
# GOAL: Practice string manipulation with two classic problems.
#
# FUNCTION 1: reverse_string(text)
#   - Return the text reversed
#   - Example: reverse_string("hello") → "olleh"
#
# FUNCTION 2: is_palindrome(text)
#   - Return True if text reads the same forwards and backwards
#   - Ignore case (upper/lower shouldn't matter)
#   - Example: is_palindrome("Racecar") → True
#   - Example: is_palindrome("hello") → False
#
# HINTS:
#   Hint 1: text[::-1] reverses a string
#   Hint 2: Or use a loop to build it backwards
#   Hint 3: .lower() makes comparison case-insensitive
#
# When done, run: python3 strings_reverse.py
# ============================================

def reverse_string(text):
    # YOUR CODE HERE
    pass

def is_palindrome(text):
    # YOUR CODE HERE
    pass


# --- Don't modify below this line ---
if __name__ == "__main__":
    print(reverse_string("hello"))
    print(reverse_string("Python"))
    print(is_palindrome("racecar"))
    print(is_palindrome("Racecar"))
    print(is_palindrome("hello"))
