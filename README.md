# Python Tutor — Claude Code Skill

A Claude Code skill that turns Claude into a personalized Python tutor for absolute beginners. It uses real `.py` files, persistent memory, adaptive difficulty, Socratic teaching, and spaced repetition to teach Python — without ever writing code for the learner.

## Install

```bash
# Copy skill to Claude skills directory
cp -r skill/ ~/.claude/skills/python-tutor/

# Or symlink for development
ln -s "$(pwd)/skill" ~/.claude/skills/python-tutor
```

## Usage

```
/learn start     — First-time onboarding (profile, env check, first exercise)
/learn           — Smart session start (resumes where you left off)
/learn check     — Run tests on current exercise + Socratic feedback
/learn run       — Run current exercise file, show output
/learn hint      — Get next hint (graduated: vague → specific)
/learn next      — Move to next exercise
/learn back      — Redo previous exercise
/learn progress  — Full dashboard (level, streak, curriculum map)
/learn review    — Spaced repetition quiz on past concepts
/learn project   — Start/continue current project
/learn try       — Quick inline sandbox for experiments
/learn explain   — On-demand explanation of any concept
/learn vocab     — Show all programming terms learned
/learn goals     — View/update learning goals
/learn streak    — Show streak and stats
/learn help      — List all commands with descriptions
```

## How It Works

1. User writes Python in real `.py` files in VS Code
2. Claude reads their code, runs tests, gives Socratic feedback
3. Claude **never** writes code in the user's files
4. Progress, struggles, and patterns are tracked across sessions
5. Curriculum adapts to the learner's pace and weaknesses

## Docs

See `docs/` for full research, planning, and architecture.
