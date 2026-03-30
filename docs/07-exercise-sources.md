# Exercise Source Repositories — Research

## Summary

We researched open-source repositories with Python exercises suitable for absolute beginners. The goal: find pre-built, tested exercises with solutions that we can adapt for the Python Tutor skill's exercise bank.

## Tier 1 — Best for Our Use Case

### 0. exercism/python (THE #1 FIND)
- **URL:** https://github.com/exercism/python
- **Stars:** ~2.4k
- **License:** MIT (can freely adapt everything)
- **What it has:** 146 exercises across 17 concept areas, with difficulty ratings from 1 to 10. Split into "concept exercises" (structured syllabus) and "practice exercises" (open-ended).
- **Topics:** Variables, strings, conditionals, loops, functions, lists, dicts, classes, error handling, comprehensions, generators, and more — covers EVERYTHING in our curriculum.
- **Tests:** YES — every single exercise has a full pytest test suite. Students write code to make tests pass.
- **Solutions:** Yes (community solutions on exercism.org)
- **Why it's THE best:** Purpose-built for education. MIT license. Graded difficulty (1-10). pytest-driven. Actively maintained. The test-driven format is EXACTLY our `/learn check` model. 146 exercises means we have more than enough for all 8 modules + extras. This is the motherlode.

### 1. jerry-git/learn-python3
- **URL:** https://github.com/jerry-git/learn-python3
- **Stars:** ~6.8k
- **License:** MIT (can freely adapt)
- **What it has:** Jupyter notebooks with exercises for: Strings, Numbers, Conditionals, Lists, Dictionaries, For loops, Functions, File I/O, Classes, Exceptions, Debugging, Modules
- **Tests:** YES — includes pytest-based exercises. Dedicated "Testing with pytest" modules
- **Difficulty:** Beginner + Intermediate sections
- **Solutions:** Yes, notebooks include solutions
- **Why it's #1 for us:** Perfect topic alignment with our curriculum. Has pytest tests. MIT license. Exercises are structured as notebook → exercise pairs. We can extract exercise logic and adapt into our `.py` file format.

### 2. trekhleb/learn-python
- **URL:** https://github.com/trekhleb/learn-python
- **Stars:** ~17.8k
- **License:** MIT
- **What it has:** Python scripts split by topic, full of inline assertions. Covers: operators, data types, strings, lists, dicts, tuples, sets, control flow, functions, classes, modules, errors, files
- **Tests:** YES — uses pytest framework. Code is full of assertions that serve as self-documenting tests
- **Difficulty:** Not explicitly graded, but organized logically from simple to complex
- **Solutions:** Yes, the scripts ARE the solutions with assertions
- **Why it's great:** The assertion-based approach is exactly what we need — we can extract assertion patterns and reverse them into test files. Comprehensive topic coverage.

### 3. Asabeneh/30-Days-Of-Python
- **URL:** https://github.com/Asabeneh/30-Days-Of-Python
- **Stars:** ~45k+
- **License:** Open source (no explicit license file)
- **What it has:** 30-day curriculum: Day 1 (Intro) through Day 30 (Conclusions). Topics: Variables, Operators, Strings, Lists, Tuples, Sets, Dictionaries, Conditionals, Loops, Functions, Modules, List Comprehension, Exception Handling, File Handling, Classes, APIs
- **Tests:** No automated tests — exercises are checked manually
- **Difficulty:** YES — Level 1, Level 2, Level 3 per day
- **Solutions:** Partial — examples in the lessons, but exercises don't have provided solutions
- **Why it's great:** The graded difficulty system (Level 1-3) is exactly what we want. The curriculum structure is almost identical to ours. We can use their exercise prompts and add our own tests + solutions.

### NEW — 4GeeksAcademy/python-beginner-programming-exercises
- **URL:** https://github.com/4GeeksAcademy/python-beginner-programming-exercises
- **License:** Open source (4Geeks Academy)
- **What it has:** Interactive, auto-graded beginner exercises. Topics: print, data types, lists/tuples, functions/dictionaries. Step-by-step increasing difficulty.
- **Tests:** YES — each exercise has a `test.py` file with automated tests. Structure: `app.py` (student writes) + `README.md` (instructions) + `test.py` (auto-grading)
- **Solutions:** Partial
- **Why it's critical:** The `app.py + test.py` per-exercise structure is EXACTLY our model. This is the closest existing implementation to what we're building. Has video tutorials too.
- **Note:** Tests are "very rigid and strict" — we should make ours more flexible.

