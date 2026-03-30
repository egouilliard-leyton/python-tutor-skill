# Architecture

## System Diagram

```
┌─────────────────────────────────────────────────────┐
│                  /learn Command                      │
│               (skill entry point)                    │
├─────────────────────────────────────────────────────┤
│  Session Router                                      │
│  - Loads environment.json + profile.json             │
│  - Detects context (first time / returning / active) │
│  - Routes to correct sub-command                     │
├──────────┬──────────┬────────────┬──────────────────┤
│ Curriculum│ Socratic │ Memory     │ Execution        │
│ Engine    │ Engine   │ System     │ Engine           │
│           │          │            │                  │
│ - Graph   │ - Hints  │ - Profile  │ - Run .py files  │
│ - Prereqs │ - Never  │ - Errors   │ - Run tests      │
│ - Unlock  │   answer │ - Progress │ - Capture output │
│ - Adapt   │ - Ask    │ - Concepts │ - Error translate │
│   pace    │   first  │ - Sessions │                  │
├──────────┴──────────┴────────────┴──────────────────┤
│  Gamification  │  Spaced Review  │  Visualization    │
├────────────────┴─────────────────┴──────────────────┤
│              Persistent File Storage                 │
│         ~/learning/.claude/ (JSON + logs)            │
│         ~/learning/lessons/ (exercise files)         │
│         ~/learning/projects/ (project files)         │
└─────────────────────────────────────────────────────┘
```

## File Structure — Skill Source

```
~/.claude/skills/python-tutor/
├── python-tutor.md              # Main skill prompt (loaded by Claude)
├── lib/
│   ├── test_runner.py           # Custom test runner (human-readable output)
│   └── error_translator.py     # Python error → plain language
├── templates/
│   ├── exercise.py.tmpl         # Exercise file template
│   ├── test_exercise.py.tmpl    # Test file template
│   └── project_readme.md.tmpl   # Project README template
└── curriculum/
    ├── curriculum.json           # Full curriculum graph definition
    └── modules/
        ├── 01_first_steps.json
        ├── 02_decisions.json
        ├── 03_loops.json
        ├── 04_collections.json
        ├── 05_functions.json
        ├── 06_files_errors.json
        ├── 07_leveling_up.json
        └── 08_objects.json
```

## File Structure — User's Learning Directory

```
~/learning/
├── .claude/
│   ├── environment.json         # OS, Python version, VS Code, paths
│   │                            # (checked ONCE, never asked again)
│   ├── profile.json             # name, goals, level, preferences, language
│   ├── curriculum.json          # current position, unlocked modules
│   ├── concepts.json            # per-concept comfort scores (0-100)
│   ├── errors.json              # recurring error pattern history
│   ├── vocabulary.json          # programming terms learned + confidence
│   ├── achievements.json        # unlocked badges
│   ├── streak.json              # daily streak data
│   └── sessions/
│       ├── 2026-03-27.json      # per-session: topics, time, scores
│       └── ...
├── lessons/
│   ├── 01_hello_world/
│   │   ├── exercise.py
│   │   └── test_exercise.py
│   ├── 02_variables/
│   │   ├── exercise.py
│   │   └── test_exercise.py
│   └── ... (generated on demand, not all at once)
├── projects/
│   ├── 01_mad_libs/
│   │   ├── README.md
│   │   ├── game.py
│   │   ├── test_game.py
│   │   └── hints.md
│   └── ...
└── sandbox/
    └── scratch.py
```

## Key Design Decisions

### 1. environment.json — The "Never Ask Twice" File

Stores everything about the setup so Claude never repeats environment checks:

```json
{
  "checked_at": "2026-03-27",
  "os": "linux",
  "distro": "ubuntu",
  "python": {
    "installed": true,
    "version": "3.12.3",
    "path": "/usr/bin/python3"
  },
  "vscode": {
    "installed": true,
    "python_extension": true,
    "python_indent_extension": true
  },
  "learning_dir": "/home/charles/learning",
  "shell": "bash",
  "locale": "fr_FR"
}
```

On every `/learn` start, Claude reads this file first. If it exists and is populated, skip all setup questions. Only re-check if user reports a problem.

### 2. Starter Kit — Claude's Session Bootstrap

When a new Claude Code conversation starts, the skill prompt (python-tutor.md) tells Claude to:

1. Read `~/learning/.claude/environment.json` — know the setup
2. Read `~/learning/.claude/profile.json` — know the learner
3. Read `~/learning/.claude/curriculum.json` — know where they are
4. Read `~/learning/.claude/concepts.json` — know strengths/weaknesses
5. Check `~/learning/.claude/streak.json` — know how long since last session
6. Check latest session file — know what was covered last time

This means every new conversation starts fully informed — no "remind me where we were?"

### 3. Exercise Generation (on demand)

Exercises are NOT pre-generated. When the curriculum engine says "next: lesson 14, nested loops":
1. Claude reads the module JSON for lesson 14's spec
2. Generates `exercise.py` and `test_exercise.py` using templates + spec
3. Creates the lesson folder
4. This allows customization based on the user's interests (game examples for game-track, data examples for data-track)

### 4. Test Runner (skill-owned)

`lib/test_runner.py` is a simple script that:
- Imports the user's exercise module
- Runs each test function
- Catches assertion errors and translates them
- Outputs a clean pass/fail report
- Returns structured JSON for Claude to interpret

### 5. Separation of Concerns

| Actor | Reads | Writes |
|---|---|---|
| Claude | User's .py files, all .claude/ state | .claude/ state, exercise/test files |
| User | Exercise .py files | Exercise .py files ONLY |
| Test runner | User's .py files | stdout (results) |

**Golden rule:** Claude never modifies files inside `lessons/` or `projects/` that the user has started editing. Claude only creates new exercise files and updates `.claude/` state files.

## Command Routing

```
/learn          → session_router (smart start)
/learn start    → onboarding flow
/learn check    → test_runner → feedback_engine
/learn run      → python3 exercise.py → show output
/learn hint     → hint_system (graduated, tracks level)
/learn next     → curriculum_engine (advance + generate next)
/learn back     → curriculum_engine (go back one)
/learn progress → dashboard_renderer
/learn review   → spaced_repetition_engine
/learn project  → project_manager
/learn try      → inline sandbox execution
/learn explain  → socratic_explainer (any concept)
/learn vocab    → vocabulary_tracker
/learn goals    → profile editor
/learn streak   → streak display
/learn help     → command list with descriptions
```
