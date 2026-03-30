"""Solution variants for Lesson 6: Booleans
Correct answers for predictions:
1. True   (10 > 5)
2. True   (3 == 3.0 — Python considers them equal)
3. False  ("hello" != "Hello" — case-sensitive!)
4. False  (7 != 7 is False — 7 IS equal to 7)
5. True   (1 >= 1 — it IS equal, and >= includes equal)
6. True   (0 == False — 0 is "falsy" in Python)
7. False  ("" == False — empty string is falsy but not == False)
8. False  (10 < 10 — not strictly less than)

#7 is the tricky one. "" is "falsy" (bool("") == False)
but "" == False is False because == compares values directly.
"""
