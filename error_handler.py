import re
from datetime import datetime

def validate_input(pattern, user_input):
    """Validate user input against a regex pattern."""
    if not user_input or not isinstance(user_input, str):
        return False
    return bool(re.match(pattern, user_input))

def validate_date(date_str):
    """Validate date string in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_library_id(library_id):
    """Validate library ID format (e.g., LIB-12345)."""
    return validate_input(r'^LIB-\d{5}$', library_id)

def validate_name(name):
    """Validate name (letters, spaces, and hyphens only)."""
    return validate_input(r'^[A-Za-z\s-]+$', name)

def handle_invalid_input(message="Invalid input! Please try again."):
    """Handle invalid input with custom message."""
    print(message)

class LibraryError(Exception):
    """Base exception class for library errors."""
    pass

class BookNotFoundError(LibraryError):
    """Raised when a book is not found."""
    pass

class UserNotFoundError(LibraryError):
    """Raised when a user is not found."""
    pass

class InvalidInputError(LibraryError):
    """Raised when input validation fails."""
    pass
