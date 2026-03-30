"""Solution variants for Lesson 12: FizzBuzz"""

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

# --- Solution B: string building ---
# def fizzbuzz(n):
#     result = []
#     for i in range(1, n + 1):
#         s = ""
#         if i % 3 == 0: s += "Fizz"
#         if i % 5 == 0: s += "Buzz"
#         result.append(s or i)
#     return result
