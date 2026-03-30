# Project 4: Contact Book — Hints

## Hint 1: Start with the dictionary
```python
contacts = {}
contacts["Alice"] = "555-1234"
print(contacts["Alice"])  # → 555-1234
```

## Hint 2: Adding a contact
```python
def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    contacts[name] = phone
    print(f"Added {name}!")
```

## Hint 3: Searching safely
```python
if name in contacts:
    print(f"{name}: {contacts[name]}")
else:
    print("Not found.")
```

## Hint 4: Listing all contacts
```python
for name, phone in contacts.items():
    print(f"{name}: {phone}")
```

## Hint 5: The menu loop
```python
while True:
    print("\n1. Add  2. Search  3. List  4. Quit")
    choice = input("Choice: ")
    if choice == "4":
        print("Goodbye!")
        break
```
