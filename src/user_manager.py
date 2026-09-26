from src.database import get_connection
from src.validators import validate_user_id,validate_name,validate_email


class UserManager:
    
    def add_user(self, user_id, name, email):
        if not validate_user_id(user_id):
            print("Invalid user ID.")
            return

        if not validate_name(name):
            print("User name cannot be empty.")
            return

        if not validate_email(email):
            print("Invalid email address.")
            return

        connection = get_connection()
        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO users (user_id, name, email)
                VALUES (?, ?, ?)
                """,
                (user_id, name, email)
            )

            connection.commit()
            print("User registered successfully!")

        except Exception as error:
            print(f"Error registering user: {error}")

        finally:
            connection.close()

    def display_users(self):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT user_id, name, email FROM users"
        )

        users = cursor.fetchall()
        connection.close()

        if not users:
            print("No users registered.")
            return

        print("\n--- Registered Users ---")

        for user in users:
            print(
                f"ID: {user[0]} | "
                f"Name: {user[1]} | "
                f"Email: {user[2]}"
            )

    def search_user(self, user_id):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT user_id, name, email
            FROM users
            WHERE user_id = ?
            """,
            (user_id,)
        )

        user = cursor.fetchone()
        connection.close()

        if user:
            print("\nUser found!")
            print(f"ID: {user[0]}")
            print(f"Name: {user[1]}")
            print(f"Email: {user[2]}")

            return user

        print("User not found.")
        return None