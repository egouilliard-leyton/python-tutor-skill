# ============================================
# Bonus: Word Counter
# ============================================
#
# GOAL: Use dictionaries to count words in text.
#
# FUNCTION 1: word_count(text)
#   - Return a dictionary of {word: count}
#   - Convert to lowercase first
#   - Example: word_count("hi hi hello") → {"hi": 2, "hello": 1}
#
# FUNCTION 2: most_common(text)
#   - Return the most frequent word in the text
#   - Example: most_common("the cat and the dog") → "the"
#
# HINTS:
#   Hint 1: text.lower().split() gives a list of lowercase words
#   Hint 2: dict.get(key, 0) returns 0 if key doesn't exist yet
#   Hint 3: most_common can call word_count and then find the max
#
# When done, run: python3 dict_word_count.py
# ============================================

def word_count(text):
    # YOUR CODE HERE
    pass

def most_common(text):
    # YOUR CODE HERE
    pass


# --- Don't modify below this line ---
if __name__ == "__main__":
    print(word_count("hi hi hello world hello"))
    print(most_common("the cat and the dog and the fish"))
