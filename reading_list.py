import csv
import os

def add_book(title, author, year):
    """Add a book to the reading list."""
    try:
        if not title or not author or title.isspace() or author.isspace():
            raise ValueError("Title and Author cannot be empty or just whitespace.")

        try:
            year = int(year)  # Check if year is an integer
        except ValueError:
            raise ValueError("Invalid year value. Please enter a valid number.")

        file_path = os.path.join(os.getcwd(), 'books.csv')
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([title, author, year])
        print(f'Book added: {title}')
    except ValueError as e:
        print(f"Error: {e}")
        raise e  # Reraise the exception for the test to catch it
    except Exception as e:
        print(f"Unexpected error: {e}")


def read_books():
    """Read all books from the CSV file."""
    file_path = os.path.join(os.getcwd(), 'books.csv')
    if not os.path.exists(file_path):
        return []  # Return an empty list if the file does not exist
    books = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        books = list(reader)
    return books


def list_books():
    """List all books in the reading list."""
    books = read_books()
    if not books:
        print("No books available.")
    else:
        for book in books:
            title, author, year = book
            print(f"Title: {title}, Author: {author}, Year: {year}")


def delete_book(title):
    """Delete a book by title."""
    books = read_books()
    found = False
    file_path = os.path.join(os.getcwd(), 'books.csv')
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for book in books:
            if book[0] == title:
                found = True
            else:
                writer.writerow(book)
    if found:
        print(f"Book deleted: {title}")
    else:
        print("Book not found.")

def clear_books_file():
    """Clear the books.csv file before each test."""
    file_path = os.path.join(os.getcwd(), 'books.csv')
    if os.path.exists(file_path):
        os.remove(file_path)
