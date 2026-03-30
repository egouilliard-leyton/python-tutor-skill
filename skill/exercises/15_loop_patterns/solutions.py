"""Solution variants for Lesson 15: Loop Patterns"""

def find_total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def find_max(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest

def count_above(numbers, threshold):
    count = 0
    for n in numbers:
        if n > threshold:
            count += 1
    return count

# --- Solution B: more concise ---
# def find_total(numbers):
#     total = 0
#     for n in numbers:
#         total = total + n
#     return total
#
# def find_max(numbers):
#     biggest = numbers[0]
#     for n in numbers[1:]:
#         if n > biggest:
#             biggest = n
#     return biggest
#
# def count_above(numbers, threshold):
#     count = 0
#     for n in numbers:
#         if n > threshold:
#             count = count + 1
#     return count
