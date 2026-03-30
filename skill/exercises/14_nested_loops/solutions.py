"""Solution variants for Lesson 14: Nested Loops"""

def times_table(n):
    rows = []
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            if row:
                row += "  "
            row += f"{i} x {j} = {i * j}"
        rows.append(row)
    return rows

# --- Solution B: join ---
# def times_table(n):
#     rows = []
#     for i in range(1, n + 1):
#         entries = [f"{i} x {j} = {i*j}" for j in range(1, n + 1)]
#         rows.append("  ".join(entries))
#     return rows
