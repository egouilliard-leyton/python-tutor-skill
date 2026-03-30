# Lesson 19: Dictionaries — Teaching Guide

## Concept Introduction
"A dictionary maps keys to values. Instead of numbered positions, you look things up by name."

Analogy: "Like a phone book: look up a name (key), get a number (value)."

## Visualization
```
  phone_book = {"Alice": "555-1234", "Bob": "555-5678"}

  phone_book["Alice"]     → "555-1234"
  phone_book["Charlie"]   → KeyError!
  phone_book.get("Charlie", "Not found") → "Not found"  (safe!)
```

## Common Mistakes
### 1. Using [] instead of .get() for lookup
→ "dict[key] crashes if key missing. dict.get(key, default) is safe."

### 2. Confusing dict keys with list indices
→ "Dicts use names, not numbers. phone_book['Alice'] not phone_book[0]."

## Vocabulary Introduced
- **dictionary (dict)** — key-value pairs in curly braces
- **key** — the lookup name
- **value** — what you get back
- **.get()** — safe lookup with default
- **.keys()** — all keys as a view
