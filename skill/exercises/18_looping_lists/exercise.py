"""Solution variants for Lesson 18: Looping Lists"""

def print_roster(names):
    lines = []
    for i, name in enumerate(names, 1):
        lines.append(f"{i}. {name}")
    return "\n".join(lines)

def find_passing(names, scores):
    passing = []
    for name, score in zip(names, scores):
        if score >= 60:
            passing.append(name)
    return passing

def pair_names_scores(names, scores):
    return [f"{name}: {score}" for name, score in zip(names, scores)]
