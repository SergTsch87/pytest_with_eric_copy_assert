import os
import math
import re


class invalid_email_error(Exception):
    """
    Raised when an email address is invalid
    """

    pass


def division(a: int | float, b: int | float) -> float | ZeroDivisionError:
    """
    Returns the result of dividing a by b

    Raises:
        ZeroDivisionError: If b is 0
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed")


def square_root(a: int) -> float | ValueError:
    """
    Returns the square root of a  
  
    Raises:  
        ValueError: If a is negative  
    """
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Square root of negative numbers is not allowed")
    

def delete_file(filename: str) -> None | FileNotFoundError:
    """
    Deletes a file  
  
    Raises:  
        FileNotFoundError: If the file does not exist
    """
    try:
        os.remove(filename)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found")
    

def validate_email(email: str) -> bool | invalid_email_error:
    """
    Validates an email address  
  
    Raises:  
        invalid_email_error: If the email address is invalid
    """
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        raise invalid_email_error("Invalid email adress")