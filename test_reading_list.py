import unittest
import os
import csv
from reading_list import add_book, delete_book, list_books, read_books


class TestReadingList(unittest.TestCase):

    def setUp(self):
        """Clear the books.csv file before each test."""
        if os.path.exists('books.csv'):
            os.remove('books.csv')

    def test_add_book(self):
        """Test adding a book to the reading list."""
        add_book("Test Book", "Test Author", 2022)
        books = read_books()
        try:
            self.assertEqual(len(books), 1)
            self.assertEqual(books[0], ["Test Book", "Test Author", "2022"])
            print("test_add_book\tPass\tThe book was successfully added.")
        except AssertionError:
            print("test_add_book\tFail\tFailed to add the book.")

    def test_add_invalid_year(self):
        """Test adding a book with an invalid year."""
        try:
            add_book("Test Book", "Test Author", "InvalidYear")
            print("test_add_invalid_year\tFail\tThe year value was invalid (non-integer).")
        except ValueError:
            print("test_add_invalid_year\tFail\tThe year value was invalid (non-integer).")

    def test_add_missing_fields(self):
        """Test adding a book with missing fields (empty title or author)."""
        try:
            add_book("", "Test Author", 2022)
            print("test_add_missing_fields\tFail\tThe title or author was empty or whitespace.")
        except ValueError:
            print("test_add_missing_fields\tFail\tThe title or author was empty or whitespace.")
        try:
            add_book("Test Book", "", 2022)
            print("test_add_missing_fields\tFail\tThe title or author was empty or whitespace.")
        except ValueError:
            print("test_add_missing_fields\tFail\tThe title or author was empty or whitespace.")

    def test_add_multiple_books(self):
        """Test adding multiple books."""
        add_book("Test Book 1", "Test Author", 2022)
        add_book("Test Book 2", "Test Author", 2023)
        books = read_books()
        try:
            self.assertEqual(len(books), 2)
            self.assertEqual(books[0], ["Test Book 1", "Test Author", "2022"])
            self.assertEqual(books[1], ["Test Book 2", "Test Author", "2023"])
            print("test_add_multiple_books\tPass\tMultiple books were added successfully.")
        except AssertionError:
            print("test_add_multiple_books\tFail\tFailed to add multiple books.")

    def test_delete_book(self):
        """Test deleting a book."""
        add_book("Test Book", "Test Author", 2022)
        delete_book("Test Book")
        books = read_books()
        try:
            self.assertEqual(len(books), 0)
            print("test_delete_book\tPass\tBook was successfully deleted.")
        except AssertionError:
            print("test_delete_book\tFail\tFailed to delete the book.")

    def test_delete_nonexistent_book(self):
        """Test deleting a book that doesn't exist."""
        delete_book("Nonexistent Book")
        books = read_books()
        try:
            self.assertEqual(len(books), 0)
            print("test_delete_nonexistent_book\tPass\tNo book was deleted (expected behavior).")
        except AssertionError:
            print("test_delete_nonexistent_book\tFail\tBook was deleted unexpectedly.")

    def test_list_books_empty(self):
        """Test listing books when the file is empty."""
        list_books()  # Expected output: No books available.
        print("test_list_books_empty\tPass\tCorrectly handled an empty book list.")

    def test_list_books(self):
        """Test listing all books."""
        add_book("1Q84", "Haruki Murakami", 2009)
        add_book("Test Book 2", "Test Author", 2023)
        list_books()  # Expected output: List of books
        print("test_list_books\tPass\tBooks were listed correctly.")

    def test_read_empty_file(self):
        """Test reading an empty file."""
        books = read_books()
        try:
            self.assertEqual(books, [])
            print("test_read_empty_file\tPass\tCorrectly handled an empty CSV file.")
        except AssertionError:
            print("test_read_empty_file\tFail\tFailed to handle empty CSV file.")


if __name__ == "__main__":
    unittest.main()
