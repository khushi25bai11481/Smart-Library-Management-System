from datetime import datetime
from src.database import get_connection


class IssueManager:

    def issue_book(self, book_manager, user_manager, book_id, user_id):
        connection = get_connection()
        cursor = connection.cursor()

        # Check whether the book exists
        cursor.execute(
            "SELECT book_id, title, available FROM books WHERE book_id = ?",
            (book_id,)
        )
        book = cursor.fetchone()

        if book is None:
            print("Book not found.")
            connection.close()
            return

        # Check whether the user exists
        cursor.execute(
            "SELECT user_id, name FROM users WHERE user_id = ?",
            (user_id,)
        )
        user = cursor.fetchone()

        if user is None:
            print("User not found.")
            connection.close()
            return

        # Check availability
        if book[2] == 0:
            print("Book is already issued.")
            connection.close()
            return

        # Mark book as issued
        cursor.execute(
            "UPDATE books SET available = 0 WHERE book_id = ?",
            (book_id,)
        )

        # Store issue record
        issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute(
            """
            INSERT INTO issued_books (book_id, user_id, issue_date)
            VALUES (?, ?, ?)
            """,
            (book_id, user_id, issue_date)
        )

        connection.commit()
        connection.close()

        print("Book issued successfully!")

    def return_book(self, book_manager, book_id):
        connection = get_connection()
        cursor = connection.cursor()

        # Check whether the book is issued
        cursor.execute(
            "SELECT book_id FROM issued_books WHERE book_id = ?",
            (book_id,)
        )

        record = cursor.fetchone()

        if record is None:
            print("This book is not currently issued.")
            connection.close()
            return

        # Make the book available again
        cursor.execute(
            "UPDATE books SET available = 1 WHERE book_id = ?",
            (book_id,)
        )

        # Remove issue record
        cursor.execute(
            "DELETE FROM issued_books WHERE book_id = ?",
            (book_id,)
        )

        connection.commit()
        connection.close()

        print("Book returned successfully!")

    def display_issued_books(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                issued_books.book_id,
                books.title,
                issued_books.user_id,
                users.name,
                issued_books.issue_date
            FROM issued_books
            JOIN books
                ON issued_books.book_id = books.book_id
            JOIN users
                ON issued_books.user_id = users.user_id
            """
        )

        records = cursor.fetchall()
        connection.close()

        if not records:
            print("No books are currently issued.")
            return

        print("\n--- Issued Books ---")

        for record in records:
            print(
                f"Book ID: {record[0]} | "
                f"Title: {record[1]} | "
                f"User ID: {record[2]} | "
                f"User: {record[3]} | "
                f"Issue Date: {record[4]}"
            )