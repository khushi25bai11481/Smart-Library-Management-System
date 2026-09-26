import re


def validate_book_id(book_id):
    if not book_id.strip():
        return False

    return True


def validate_title(title):
    if not title.strip():
        return False

    return True


def validate_author(author):
    if not author.strip():
        return False

    return True


def validate_user_id(user_id):
    if not user_id.strip():
        return False

    return True


def validate_name(name):
    if not name.strip():
        return False

    return True


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(pattern, email) is not None