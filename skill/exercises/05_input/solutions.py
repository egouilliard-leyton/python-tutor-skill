"""Solution variants for Lesson 5: User Input"""

# --- Solution A: f-string ---
name = input("What is your name? ")
birth_year = input("What year were you born? ")
age = 2026 - int(birth_year)
print(f"Hello {name}! You are {age} years old.")

# --- Solution B: inline conversion ---
# name = input("What is your name? ")
# age = 2026 - int(input("What year were you born? "))
# print(f"Hello {name}! You are {age} years old.")

# --- Solution C: concatenation ---
# name = input("What is your name? ")
# birth_year = input("What year were you born? ")
# age = 2026 - int(birth_year)
# print("Hello " + name + "! You are " + str(age) + " years old.")
