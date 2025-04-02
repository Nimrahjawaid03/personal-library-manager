import json
import os

# File to store library data
LIBRARY_FILE = "library.txt"

# Load existing library data if available
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save library data to a file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Initialize library
library = load_library()

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    })
    print("Book added successfully!")
    save_library(library)

def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            save_library(library)
            return
    print("Book not found.")

def search_book():
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    query = input("Enter search term: ").lower()
    matches = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]
    
    if matches:
        print("Matching Books:")
        for book in matches:
            status = "Read" if book["read"] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No books found.")

def display_books():
    if not library:
        print("Your library is empty.")
        return
    print("Your Library:")
    for book in library:
        status = "Read" if book["read"] else "Unread"
        print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics():
    total_books = len(library)
    if total_books == 0:
        print("No books in library.")
        return
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def main():
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("Library saved to file. Goodbye!")
            save_library(library)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
