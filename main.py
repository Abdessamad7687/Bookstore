import pickle
from prettytable import PrettyTable

class Book:
    def __init__(self, title, author, isbn, price, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.quantity = quantity

class Bookstore:
    def __init__(self):
        self.inventory = []

    def add_book(self, title, author, isbn, price, quantity):
        book = Book(title, author, isbn, price, quantity)
        self.inventory.append(book)
        print(f"\tAdded '{title}' to the inventory.")

    def view_inventory(self):
        if not self.inventory:
            print("\tInventory is empty.")
        else:
            print("\tBook Inventory:")
            for idx, book in enumerate(self.inventory, start=1):
                print(f"\t{idx}. Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Price: ${book.price}, Quantity: {book.quantity}")

    def search_book(self, title):
        found_books = [book for book in self.inventory if title.lower() in book.title.lower()]
        if found_books:
            print(f"\tFound {len(found_books)} book(s) matching '{title}':")
            for idx, book in enumerate(found_books, start=1):
                print(f"\t{idx}. Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Price: ${book.price}, Quantity: {book.quantity}")
        else:
            print(f"\tNo books found with '{title}' in the title.")

    def edit_book(self, title):
        found_books = [book for book in self.inventory if title.lower() in book.title.lower()]
        if found_books:
            print(f"\tFound {len(found_books)} book(s) matching '{title}':")
            for idx, book in enumerate(found_books, start=1):
                print(f"\t{idx}. Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Price: ${book.price}, Quantity: {book.quantity}")
            book_index = int(input("Enter the number of the book to edit: ")) - 1
            if 0 <= book_index < len(found_books):
                book = found_books[book_index]
                new_quantity = int(input("Enter new quantity: "))
                book.quantity = new_quantity
                print(f"\tUpdated quantity for '{book.title}' to {new_quantity}.")
            else:
                print("\tInvalid book number.")
        else:
            print(f"\tNo books found with '{title}' in the title.")

    def delete_book(self, title):
        found_books = [book for book in self.inventory if title.lower() in book.title.lower()]
        if found_books:
            print(f"\tFound {len(found_books)} book(s) matching '{title}':")
            for idx, book in enumerate(found_books, start=1):
                print(f"\t{idx}. Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Price: ${book.price}, Quantity: {book.quantity}")
            book_index = int(input("Enter the number of the book to delete: ")) - 1
            if 0 <= book_index < len(found_books):
                deleted_book = self.inventory.pop(self.inventory.index(found_books[book_index]))
                print(f"\tDeleted '{deleted_book.title}' from the inventory.")
            else:
                print("\tInvalid book number.")
        else:
            print(f"\tNo books found with '{title}' in the title.")

class FileHandler:
    @staticmethod
    def save_inventory_to_file(filename, inventory):
        with open(filename, 'wb') as file:
            pickle.dump(inventory, file)

    @staticmethod
    def load_inventory_from_file(filename):
        try:
            with open(filename, 'rb') as file:
                inventory = pickle.load(file)
            return inventory
        except FileNotFoundError:
            return []

class BookstoreManager:
    def __init__(self, inventory_file):
        self.inventory_file = inventory_file
        self.bookstore = Bookstore()

    def load_inventory(self):
        self.bookstore.inventory = FileHandler.load_inventory_from_file(self.inventory_file)
        print(f"\tInventory loaded from '{self.inventory_file}'.")

    def save_inventory(self):
        FileHandler.save_inventory_to_file(self.inventory_file, self.bookstore.inventory)
        print(f"\tInventory saved to '{self.inventory_file}'.")

def print_inventory_table(inventory):
    if not inventory:
        print("\tInventory is empty.")
    else:
        table = PrettyTable()
        table.field_names = ["#", "Title", "Author", "ISBN", "Price", "Quantity"]
        for idx, book in enumerate(inventory, start=1):
            table.add_row([idx, book.title, book.author, book.isbn, f"${book.price}", book.quantity])
        print(table)

def main():
    inventory_file = "inventory.pkl"
    manager = BookstoreManager(inventory_file)

    while True:
        print("\t")
        print("\t-----------------------------------------")
        print("\t Bookstore Inventory Management System")
        print("\t ----------------------------------------- \n")
        print("\t 1. Add a book to the inventory")
        print("\t 2. View inventory")
        print("\t 3. Search for a book by title")
        print("\t 4. Edit a book")
        print("\t 5. Delete a book")
        print("\t 6. Load inventory from file")
        print("\t 7. Save inventory to file")
        print("\t 8. Quit")
        print("\t -----------------------------------------")

        choice = input("\t Enter your choice: ")

        if choice == "1":
            title = input("\t Enter book title: ")
            author = input("\t Enter author: ")
            isbn = input("\t Enter ISBN: ")
            price = float(input("\t Enter price: "))
            quantity = int(input("\t Enter quantity: "))
            manager.bookstore.add_book(title, author, isbn, price, quantity)
        elif choice == "2":
            print_inventory_table(manager.bookstore.inventory)
        elif choice == "3":
            title = input("Enter the title to search for: ")
            manager.bookstore.search_book(title)
        elif choice == "4":
            title = input("Enter the title of the book to edit: ")
            manager.bookstore.edit_book(title)
        elif choice == "5":
            title = input("Enter the title of the book to delete: ")
            manager.bookstore.delete_book(title)
        elif choice == "6":
            manager.load_inventory()
        elif choice == "7":
            manager.save_inventory()
        elif choice == "8":
            print("\tGoodbye!")
            break
        else:
            print("\tInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
