"""Solution variants for Bonus: String Reversal & Palindromes"""

# --- Approach 1: Slicing ---

def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    lower = text.lower()
    return lower == lower[::-1]


# --- Approach 2: Loop ---

def reverse_string_v2(text):
    result = ""
    for char in text:
        result = char + result
    return result

def is_palindrome_v2(text):
    lower = text.lower()
    return lower == reverse_string_v2(lower)
