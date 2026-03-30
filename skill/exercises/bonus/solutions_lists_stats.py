"""Solution variants for Bonus: List Statistics"""

# --- Approach 1: Simple and clear ---

def median(numbers):
    s = sorted(numbers)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    else:
        return (s[mid - 1] + s[mid]) / 2

def mode(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    best = numbers[0]
    for num, count in counts.items():
        if count > counts[best]:
            best = num
    return best

def range_of(numbers):
    return max(numbers) - min(numbers)


# --- Approach 2: mode using max() with key ---

def mode_v2(numbers):
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key=counts.get)
