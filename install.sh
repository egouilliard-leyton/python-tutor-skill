#!/usr/bin/env bash
# ============================================
# Python Tutor Skill — Installer
# ============================================
# Sets up the /learn skill for Claude Code.
#
# Usage:
#   bash install.sh              # Install from local repo
#   bash install.sh --uninstall  # Remove the skill
#
# What it does:
#   1. Detects where the repo lives
#   2. Creates ~/.claude/skills/python-tutor/
#   3. Symlinks SKILL.md to the repo's skill prompt
#   4. Verifies Python is installed
#   5. Done — type /learn start in Claude Code
# ============================================

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

SKILL_DIR="$HOME/.claude/skills/python-tutor"
REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_SOURCE="$REPO_DIR/skill/python-tutor.md"

# --- Uninstall ---
if [ "$1" = "--uninstall" ]; then
    echo -e "${YELLOW}Uninstalling Python Tutor skill...${NC}"
    rm -rf "$SKILL_DIR"
    echo -e "${GREEN}Done. Skill removed.${NC}"
    echo "Note: ~/learning/ directory (student data) was NOT deleted."
    exit 0
fi

echo "============================================"
echo "  Python Tutor — Installer"
echo "============================================"
echo ""

# Step 1: Check repo
if [ ! -f "$SKILL_SOURCE" ]; then
    echo -e "${RED}Error: Can't find skill source at:${NC}"
    echo "  $SKILL_SOURCE"
    echo "Run this script from the python-tutor-skill repo directory."
    exit 1
fi
echo -e "${GREEN}[1/4]${NC} Found repo at: $REPO_DIR"

# Step 2: Check Claude Code skills directory
if [ ! -d "$HOME/.claude" ]; then
    echo -e "${RED}Error: ~/.claude/ not found. Is Claude Code installed?${NC}"
    echo "Install Claude Code first: https://claude.ai/claude-code"
    exit 1
fi
mkdir -p "$SKILL_DIR"
echo -e "${GREEN}[2/4]${NC} Skills directory ready: $SKILL_DIR"

# Step 3: Create symlink
if [ -L "$SKILL_DIR/SKILL.md" ]; then
    echo -e "${YELLOW}       Symlink already exists, updating...${NC}"
    rm "$SKILL_DIR/SKILL.md"
fi
ln -sf "$SKILL_SOURCE" "$SKILL_DIR/SKILL.md"
echo -e "${GREEN}[3/4]${NC} Symlinked SKILL.md → repo (auto-updates on edit)"

# Step 4: Check Python
if command -v python3 &>/dev/null; then
    PY_VERSION=$(python3 --version 2>&1)
    echo -e "${GREEN}[4/4]${NC} $PY_VERSION found"
else
    echo -e "${YELLOW}[4/4]${NC} Python 3 not found — install it before using /learn"
fi

# Check editor
EDITOR_CMD=""
if command -v cursor &>/dev/null; then
    EDITOR_CMD="cursor"
elif command -v code &>/dev/null; then
    EDITOR_CMD="code"
fi

echo ""
echo "============================================"
echo -e "${GREEN}  Installation complete!${NC}"
echo "============================================"
echo ""
echo "  Repo:    $REPO_DIR"
echo "  Skill:   $SKILL_DIR/SKILL.md → repo (symlink)"
if [ -n "$EDITOR_CMD" ]; then
    echo "  Editor:  $EDITOR_CMD"
else
    echo -e "  Editor:  ${YELLOW}Not found (install VS Code or Cursor)${NC}"
fi
echo ""
echo "  Next steps:"
echo "    1. Open Claude Code"
echo "    2. Type: /learn start"
echo "    3. Follow the onboarding!"
echo ""
echo "  To update after repo changes: /learn update"
echo "  To uninstall: bash $REPO_DIR/install.sh --uninstall"
echo ""
