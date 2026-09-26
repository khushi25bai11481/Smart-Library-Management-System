from src.database import get_connection
from src.validators import validate_book_id,validate_title,validate_author


class BookManager:
    def add_book(self, book_id, title, author):
            connection = get_connection()
            cursor = connection.cursor()
    
            try:
                cursor.execute(
                    """
                    INSERT INTO books (book_id, title, author, available)
                    VALUES (?, ?, ?, ?)
                    """,
                    (book_id, title, author, 1)
                )
    
                connection.commit()
                print("Book added successfully!")
    
            except Exception as error:
                print(f"Error adding book: {error}")
    
            finally:
                connection.close()
    
    def display_books(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT book_id, title, author, available FROM books"
        )

        books = cursor.fetchall()
        connection.close()

        if not books:
            print("No books available.")
            return

        print("\n--- Library Books ---")

        for book in books:
            status = "Available" if book[3] else "Issued"

            print(
                f"ID: {book[0]} | "
                f"Title: {book[1]} | "
                f"Author: {book[2]} | "
                f"Status: {status}"
            )

    def search_book(self, title):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT book_id, title, author, available
            FROM books
            WHERE LOWER(title) = LOWER(?)
            """,
            (title,)
        )

        book = cursor.fetchone()
        connection.close()

        if book:
            print("\nBook found!")
            print(f"ID: {book[0]}")
            print(f"Title: {book[1]}")
            print(f"Author: {book[2]}")
            print(
                f"Status: "
                f"{'Available' if book[3] else 'Issued'}"
            )

            return book

        print("Book not found.")
        return None