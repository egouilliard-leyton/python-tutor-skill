# Python Tutor Skill — Documentation Index

## Docs

1. [Research Context](01-research-context.md) — Why this project exists, landscape analysis, platform comparison
2. [Feature Spec](02-feature-spec.md) — Complete feature list with rationale for each
3. [Architecture](03-architecture.md) — System diagram, file structures, design decisions, command routing
4. [Curriculum](04-curriculum.md) — 8 modules, 40 lessons, 8 projects, concept dependency graph
5. [Pedagogy](05-pedagogy.md) — Learning science, Socratic method, spaced repetition, anti-patterns
6. [Data Model](06-data-model.md) — JSON schemas for all state files, update rules, ownership

## Key Design Principles

- **Option A workflow**: User writes real .py files in VS Code, Claude reads + tests + gives Socratic feedback
- **Never give the answer**: Graduated hints, 4 levels, full explanation only as last resort
- **Never ask twice**: `environment.json` stores all setup state permanently
- **Session bootstrap**: Every new Claude conversation reads all state files before responding
- **Adaptive**: Comfort scores (0-100) per concept drive difficulty and review scheduling
- **Memory across sessions**: All progress persists in `~/learning/.claude/` as JSON files
