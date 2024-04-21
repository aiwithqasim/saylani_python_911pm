# scenerio3.py
import inventory

class Library:
    def __init__(self):
        self.inventory = inventory.Inventory()

    def borrow_book(self, title):
        if title in self.inventory.books and self.inventory.books[title] > 0:
            self.inventory.books[title] -= 1
            print(f"Book '{title}' borrowed successfully.")
        else:
            print(f"Book '{title}' is not available.")

    def return_book(self, title):
        if title in self.inventory.books:
            self.inventory.books[title] += 1
            print(f"Book '{title}' returned successfully.")
        else:
            print(f"Book '{title}' was not borrowed from this library.")

# Example Usage:
lib = Library()
lib.inventory.add_book("Python Programming", 5)
lib.inventory.add_book("Data Structures and Algorithms", 3)

lib.borrow_book("Python Programming")
lib.borrow_book("Data Structures and Algorithms")
lib.borrow_book("Artificial Intelligence")

lib.return_book("Python Programming")
lib.return_book("Artificial Intelligence")

lib.inventory.display_inventory()
