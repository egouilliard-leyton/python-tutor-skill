"""Solution variants for Lesson 23: Default Parameters"""

# --- Approach 1: Simple if checks ---

def format_message(text, uppercase=False, prefix=""):
    if uppercase:
        text = text.upper()
    if prefix:
        text = prefix + " " + text
    return text

def create_tag(name, color="blue", size="medium"):
    return f"{size} {color} tag: {name}"

def repeat_char(char, times=5):
    return char * times


# --- Approach 2: Using ternary expressions ---

def format_message_v2(text, uppercase=False, prefix=""):
    result = text.upper() if uppercase else text
    return f"{prefix} {result}" if prefix else result
