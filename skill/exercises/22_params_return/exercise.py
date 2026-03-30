"""Solution variants for Lesson 22: Parameters & Return"""

# --- Approach 1: Simple and direct ---

def convert_f_to_c(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 1)

def convert_c_to_f(celsius):
    return round(celsius * 9/5 + 32, 1)

def convert_temp(value, from_unit):
    if from_unit == "F":
        return convert_f_to_c(value)
    else:
        return convert_c_to_f(value)


# --- Approach 2: Using a dictionary for dispatch ---

def convert_temp_v2(value, from_unit):
    converters = {
        "F": convert_f_to_c,
        "C": convert_c_to_f,
    }
    return converters[from_unit](value)
