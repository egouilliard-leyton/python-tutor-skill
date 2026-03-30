"""Solution variants for Lesson 25: Function Composition"""

# --- Approach 1: Step by step ---

def clean_text(text):
    return text.strip().lower()

def extract_words(text):
    return text.split()

def count_unique(words):
    return len(set(words))

def process_text(text):
    cleaned = clean_text(text)
    words = extract_words(cleaned)
    return count_unique(words)


# --- Approach 2: One-liner pipeline ---

def process_text_v2(text):
    return count_unique(extract_words(clean_text(text)))


# --- Approach 3: count_unique without set ---

def count_unique_v2(words):
    seen = []
    for word in words:
        if word not in seen:
            seen.append(word)
    return len(seen)
