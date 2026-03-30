# Lesson 8: Elif — Teaching Guide

## Concept Introduction
"What if there are more than two options? elif (short for 'else if') lets you check multiple conditions."

## Prediction Question
"If score is 85, and we check `if score >= 90` first — that's False. What happens next?"

## Common Mistakes
### 1. Checking ranges explicitly: `if score >= 80 and score < 90`
→ "That works but you don't need the `and score < 90` — because elif only runs if the previous conditions were False. So by the time we reach `elif score >= 80`, we already know score < 90."

### 2. Using separate if instead of elif
→ "With separate ifs, score=95 would match BOTH >= 90 AND >= 80. elif stops after the first match."

### 3. Missing the else for F
→ "What happens if score is 45? None of your conditions match — you need else at the end."

## Hint Sequence
1. "Start with the highest: if score >= 90: return 'A'"
2. "Add elif score >= 80: return 'B' — and so on down"
3. "End with else: return 'F' for anything below 60"

## Vocabulary Introduced
- **elif** — "else if": checks another condition if previous ones were False
