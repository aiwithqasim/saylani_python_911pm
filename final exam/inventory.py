# inventory.py
class Inventory:
    def __init__(self):
        self.books = {}

    def add_book(self, title, quantity):
        self.books[title] = quantity

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
        else:
            print(f"Book '{title}' not found in inventory.")

    def display_inventory(self):
        print("Current Inventory:")
        for title, quantity in self.books.items():
            print(f"{title}: {quantity}")