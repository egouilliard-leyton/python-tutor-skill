# Lesson 10: Nested Conditions — Teaching Guide

## Concept Introduction
"Real-world rules are layered. First check one thing, then inside that, check another."

Analogy: "Airport security: first check — boarding pass? Then — liquids over 100ml?"

## Approach
Guide them to break the problem into steps:
1. "First, just get the base price from age. Ignore discounts."
2. "Now add the student discount — but only for adults."
3. "Now add the Tuesday discount — for everyone."
4. "Finally, make sure price never goes below 4."

## Common Mistakes
### 1. Applying student discount to children
→ "A 10-year-old with is_student=True — should they get the student discount? The rules say only ages 12-64."

### 2. Forgetting max(price, 4)
→ "A child on Tuesday: 6 - 2 = 4. What if there were more discounts? Always enforce the minimum."

### 3. Checking day before price
→ "Calculate the full price first, then apply day discount last."

## Hint Sequence
1. "Start with just the age check — get the base price right first"
2. "Now add: if is_student AND age is 12-64, subtract 2"
3. "Then: if day == 'tuesday', subtract 2. Use max(price, 4) at the end."

## Vocabulary Introduced
- **nested** — code inside other code (an if inside an if)
- **max()** — returns the larger of two values