### NEW — gregmalcolm/python_koans
- **URL:** https://github.com/gregmalcolm/python_koans
- **Stars:** ~5.1k
- **License:** MIT
- **What it has:** Port of Ruby Koans — learn Python through TDD. Fix failing tests to learn. Covers: assertions, tuples, strings, lists, logic problems.
- **Tests:** YES — the entire teaching method IS tests. Run `contemplate_koans.py` → see failing test → fix it → learn.
- **Approach:** "Red, Green, Refactor" — see failure, make it pass, reflect.
- **Why it's great:** The fill-in-the-assert approach (`assert __ == 4`) is brilliant for our "predict the output" exercises. The TDD-first teaching philosophy aligns perfectly with our test-driven feedback loop. MIT license.

### NEW — ELC/python-basics
- **URL:** https://github.com/ELC/python-basics
- **License:** Open source
- **What it has:** Autograding template for Python assignments. Each exercise has function signature + docstring, student implements. Tests in separate `tests/` folder.
- **Tests:** YES — designed for GitHub Classroom autograding, also works standalone with `python exercise/<exercise>.py`
- **Topics:** IF blocks, logical operators, chained comparisons, recursion, boolean expressions, FOR loops (range, len, enumerate, zip)
- **Why useful:** Clean separation of exercise/tests structure we can directly adapt.

## Tier 2 — Good Supplementary Sources

### 4. donnemartin/interactive-coding-challenges
- **URL:** https://github.com/donnemartin/interactive-coding-challenges
- **Stars:** ~30k+
- **License:** Personal open source
- **What it has:** 120+ interactive Python challenges in Jupyter notebooks. Algorithm/data structure focus.
- **Tests:** YES — every challenge has built-in unit tests
- **Solutions:** Yes, solution notebooks provided
- **Why useful:** Great test patterns to adapt. The Jupyter Challenge → Solution structure is a model for our exercise → test approach. However, topics skew toward algorithms/interviews rather than absolute beginner basics.

### 5. zhiwehu/Python-programming-exercises + darkprinx/break-the-ice-with-python
- **URLs:** https://github.com/zhiwehu/Python-programming-exercises / https://github.com/darkprinx/100-plus-Python-programming-exercises-extended
- **Stars:** ~25k+ / ~3k
- **License:** Not explicitly stated
- **What it has:** 100+ sequential problems with question + hint + solution format
- **Tests:** No automated tests
- **Solutions:** Yes — multiple solution approaches per problem (Python 2 + Python 3)
- **Why useful:** Good for "drill practice" — many small problems. The multiple-solution approach aligns with our "accept any valid style" philosophy. Problems cover: string manipulation, list operations, math, classes, regex.

### 6. karan/Projects
- **URL:** https://github.com/karan/Projects
- **Stars:** ~47k+
- **License:** MIT
- **What it has:** ~100+ practical project ideas categorized by: Numbers, Text, Networking, Classes, Files, Databases, Graphics, Security
- **Tests:** No
- **Solutions:** User-contributed via links
- **Why useful:** Excellent for our PROJECT exercises (not individual lessons). Many overlap with our project ideas: Calculator, Mortgage Calculator, Fibonacci, Hangman, Address Book. Can mine for project descriptions and requirements.

## Tier 3 — Reference / Inspiration Only

### 7. TheAlgorithms/Python
- **URL:** https://github.com/TheAlgorithms/Python
- **Stars:** ~195k+
- **License:** MIT
- **What it has:** Hundreds of algorithm implementations with doctests
- **Why limited:** Too advanced for absolute beginners. Useful as a reference for "what good Python code looks like" in later modules (7-8).

### 8. geekcomputers/Python
- **URL:** https://github.com/geekcomputers/Python
- **Stars:** ~33k+
- **License:** MIT
- **What it has:** 41+ educational Python scripts for beginners (batch renamers, downloaders, etc.)
- **Why limited:** Scripts are example programs, not structured exercises. Good for "here's what Python can do" inspiration during onboarding.

### 9. freeCodeCamp/freeCodeCamp
- **URL:** https://github.com/freeCodeCamp/freeCodeCamp
- **Stars:** ~410k+
- **License:** BSD-3-Clause (software), Copyright (curriculum)
- **What it has:** Full Python certification with interactive challenges
- **Why limited:** Curriculum content is copyrighted. The platform is web-based, not file-based. However, the curriculum STRUCTURE is useful as a reference for ordering topics.

