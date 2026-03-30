"""Solution variants for Lesson 11: While Loops"""

# --- Solution A: standard while ---
def countdown(n):
    result = []
    while n > 0:
        result.append(n)
        n -= 1
    result.append("Go!")
    return result

# --- Solution B: using n = n - 1 ---
# def countdown(n):
#     result = []
#     while n >= 1:
#         result.append(n)
#         n = n - 1
#     result.append("Go!")
#     return result
