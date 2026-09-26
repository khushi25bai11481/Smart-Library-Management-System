from src.validators import (
    validate_book_id,
    validate_title,
    validate_author,
    validate_user_id,
    validate_name,
    validate_email
)


def test_valid_book_id():
    assert validate_book_id("B001") is True


def test_empty_book_id():
    assert validate_book_id("") is False


def test_valid_title():
    assert validate_title("Python Basics") is True


def test_empty_title():
    assert validate_title("") is False


def test_valid_author():
    assert validate_author("John Smith") is True


def test_empty_author():
    assert validate_author("") is False


def test_valid_user_id():
    assert validate_user_id("U001") is True


def test_empty_user_id():
    assert validate_user_id("") is False


def test_valid_name():
    assert validate_name("Rahul Sharma") is True


def test_empty_name():
    assert validate_name("") is False


def test_valid_email():
    assert validate_email("rahul@example.com") is True


def test_invalid_email():
    assert validate_email("invalid-email") is False