"""
Translates Python errors into beginner-friendly explanations.

Usage:
    python3 error_translator.py <python_file>

Runs the file, and if it errors, outputs a JSON translation.
If it succeeds, outputs the normal stdout.
"""

import sys
import subprocess
import json
import re

TRANSLATIONS = {
    "SyntaxError": {
        "message": "Python found something unexpected in your code.",
        "common_causes": [
            "Missing colon (:) after if, elif, else, for, while, def",
            "Missing closing parenthesis, bracket, or quote",
            "Typo in a keyword (e.g., 'pritn' instead of 'print')",
        ],
    },
    "IndentationError": {
        "message": "Python uses spaces to know what code is 'inside' an if/loop/function. This line has the wrong amount of spaces.",
        "common_causes": [
            "Mixed tabs and spaces (use only spaces)",
            "Forgot to indent after a colon (:)",
            "Extra indentation where it shouldn't be",
        ],
    },
    "NameError": {
        "message": "Python doesn't recognize this name. Either it's a typo or you used it before creating it.",
        "common_causes": [
            "Variable name spelled differently than where you defined it",
            "Used a variable before assigning a value to it",
            "Forgot to import a module",
        ],
    },
    "TypeError": {
        "message": "You tried to do something with the wrong type of data.",
        "common_causes": [
            "Adding a number and a string together (use str() or int())",
            "Calling something that isn't a function",
            "Passing the wrong number of arguments to a function",
        ],
    },
    "IndexError": {
        "message": "You asked for an item at a position that doesn't exist. Remember, Python counts from 0!",
        "common_causes": [
            "List has 3 items (index 0, 1, 2) but you asked for index 3",
            "Empty list — no items to access at all",
            "Off-by-one error in a loop",
        ],
    },
    "ValueError": {
        "message": "The value you gave is the right type but doesn't make sense for the operation.",
        "common_causes": [
            "Trying to convert a non-numeric string to int (e.g., int('hello'))",
            "Unexpected input from the user",
        ],
    },
    "KeyError": {
        "message": "You tried to access a dictionary key that doesn't exist.",
        "common_causes": [
            "Typo in the key name",
            "Key hasn't been added to the dictionary yet",
            "Use .get(key) to safely check without crashing",
        ],
    },
    "AttributeError": {
        "message": "You tried to use a feature that doesn't exist on this type of thing.",
        "common_causes": [
            "Calling a method that doesn't exist (e.g., 'hello'.push() — strings don't have push)",
            "Variable is None when you expected something else",
            "Typo in the method name",
        ],
    },
    "FileNotFoundError": {
        "message": "Python can't find that file.",
        "common_causes": [
            "Filename is spelled wrong",
            "File is in a different folder",
            "Path uses wrong slashes",
        ],
    },
    "ModuleNotFoundError": {
        "message": "Python can't find that package/module.",
        "common_causes": [
            "Forgot to install it (run: pip install <name>)",
            "Typo in the import name",
            "Wrong Python environment",
        ],
    },
    "ZeroDivisionError": {
        "message": "You tried to divide by zero — that's mathematically impossible!",
        "common_causes": [
            "A variable used as a divisor is 0",
            "Add a check: if divisor != 0 before dividing",
        ],
    },
}


def parse_error(stderr_text):
    """Extract error type, message, file, and line from Python traceback."""
    lines = stderr_text.strip().split("\n")

    error_line = lines[-1] if lines else ""
    match = re.match(r"(\w+Error):?\s*(.*)", error_line)

    error_type = match.group(1) if match else "UnknownError"
    error_detail = match.group(2) if match else error_line

    # Find file and line number
    file_path = None
    line_num = None
    code_line = None
    for i, line in enumerate(lines):
        m = re.match(r'\s*File "(.+)", line (\d+)', line)
        if m:
            file_path = m.group(1)
            line_num = int(m.group(2))
            if i + 1 < len(lines) and not lines[i + 1].startswith("File"):
                code_line = lines[i + 1].strip()

    return {
        "error_type": error_type,
        "error_detail": error_detail,
        "file": file_path,
        "line": line_num,
        "code_line": code_line,
    }


def translate(parsed):
    """Produce a beginner-friendly translation."""
    error_type = parsed["error_type"]
    info = TRANSLATIONS.get(error_type, {
        "message": f"An error occurred: {error_type}",
        "common_causes": ["This is less common — read the error message carefully"],
    })

    result = {
        "python_says": f'{error_type}: {parsed["error_detail"]}',
        "this_means": info["message"],
        "line": parsed["line"],
        "code_at_line": parsed["code_line"],
        "common_causes": info["common_causes"],
        "question": f"Look at line {parsed['line']} — can you spot what might be wrong?",
    }
    return result


def run_file(filepath):
    """Run a Python file and return (success, stdout, stderr)."""
    proc = subprocess.run(
        [sys.executable, filepath],
        capture_output=True,
        text=True,
        timeout=10,
    )
    return proc.returncode == 0, proc.stdout, proc.stderr


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 error_translator.py <python_file>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        success, stdout, stderr = run_file(filepath)
    except subprocess.TimeoutExpired:
        print(json.dumps({
            "success": False,
            "translation": {
                "python_says": "TimeoutError: your program ran for more than 10 seconds",
                "this_means": "Your code is stuck in an infinite loop — it never stops running.",
                "common_causes": [
                    "A while loop whose condition never becomes False",
                    "Forgot to update the loop variable inside the loop",
                ],
                "question": "Check your while loop — does the condition ever become False?",
            }
        }))
        sys.exit(1)

    if success:
        print(json.dumps({"success": True, "output": stdout}))
    else:
        parsed = parse_error(stderr)
        translation = translate(parsed)
        print(json.dumps({"success": False, "translation": translation, "raw_error": stderr}))
