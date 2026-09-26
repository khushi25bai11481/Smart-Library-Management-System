from src.database import get_connection


class LibraryReports:

    def total_books(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM books")
        total = cursor.fetchone()[0]

        connection.close()

        return total

    def available_books(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM books WHERE available = 1"
        )
        total = cursor.fetchone()[0]

        connection.close()

        return total

    def issued_books(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM issued_books"
        )
        total = cursor.fetchone()[0]

        connection.close()

        return total

    def total_users(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM users")
        total = cursor.fetchone()[0]

        connection.close()

        return total

    def display_report(self):
        print("\n===== LIBRARY REPORT =====")

        print(f"Total Books: {self.total_books()}")
        print(f"Available Books: {self.available_books()}")
        print(f"Issued Books: {self.issued_books()}")
        print(f"Registered Users: {self.total_users()}")