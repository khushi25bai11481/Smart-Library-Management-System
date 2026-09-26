# Smart Library Management System

## Project Overview

The Python-based application which is designed to manage the library books, registered users, book issuing and returning and library reports is the Smart Library Management System.

This system uses Python and SQLite for managing the dataand provides a command-line interface for performing the ibrary operations.

## Features

- Display all library books
- Search for a book
- Register users
- Display registered users
- Search for users
- Issue books
- Return books
- Generate library reports
- Input validation
- SQLite database storage
- Automated validation testing using pytest

## Technologies Used

- Python 3
- SQLite
- pytest
- Visual Studio Code

## Project Structure

```text
Smart-Library-Management-System/
│
├── src/
│   ├── book_manager.py
│   ├── database.py
│   ├── issue_manager.py
│   ├── reports.py
│   ├── user_manager.py
│   └── validators.py
│
├── tests/
│   └── test_validators.py
│
├── library.db
├── main.py
└── README.md