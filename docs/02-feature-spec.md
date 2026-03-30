# Feature Specification

## Why People Quit Learning to Code (and our counters)

| Quit Reason | When It Hits | Counter |
|---|---|---|
| "I don't know what to type" | Day 1 | Scaffolded exercise files with clear comments |
| "The error makes no sense" | Day 2 | Error translator + Socratic debugging |
| "I don't see the point" | Week 1 | Every lesson tied to a real project |
| "It's too easy / boring" | Week 2 | Adaptive difficulty + skip-ahead tests |
| "It got suddenly hard" | Week 3 | Difficulty spike detector + auto-remediation |
| "I forgot what I learned" | After a break | Spaced review + welcome-back recap |
| "I can't build anything real yet" | Week 4 | Mini-projects every 3-5 lessons |
| "I'm not making progress" | Ongoing | Visible progress map + streak + growth evidence |
| "I don't know what to learn next" | Ongoing | Curriculum engine decides automatically |

## Feature Categories

### 1. Onboarding & Placement

- Initial assessment (prior experience, goals, time commitment)
- Environment check (Python, VS Code, directory creation)
- Profile creation stored in `environment.json`
- First exercise delivered immediately (hello world → instant win)
- Everything checked once, stored permanently — never asked again

### 2. Structured Curriculum Engine

Concept dependency graph (not flat list):

```
Variables → Data Types → Operators → Conditionals → Loops
                                          ↓
                                    Functions → Scope → Modules
                                        ↓
                                  Lists → Dicts → Comprehensions
                                        ↓
                                  Classes → OOP → Inheritance
                                        ↓
                                  File I/O → Error Handling → APIs
                                        ↓
                                  Projects (game, scraper, bot)
```

- 40 lessons across 8 modules
- Micro-lessons (5-10 min each, ONE concept)
- Mini-project after every module (combines recent concepts)
- Prerequisite gating — can't skip ahead without proving mastery

### 3. Persistent Memory System

Stored in `~/learning/.claude/`:

| File | Purpose |
|---|---|
| `profile.json` | Name, goals, level, preferences |
| `environment.json` | What's installed, paths, editor, OS — checked once |
| `curriculum.json` | Current position, unlocked modules |
| `concepts.json` | Per-concept comfort scores (0-100) |
| `errors.json` | Error pattern history |
| `vocabulary.json` | Known programming terms |
| `sessions/*.json` | Per-session logs (topics, time, scores) |
| `achievements.json` | Unlocked badges |
| `streak.json` | Daily streak tracking |

### 4. Socratic Teaching Engine

- Ask before telling — prediction questions first
- Graduated hints (4 levels: vague → specific → almost answer → full explanation)
- Explain the "why" — never just "use len()"
- Celebrate struggle — errors are learning signals
- Rubber duck mode — user explains before getting help

### 5. Exercise File Design

Every exercise is a self-contained `.py` file:
- Clear goal as comments at top
- Real-world scenario (not abstract)
- Expected output examples
- Hints (separated, try-first encouraged)
- Test runner at bottom (user sees output on `python3 exercise.py`)
- Paired `test_exercise.py` (run by Claude, never opened by user)

### 6. Test System

- Flexible assertions (keyword matching, not exact strings)
- Edge cases included naturally
- Custom runner outputs human-readable failures, not tracebacks
- Tests are invisible infrastructure — user just sees pass/fail + feedback

### 7. Feedback Engine (post `/learn check`)

Four layers, applied in order:
1. **Does it run?** — Error translation to plain language
2. **Does it pass tests?** — Describe failing scenario, not the fix
3. **Code quality** — Only after all tests pass, and only after week 2
4. **Pattern recognition** — Detect recurring mistakes across exercises

### 8. Adaptive Difficulty

Per-concept comfort score (0-100):

| Score | Meaning | Action |
|---|---|---|
| 0-20 | Never seen / completely lost | Teach with analogies |
| 20-40 | Seen but can't apply | Guided walkthrough |
| 40-60 | Can apply with help | Standard exercises |
| 60-80 | Can apply alone | Harder variations |
| 80-100 | Mastered | Skip reviews, use in projects |

Smart skip: if user passes first try instantly, offer to jump ahead.

### 9. Lesson Types (variety)

| Type | When |
|---|---|
| Concept intro | New topic |
| Predict the output | Building mental model |
| Write the code | Core practice |
| Fix the bug | Debugging skill |
| Fill in the blank | Scaffolded difficulty |
| Refactor | Style + Pythonic thinking |
| Code review | Reading comprehension |
| Free build | Synthesis + creativity |
| Speed drill | Fluency building |
| Explain back | Metacognition |

Rotation: Concept → Predict → Write → Write → Bug fix → Mini-project → Review

### 10. Error Translator

Converts Python tracebacks to plain language:
- Shows what Python said
- Explains what it means
- Gives a concrete example
- Asks the user to look at their code

Priority errors: SyntaxError, IndentationError, NameError, TypeError, IndexError, AttributeError, FileNotFoundError, ModuleNotFoundError.

### 11. Spaced Repetition

- Concept review on decay schedule (1 day, 3 days, 7 days)
- Start-of-session warmup (2-3 recall questions)
- Code reconstruction ("recreate last week's function from memory")
- Confidence self-rating after each topic

### 12. Progress Dashboard (`/learn progress`)

ASCII dashboard showing:
- Current level and XP
- Streak count
- Module completion bars
- Recent achievements
- Active struggles
- Next up

### 13. Gamification

- XP for completions, streaks, challenges
- Achievement badges (First Program, Loop Hero, Bug Squasher, etc.)
- Level system: Novice → Apprentice → Journeyman → Craftsman → Expert
- Daily streak tracking
- Optional daily challenges

### 14. Project System

After every module, a project combining recent concepts:
- README.md with plain English description
- Starter file with structure comments
- Tests (run via `/learn check`)
- Graduated hint file
- Three modes: scaffolded, guided, challenge

### 15. Concept Visualization

ASCII diagrams generated in conversation:
- Variables as labeled boxes
- Lists as indexed arrays
- Loop step-by-step execution
- Function call flow diagrams

### 16. Struggle Intervention (escalating)

1. Change analogy
2. Decompose the problem into sub-steps
3. Worked example (parallel problem)
4. Pair programming mode
5. Skip and revisit later

### 17. Vocabulary Tracker

- Terms introduced with definition + analogy
- Never use jargon before teaching it
- Track confidence per term
- Gentle correction on misuse

### 18. Session Management

- Smart start (detects context: first time, returning, same day)
- Session pacing based on chosen time (15/30/60 min)
- End-of-session summary
- Time tracking with natural stop suggestions

### 19. Welcome Back System

- After 3+ days: warmup quiz on likely-forgotten concepts
- After 2+ weeks: mini-challenge to assess retention
- Score recall → adjust comfort scores → quick refresher if needed

### 20. Safety Rails

- Anti-copy-paste: if perfect code appears instantly, ask to explain it
- Comprehension checks: random "what does this line do?"
- Progressive complexity: earn the next concept
- Frustration circuit breaker: after 3 fails, switch approach entirely

### 21. Help Command

`/learn help` lists all commands with one-line descriptions and usage examples.

### 22. Environment Memory

`environment.json` stores everything about the user's setup (OS, Python version, VS Code, paths). Checked once during onboarding, updated only when something changes. Prevents asking the same setup questions twice across sessions.
