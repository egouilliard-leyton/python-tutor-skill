# ============================================
# Lesson 13: Break & Continue — Fix the Bugs!
# ============================================
#
# GOAL: Fix 3 bugs in this password checker.
#
# The function find_valid_passwords(passwords) should:
#   - Skip passwords shorter than 6 characters (use continue)
#   - Stop checking if it finds "quit" (use break)
#   - Return a list of valid passwords (length >= 6)
#
# EXAMPLES:
#   find_valid_passwords(["hi", "secret123", "ab", "longpass"])
#   → ["secret123", "longpass"]
#
#   find_valid_passwords(["hello1", "quit", "never_seen"])
#   → ["hello1"]
#
# When done, save and run: python3 exercise.py
# Then ask Claude: /learn check
# ============================================

def find_valid_passwords(passwords):
    valid = []
    for pw in passwords:
        # BUG 1: Should STOP when we see "quit", not skip it
        if pw == "quit":
            continue

        # BUG 2: Should SKIP short passwords, not stop
        if len(pw) < 6:
            break

        # BUG 3: Should add to 'valid' list, not print
        print(pw)

    return valid


# --- Don't modify below this line ---
if __name__ == "__main__":
    print(find_valid_passwords(["hi", "secret123", "ab", "longpass"]))
    print(find_valid_passwords(["hello1", "quit", "never_seen"]))
    print(find_valid_passwords(["short", "quitnow", "valid1"]))
