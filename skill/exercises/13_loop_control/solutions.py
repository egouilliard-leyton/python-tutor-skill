"""Solution variants for Lesson 13: Loop Control
Fixes: 1. continue→break for quit, 2. break→continue for short, 3. print→append
"""

def find_valid_passwords(passwords):
    valid = []
    for pw in passwords:
        if pw == "quit":
            break
        if len(pw) < 6:
            continue
        valid.append(pw)
    return valid
