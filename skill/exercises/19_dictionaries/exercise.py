"""Solution variants for Lesson 19: Dictionaries"""

def create_contact(name, phone):
    return {"name": name, "phone": phone}

def get_phone(phone_book, name):
    return phone_book.get(name, "Not found")

def add_contact(phone_book, name, phone):
    phone_book[name] = phone
    return phone_book

def list_names(phone_book):
    return sorted(phone_book.keys())
