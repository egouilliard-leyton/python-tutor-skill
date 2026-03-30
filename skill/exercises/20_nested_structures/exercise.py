"""Solution variants for Lesson 20: Nested Structures"""

def get_names(students):
    return [s["name"] for s in students]

def best_student(students):
    top = students[0]
    for s in students:
        if s["grade"] > top["grade"]:
            top = s
    return top["name"]

def filter_by_subject(students, subject):
    return [s for s in students if s["subject"] == subject]

def average_grade(students):
    total = sum(s["grade"] for s in students)
    return round(total / len(students), 1)
