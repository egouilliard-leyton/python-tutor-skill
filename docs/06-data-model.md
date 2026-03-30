# Data Model

## State Files (~/learning/.claude/)

### environment.json — "Never Ask Twice"

Stores everything about the user's machine. Populated once during onboarding. Prevents Claude from ever asking the same environment question across sessions.

```json
{
  "checked_at": "2026-03-27",
  "os": "linux",
  "distro": "ubuntu",
  "shell": "bash",
  "locale": "fr_FR",
  "python": {
    "installed": true,
    "version": "3.12.3",
    "path": "/usr/bin/python3"
  },
  "vscode": {
    "installed": true,
    "path": "/usr/bin/code",
    "extensions": {
      "python": true,
      "python_indent": true
    }
  },
  "learning_dir": "/home/charles/learning",
  "pip": {
    "installed": true,
    "path": "/usr/bin/pip3"
  }
}
```

### profile.json — Learner Identity

```json
{
  "name": "Charles",
  "started": "2026-06-01",
  "experience": "never",
  "goal_track": "games",
  "session_length": "30min",
  "level": 2,
  "xp": 340,
  "total_sessions": 12,
  "total_time_minutes": 380
}
```

### curriculum.json — Progress State

```json
{
  "current_module": 2,
  "current_lesson": 8,
  "current_exercise_status": "in_progress",
  "completed_lessons": [1, 2, 3, 4, 5, 6, 7],
  "completed_projects": ["p1_mad_libs"],
  "skipped_lessons": [],
  "hint_counts": {
    "8": 1
  }
}
```

### concepts.json — Comfort Scores

```json
{
  "print": {"score": 95, "last_practiced": "2026-06-10", "times_practiced": 8},
  "variables": {"score": 90, "last_practiced": "2026-06-10", "times_practiced": 6},
  "strings": {"score": 85, "last_practiced": "2026-06-09", "times_practiced": 5},
  "if": {"score": 60, "last_practiced": "2026-06-12", "times_practiced": 3},
  "elif": {"score": 35, "last_practiced": "2026-06-12", "times_practiced": 1}
}
```

Score update rules:
| Event | Delta |
|---|---|
| First attempt pass (all tests) | +30 |
| Pass after 1 hint | +20 |
| Pass after 2+ hints | +10 |
| Fail 3+ times | -10 |
| Used in project | +15 |
| Correct in spaced review | +5 |
| Forgotten in review | -15 |
| Weekly time decay (per week unused) | -5 |

### errors.json — Error Patterns

```json
{
  "patterns": [
    {
      "type": "SyntaxError",
      "subtype": "missing_colon",
      "occurrences": 4,
      "lessons": [7, 8, 9, 11],
      "last_seen": "2026-06-12",
      "improving": true
    },
    {
      "type": "TypeError",
      "subtype": "string_int_concat",
      "occurrences": 2,
      "lessons": [5, 7],
      "last_seen": "2026-06-08",
      "improving": false
    }
  ]
}
```

When an error type reaches 3+ occurrences and `improving: false`, trigger a targeted micro-drill.

### vocabulary.json — Known Terms

```json
{
  "terms": {
    "variable": {"introduced_lesson": 2, "confidence": 90, "definition": "A name that stores a value"},
    "string": {"introduced_lesson": 3, "confidence": 85, "definition": "Text data inside quotes"},
    "boolean": {"introduced_lesson": 6, "confidence": 40, "definition": "True or False value"}
  }
}
```

### streak.json — Engagement Tracking

```json
{
  "current_streak": 5,
  "longest_streak": 7,
  "last_session_date": "2026-06-12",
  "session_dates": ["2026-06-08", "2026-06-09", "2026-06-10", "2026-06-11", "2026-06-12"]
}
```

### achievements.json — Badges

```json
{
  "unlocked": [
    {"id": "first_program", "name": "First Program", "date": "2026-06-01"},
    {"id": "variable_master", "name": "Variable Master", "date": "2026-06-05"},
    {"id": "streak_3", "name": "Streak Starter", "date": "2026-06-10"}
  ]
}
```

### attempts/<lesson_slug>.json — Per-Exercise Attempt History

The most granular tracking — every `/learn check` creates a record. This is how we track the full learning journey within each exercise.

```json
{
  "lesson": "07_if_else",
  "started": "2026-06-05T14:30:00",
  "completed": "2026-06-05T14:52:00",
  "total_attempts": 3,
  "hints_used": 1,
  "attempts": [
    {
      "attempt": 1,
      "timestamp": "2026-06-05T14:35:00",
      "code_snapshot": "def can_vote(age):\n    if age > 18:\n        return 'You can vote!'\n",
      "result": "test_failure",
      "tests_passed": 3,
      "tests_total": 7,
      "failing_tests": ["test_exactly_18", "test_years_remaining"],
      "error_type": null,
      "error_message": null,
      "error_line": null,
      "hints_used_before": 0
    },
    {
      "attempt": 2,
      "timestamp": "2026-06-05T14:41:00",
      "code_snapshot": "def can_vote(age):\n    if age >= 18:\n        return 'You can vote!'\n    else:\n        return 'Not yet! ' + 18 - age + ' more years.'\n",
      "result": "runtime_error",
      "error_type": "TypeError",
      "error_message": "can only concatenate str (not \"int\") to str",
      "error_line": 5,
      "tests_passed": 0,
      "tests_total": 7,
      "failing_tests": [],
      "hints_used_before": 1
    },
    {
      "attempt": 3,
      "timestamp": "2026-06-05T14:52:00",
      "code_snapshot": "def can_vote(age):\n    if age >= 18:\n        return 'You can vote!'\n    else:\n        return f'Not yet! {18 - age} more years to go.'\n",
      "result": "pass",
      "tests_passed": 7,
      "tests_total": 7,
      "failing_tests": [],
      "error_type": null,
      "error_message": null,
      "error_line": null,
      "hints_used_before": 1
    }
  ]
}
```

This example tells the full story:
1. Used `>` instead of `>=` (off-by-one) → 3/7 tests pass
2. Fixed the comparison but hit TypeError building the string → runtime crash
3. Switched to f-string → all 7 pass

**What we can derive from attempt data:**
- Average attempts per exercise (difficulty indicator)
- Common error patterns across exercises
- Improvement trend (fewer attempts over time)
- Hint dependency (using fewer hints as skills build)
- Time-to-completion per exercise
- Which exercises were hardest for this specific learner

### sessions/YYYY-MM-DD.json — Session Logs

```json
{
  "date": "2026-06-12",
  "duration_minutes": 35,
  "lessons_attempted": [8],
  "lessons_completed": [],
  "concepts_practiced": ["elif"],
  "errors_encountered": [
    {"type": "SyntaxError", "subtype": "missing_colon", "line": 5}
  ],
  "hints_used": 1,
  "xp_earned": 0,
  "notes": "Working on elif chains. Got stuck on grade boundaries."
}
```

## File Ownership Rules

| Actor | Can Read | Can Write |
|---|---|---|
| Claude | Everything | .claude/ state files, new exercise/test files |
| User | Everything | Their own exercise .py files ONLY |
| Test runner | Exercise files | stdout only |

**Critical:** Claude NEVER modifies an exercise file that the user has started editing. Claude only creates new scaffold files and updates state.
