# Project Statement

## Project Title

Smart Library Management System

## Problem Statement

It can be very difficult to track book availability, issued books, returned books and registered users when we manage books and library users manually.

The given project provides a simple command-line based library management system by using Python and SQLite.

## Project Objective

The objective of this project is to develop a modular Python application that can:

- Manage library books
- Manage registered users
- Issue and return books
- Search books and users
- Generate library reports
- Validate user input
- Store information using SQLite

## Main Functional Modules

### 1. Book Management

The system allows users to display and search library books.

### 2. User Management

The system allows users to register users, display registered users, and search for users.

### 3. Issue and Return Management

The system allows books to be issued to registered users and returned when they are no longer borrowed.

### 4. Reporting

The system generates a library report containing the total number of books, available books, issued books, and registered users.

### 5. Validation

The system validates book IDs, user IDs, names, titles, authors, and email addresses.

## Technology Used

- Python
- SQLite
- pytest
- Visual Studio Code

## Data Storage

SQLite is used to store:

- Book information
- User information
- Issued book information

## Testing

The project includes automated validation tests using pytest.

The current test suite contains 12 tests, all of which have passed successfully.

## Project Outcome

The completed system provides a modular and executable command-line application for basic library management operations.