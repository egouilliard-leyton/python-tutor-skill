<div align="center">

# 🐍 Python Tutor — Claude Code Skill

**Learn Python the right way — with an AI tutor that never gives you the answer.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-D97706?style=for-the-badge&logo=anthropic&logoColor=white)](https://claude.ai/claude-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Exercises](https://img.shields.io/badge/Exercises-25+-blue?style=for-the-badge)](#curriculum)
[![Tests](https://img.shields.io/badge/Tests-270_passing-brightgreen?style=for-the-badge)](#exercises)

<br>

A [Claude Code](https://claude.ai/claude-code) skill that turns your terminal into a personalized Python classroom. Write real code in real files, get Socratic feedback, and build projects — all with persistent memory that adapts to how *you* learn.

<br>

**No copy-paste. No hand-holding. Real skills.**

</div>

---

## Why This Exists

Most AI coding tools **write code for you**. That's great for productivity — terrible for learning.

This skill flips the model: **you write the code**, and Claude acts as a patient teacher who reads your work, runs tests, and guides you with questions — never answers. It remembers what you struggle with, tracks every attempt, and adapts the curriculum to your pace.

Built for absolute beginners. No prior coding experience needed.

## How It Works

```
┌─────────────────────────────────────────────────┐
│  You write Python          Claude teaches        │
│  in real .py files    →    reads your code       │
│  in VS Code/Cursor    →    runs tests silently   │
│                       →    gives Socratic hints   │
│                       →    tracks your progress   │
│                       →    NEVER writes your code │
└─────────────────────────────────────────────────┘
```

1. **`/learn start`** — onboarding: profile, environment check, first exercise
2. **You write code** in VS Code/Cursor — real `.py` files, not a chat window
3. **`/learn check`** — Claude runs your code + tests, gives feedback without spoiling the answer
4. **`/learn hint`** — graduated hints (vague → specific), only when you're stuck
5. **`/learn next`** — advance when you're ready. Curriculum adapts to you.

## Quick Start

```bash
# Clone the repo
git clone https://github.com/egouilliard-leyton/python-tutor-skill.git
cd python-tutor-skill

# Install (creates symlink — updates are instant)
bash install.sh

# Open Claude Code and start learning
/learn start
```

**Requirements:** Python 3.10+, [Claude Code](https://claude.ai/claude-code), VS Code or Cursor

## Features

<table>
<tr>
<td width="50%">

### 🎓 Socratic Teaching
Never gives the answer. Uses graduated hints (4 levels), prediction questions, and "what do you think went wrong?" to build real understanding.

### 📊 Attempt Tracking
Every `/learn check` logs a full snapshot: your code, test results, error types, hints used. Watch your progression from 0/5 → 3/5 → 5/5.

### 🧠 Persistent Memory
Remembers your name, pace, strengths, weaknesses, and error patterns across sessions. Never asks the same setup question twice.

</td>
<td width="50%">

### 🔄 Spaced Repetition
Concepts decay over time. The skill auto-reviews topics you haven't practiced, using proven memory science to prevent forgetting.

### 📈 Adaptive Difficulty
Comfort scores (0-100) per concept. Aced it? Skip ahead. Struggling? Extra practice, different analogies, sub-problems.

### 🏆 Gamification
XP, levels (Novice → Expert), achievements, streaks. Motivation without distraction.

</td>
</tr>
</table>

## Curriculum

8 modules, 40 lessons, from `print("Hello")` to building real projects.

| Module | Topic | Lessons | Project |
|:---:|---|:---:|---|
| 1 | **First Steps** — print, variables, strings, numbers, input | 5 | Mad Libs Generator |
| 2 | **Decisions** — booleans, if/else, elif, logic, nesting | 5 | Text Adventure Game |
| 3 | **Loops** — while, for, break/continue, nested, patterns | 5 | Number Guessing Game |
| 4 | **Collections** — lists, methods, looping, dicts, nesting | 5 | Contact Book |
| 5 | **Functions** — def, params, defaults, scope, composition | 5 | Calculator |
| 6 | **Files & Errors** — read/write, try/except, CSV/JSON | 5 | Expense Tracker |
| 7 | **Leveling Up** — comprehensions, modules, pip, APIs | 5 | Weather App |
| 8 | **Objects** — classes, methods, attributes, inheritance | 5 | Final Project |

> Modules 1-5 are fully built with pre-tested exercises. Modules 6-8 have curriculum specs ready for generation.

### Bonus Exercises

Extra practice when you need it:

| Exercise | Concepts |
|---|---|
| `strings_reverse` | String reversal, palindrome detection |
| `loops_pyramid` | Nested loops, string centering |
| `lists_stats` | Median, mode, range calculations |
| `dict_word_count` | Word frequency, finding the most common |

## Commands

| Command | What it does |
|---|---|
| `/learn` | Smart session start — resumes where you left off |
| `/learn start` | First-time setup (profile, environment, first exercise) |
| `/learn check` | Run your code + tests, get Socratic feedback |
| `/learn run` | Just run your code and see the output |
| `/learn hint` | Get the next hint (gets more specific each time) |
| `/learn next` | Move to the next exercise |
| `/learn back` | Go back to the previous exercise |
| `/learn progress` | Full dashboard — level, streak, curriculum map |
| `/learn review` | Spaced repetition quiz on past topics |
| `/learn project` | Start or continue your current project |
| `/learn try` | Run a quick code snippet inline |
| `/learn explain` | On-demand explanation of any concept |
| `/learn vocab` | All programming terms you've learned |
| `/learn stats` | Deep analytics on your learning journey |
| `/learn streak` | Your coding streak and stats |
| `/learn update` | Sync latest exercises and tests from the repo |
| `/learn help` | Show all commands |

## Exercise Format

Every exercise is a real `.py` file with clear instructions:

```python
# ============================================
# Lesson 7: If/Else — Can You Vote?
# ============================================
#
# GOAL: Check if someone is old enough to vote.
#
# RULES:
#   Write a function can_vote(age) that:
#   - Returns "You can vote!" if age is 18 or older
#   - Returns "Not yet! X more years to go." if under 18
#
# EXAMPLES:
#   can_vote(20) → "You can vote!"
#   can_vote(15) → "Not yet! 3 more years to go."
# ============================================

def can_vote(age):
    # YOUR CODE HERE
    pass
```

Tests check **behavior**, not code style — any valid approach passes:

```python
# All of these pass the tests:
if age >= 18:                          # Style A: standard
if 18 <= age:                          # Style B: reversed
return "..." if age >= 18 else "..."   # Style C: ternary
```

## Attempt Tracking

Every `/learn check` records the full story:

```
Lesson: 07_if_else
Started: 2026-06-05 14:30
Completed: 2026-06-05 14:52 (3 attempts)

  ✗ Attempt 1: SyntaxError — missing colon after if (0/7 tests)
  ✗ Attempt 2: test_failure — used > instead of >= (5/7 tests)
  ✓ Attempt 3: pass — all 7 tests passing
```

`/learn stats` analyzes this data to show improvement trends, common error patterns, and which topics need review.

## Project Structure

```
python-tutor-skill/
├── install.sh                  # One-line installer
├── docs/                       # Research, specs, architecture
│   ├── 01-research-context.md
│   ├── 02-feature-spec.md
│   ├── 03-architecture.md
│   ├── 04-curriculum.md
│   ├── 05-pedagogy.md
│   ├── 06-data-model.md
│   └── 07-exercise-sources.md
└── skill/
    ├── python-tutor.md         # Skill prompt (symlinked to ~/.claude/skills/)
    ├── curriculum/             # Curriculum graph + module specs
    ├── exercises/              # 25 lessons + 5 projects + bonus
    │   ├── 01_hello_world/
    │   │   ├── exercise.py     # What the student sees
    │   │   ├── test_exercise.py # Behavior-based tests
    │   │   ├── solutions.py    # Multiple valid approaches (never shown)
    │   │   └── teaching_guide.md # Socratic script for Claude
    │   ├── .../
    │   └── bonus/              # Extra practice exercises
    ├── lib/                    # Test runner, error translator
    └── templates/              # Exercise file templates
```

## Design Principles

| Principle | How |
|---|---|
| **Never give the answer** | 4-level graduated hints. Full explanation only after 3+ failures. |
| **Real developer workflow** | Real `.py` files in VS Code/Cursor. Not a chat window. |
| **One concept at a time** | Each lesson teaches exactly ONE thing. |
| **Errors are teachers** | Translates tracebacks to plain language, then asks "what do you think?" |
| **Tests check behavior, not style** | `if age >= 18` and `if 18 <= age` both pass. |
| **Memory across sessions** | Progress, struggles, streaks — all persisted in JSON. |
| **Never ask twice** | Environment, preferences, setup — checked once, stored forever. |

## Exercise Sources

Built with inspiration and test patterns from these MIT-licensed repos:

- [exercism/python](https://github.com/exercism/python) — 146 exercises with pytest (primary source)
- [jerry-git/learn-python3](https://github.com/jerry-git/learn-python3) — Jupyter notebooks + pytest
- [trekhleb/learn-python](https://github.com/trekhleb/learn-python) — Assertion-based scripts
- [gregmalcolm/python_koans](https://github.com/gregmalcolm/python_koans) — TDD-based learning

See [`docs/07-exercise-sources.md`](docs/07-exercise-sources.md) for full research (15+ repos analyzed).

## Contributing

```bash
# Work on a feature branch
git checkout -b feature/new-exercise

# Add exercises, run tests
python3 -m pytest skill/exercises/*/test_exercise.py -v

# Push and create PR (main requires approval)
git push -u origin feature/new-exercise
gh pr create
```

## License

MIT — use it, fork it, teach with it.

---

<div align="center">

Built with [Claude Code](https://claude.ai/claude-code) · Designed for beginners · Powered by curiosity

</div>
