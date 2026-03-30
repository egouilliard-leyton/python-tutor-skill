"""Solution variants for Bonus: Word Counter"""

# --- Approach 1: Manual counting ---

def word_count(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts

def most_common(text):
    counts = word_count(text)
    best_word = ""
    best_count = 0
    for word, count in counts.items():
        if count > best_count:
            best_word = word
            best_count = count
    return best_word


# --- Approach 2: Using max() with key ---

def most_common_v2(text):
    counts = word_count(text)
    return max(counts, key=counts.get)
