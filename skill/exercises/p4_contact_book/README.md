# Project 4: Contact Book

Build a menu-driven contact manager that stores names and phone numbers!

## What you'll build
A program where:
1. User sees a menu: Add, Search, List All, Quit
2. Add a contact (name + phone number)
3. Search for a contact by name
4. List all contacts
5. Loop until the user quits

## What you'll use
- Dictionaries (store contacts as `{name: phone}`)
- Functions (one per action: add, search, list)
- `while` loops (keep showing the menu)
- `input()` (get user choices and data)
- `if/elif/else` (handle menu choices)

## Steps (suggested order)
1. Create an empty dictionary: `contacts = {}`
2. Write `add_contact(contacts)` — ask for name and number, add to dict
3. Write `search_contact(contacts)` — ask for name, print the number
4. Write `list_contacts(contacts)` — print all contacts
5. Write the main menu loop: show options, get choice, call the right function
6. Handle invalid menu choices with a message
7. Add a goodbye message when they quit

## Example run
```
=== Contact Book ===
1. Add contact
2. Search contact
3. List all contacts
4. Quit

Choice: 1
Name: Alice
Phone: 555-1234
Added Alice!

Choice: 1
Name: Bob
Phone: 555-5678
Added Bob!

Choice: 3
--- All Contacts ---
Alice: 555-1234
Bob: 555-5678

Choice: 2
Search name: Alice
Alice: 555-1234

Choice: 4
Goodbye!
```

## Bonus challenges
- Handle "not found" when searching for a name that doesn't exist
- Let the user delete a contact
- Make search case-insensitive
- Save contacts to a file so they persist between runs