### 10. mbucko/openleetcode
- **URL:** https://github.com/mbucko/openleetcode
- **Stars:** Small
- **License:** Not stated
- **What it has:** Open-source LeetCode clone with test framework
- **Why limited:** Currently C++ only. But the .test file format for auto-verification is an interesting model we could adapt.

### Additional Finds (from deep web research)

- **bregman-arie/python-exercises** — 231 exercises in Q&A format by topic. No tests, no license. Good for exercise prompts.
- **realpython/python-basics-exercises** — Companion to Real Python book. Well-structured by chapter. No license specified.
- **Pierian-Data/Complete-Python-3-Bootcamp** (~29.5k stars) — Jupyter exercise/solution notebooks from Udemy bootcamp. No license.
- **quobit/awesome-python-in-education** (CC0) — Meta-list of Python education resources. Good for discovering more.

## How to Use These Sources

### Structural Models to Adopt

| Source | What to Copy |
|---|---|
| **exercism/python** | pytest test suites per exercise, difficulty ratings, concept syllabus — THE primary source |
| **4GeeksAcademy** | `app.py + test.py` per-exercise folder structure — almost identical to our model |
| **python_koans** | Fill-in-the-assert pattern for "predict the output" exercises |
| **ELC/python-basics** | Function signature + docstring as exercise scaffold |
| **trekhleb/learn-python** | Assertion-heavy scripts as self-documenting test patterns |

### For Exercise Bank (Modules 1-3)

| Our Lesson | Primary Source | What to Extract |
|---|---|---|
| 01 Hello World | 4GeeksAcademy + exercism "hello-world" | Exercise structure, auto-grading pattern |
| 02 Variables | exercism concept exercises + 30-Days Day 2 | pytest patterns + exercise prompts |
| 03 Strings | exercism "two-fer", "bob" + learn-python3 | String exercises with pytest tests |
| 04 Numbers | exercism "currency-exchange" + learn-python3 | Number exercises + tests |
| 05 Input | 30-Days Day 2 + 4GeeksAcademy | Interactive exercise patterns |
| 06 Booleans | python_koans + exercism "ghost-gobble" | Assert fill-in-the-blank + predict output |
| 07-10 Conditionals | exercism "meltdown-mitigation" + ELC/python-basics | Conditional exercises with pytest |
| 11-15 Loops | exercism "making-the-grade" + ELC/python-basics + 30-Days Day 10 | Loop exercises + enumerate/zip |

### For Solution Variants

- **darkprinx/break-the-ice-with-python** — shows multiple solution approaches per problem
- **trekhleb/learn-python** — clean assertion-based solutions as reference
- **learn-python3** — pytest solutions as test patterns

### For Project Ideas

- **karan/Projects** — practical project descriptions (MIT license)
- **30-Days-Of-Python** — project-level exercises in later days
- **practical-tutorials/project-based-learning** — full project tutorials

### For Test Patterns

1. **trekhleb/learn-python** — inline assertions (adapt to our test files)
2. **donnemartin/interactive-coding-challenges** — unit test structure
3. **learn-python3** — pytest exercises (closest to our format)

## License Summary

| Repo | License | Can we adapt exercises? |
|---|---|---|
| **exercism/python** | **MIT** | **YES — freely. Our #1 source.** |
| 4GeeksAcademy/python-beginner-exercises | Open source | YES — adapt structure + test patterns |
| gregmalcolm/python_koans | MIT | YES — freely adapt assert-fill patterns |
| ELC/python-basics | Open source | YES — adapt exercise/test separation |
| jerry-git/learn-python3 | MIT | YES — freely |
| trekhleb/learn-python | MIT | YES — freely |
| Asabeneh/30-Days-Of-Python | Unspecified | Exercise prompts OK, don't copy verbatim |
| karan/Projects | MIT | YES — freely |
| donnemartin/interactive-coding-challenges | Personal OSS | Adapt patterns, credit author |
| zhiwehu/Python-programming-exercises | Unspecified | Use as inspiration, write our own |
| TheAlgorithms/Python | MIT | YES — for later modules |
| geekcomputers/Python | MIT | YES |

## NotebookLM Research Notebook

All sources loaded and queryable at:
https://notebooklm.google.com/notebook/a0cb9549-82f9-4f9d-bd78-df359fd4c1aa

Deep web research was also initiated (may still be processing). Results will be imported into this notebook when complete.
