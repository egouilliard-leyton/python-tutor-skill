# Curriculum Outline

## Module 1: First Steps (Week 1-2)

| # | Lesson | Concepts | Exercise Type |
|---|---|---|---|
| 1 | Hello World | print(), running a script | Write |
| 2 | Variables | assignment, naming | Write |
| 3 | Strings | quotes, concatenation, f-strings | Write |
| 4 | Numbers | int, float, math operators | Write |
| 5 | Input | input(), type conversion | Write |
| **P1** | **Mad Libs Generator** | Combine all above | **Project** |

## Module 2: Making Decisions (Week 2-3)

| # | Lesson | Concepts | Exercise Type |
|---|---|---|---|
| 6 | Booleans | True/False, comparisons (==, <, >) | Predict output |
| 7 | If/Else | basic branching | Write |
| 8 | Elif Chains | multiple conditions | Write |
| 9 | Logical Operators | and, or, not | Fix the bug |
| 10 | Nested Conditions | if inside if | Write |
| **P2** | **Text Adventure Game** | Combine all above | **Project** |

## Module 3: Repetition (Week 3-4)

| # | Lesson | Concepts | Exercise Type |
|---|---|---|---|
| 11 | While Loops | condition-based repetition | Write |
| 12 | For Loops | range(), iteration | Write |
| 13 | Loop Control | break, continue | Fix the bug |
| 14 | Nested Loops | patterns, grids | Write |
| 15 | Loop Patterns | counters, accumulators, search | Write |
| **P3** | **Number Guessing Game** | Combine all above | **Project** |

## Module 4: Collections (Week 4-5)

| # | Lesson | Concepts | Exercise Type |
|---|---|---|---|
| 16 | Lists Basics | creation, indexing, len() | Write |
| 17 | List Methods | append, remove, sort, slicing | Write |
| 18 | Looping Lists | for item in list, enumerate | Write |
| 19 | Dictionaries | key-value pairs, access, update | Write |
| 20 | Nested Structures | lists of dicts, dicts of lists | Refactor |
| **P4** | **Contact Book / To-Do List** | Combine all above | **Project** |

## Module 5: Functions (Week 5-6)

| # | Lesson | Concepts | Exercise Type |
|---|---|---|---|
| 21 | Defining Functions | def, calling, basic flow | Write |
| 22 | Parameters & Return | args, return values | Write |
| 23 | Default Parameters | defaults, keyword args | Fill in blank |
| 24 | Scope | local vs global, LEGB | Predict output |
| 25 | Composition | functions calling functions | Write |
| **P5** | **Calculator** | Combine all above | **Project** |

## Module 6: Files & Errors (Week 6-7)

| # | Lesson | Concepts | Exercise Type |
|---|---|---|---|
| 26 | Reading Files | open(), read(), with statement | Write |
| 27 | Writing Files | write(), append mode | Write |
| 28 | Try/Except | basic error handling | Fix the bug |
| 29 | Common Exceptions | ValueError, FileNotFoundError, etc. | Code review |
| 30 | CSV & JSON | csv module, json module | Write |
| **P6** | **Expense Tracker** | Combine all above | **Project** |

## Module 7: Leveling Up (Week 7-8)

| # | Lesson | Concepts | Exercise Type |
|---|---|---|---|
| 31 | List Comprehensions | [x for x in ...], filters | Refactor |
| 32 | String Methods | split, join, strip, replace | Write |
| 33 | Modules & Imports | import, from...import, __name__ | Write |
| 34 | Installing Packages | pip, virtual environments | Guided |
| 35 | Working with APIs | requests, JSON parsing | Write |
| **P7** | **Weather App or Web Scraper** | Combine all above | **Project** |

## Module 8: Objects (Week 8-10)

| # | Lesson | Concepts | Exercise Type |
|---|---|---|---|
| 36 | Classes Basics | class, __init__, self | Write |
| 37 | Methods | instance methods, __str__ | Write |
| 38 | Attributes | instance vs class attributes | Predict output |
| 39 | Inheritance | super(), method override | Write |
| 40 | When to Use Classes | design thinking, real-world modeling | Free build |
| **P8** | **Final Project (user's choice)** | Everything | **Project** |

## Concept Dependency Graph

```
print() ─→ variables ─→ strings ─→ f-strings
                │
                ▼
            numbers ─→ operators
                │
                ▼
            input() ─→ type conversion
                │
                ▼
          booleans ─→ comparisons ─→ if/else ─→ elif ─→ nested if
                                        │
                                        ▼
                              and/or/not ─→ while loops ─→ for loops
                                                │
                                                ▼
                                          break/continue ─→ nested loops
                                                │
                                                ▼
                                          lists ─→ list methods ─→ looping lists
                                                        │
                                                        ▼
                                                  dicts ─→ nested structures
                                                        │
                                                        ▼
                                              functions ─→ params/return ─→ scope
                                                        │
                                                        ▼
                                              file I/O ─→ try/except ─→ csv/json
                                                        │
                                                        ▼
                                          comprehensions ─→ modules ─→ pip ─→ APIs
                                                        │
                                                        ▼
                                              classes ─→ methods ─→ inheritance
```

## Project Details

### P1: Mad Libs Generator
- **Uses:** variables, strings, f-strings, input()
- **Description:** Ask user for nouns/verbs/adjectives, fill into a story template
- **Bonus:** Multiple story templates, save result to file

### P2: Text Adventure Game
- **Uses:** if/elif/else, logical operators, input()
- **Description:** Simple branching story (3-4 rooms, choices lead to different outcomes)
- **Bonus:** Inventory system (uses a list — preview of module 4)

### P3: Number Guessing Game
- **Uses:** while loops, for loops, random module, conditionals
- **Description:** Computer picks number, player guesses with higher/lower hints
- **Bonus:** Difficulty levels, guess counter, play again

### P4: Contact Book
- **Uses:** lists, dicts, loops, input()
- **Description:** Add/search/delete contacts stored as dicts in a list
- **Bonus:** Save to file (preview of module 6)

### P5: Calculator
- **Uses:** functions, parameters, return values
- **Description:** Menu-driven calculator with add/subtract/multiply/divide functions
- **Bonus:** History of calculations, undo last

### P6: Expense Tracker
- **Uses:** file I/O, try/except, csv/json, dicts, functions
- **Description:** Log expenses, categorize, save to CSV, show totals
- **Bonus:** Monthly reports, budget warnings

### P7: Weather App
- **Uses:** APIs, JSON, modules, error handling
- **Description:** Fetch weather from a free API, display formatted
- **Bonus:** 5-day forecast, multiple cities

### P8: Final Project (User's Choice)
- **Uses:** Everything learned
- **Options:** Game, automation tool, bot, data tool — whatever interests the learner
- **Guided:** Claude helps plan architecture but user builds it
