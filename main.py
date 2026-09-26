from src.book_manager import BookManager
from src.user_manager import UserManager
from src.issue_manager import IssueManager
from src.database import create_tables
from src.reports import LibraryReports


def main():
    create_tables()

    library = BookManager()
    users = UserManager()
    issue_manager = IssueManager()
    reports = LibraryReports()

    while True:
        print("\n===================================")
        print("     SMART LIBRARY MANAGEMENT")
        print("===================================")
        print("1. Display Books")
        print("2. Search Book")
        print("3. Display Users")
        print("4. Search User")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Library Report")
        print("8. Register User")
        print("0. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()

        elif choice == "2":
            title = input("Enter book title: ")
            library.search_book(title)

        elif choice == "3":
            users.display_users()

        elif choice == "4":
            user_id = input("Enter user ID: ")
            users.search_user(user_id)

        elif choice == "5":
            book_id = input("Enter book ID: ")
            user_id = input("Enter user ID: ")

            issue_manager.issue_book(
                library,
                users,
                book_id,
                user_id
            )

        elif choice == "6":
            book_id = input("Enter book ID: ")

            issue_manager.return_book(
                library,
                book_id
            )

        elif choice == "7":
            reports.display_report()

        elif choice == "8":
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            email = input("Enter email: ")
            users.add_user(user_id, name, email)

        elif choice == "0":
            print("\nThank you for using Smart Library Management System!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 0 to 8.")


if __name__ == "__main__":
    main()