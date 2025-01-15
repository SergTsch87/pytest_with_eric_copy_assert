# Відступи не зробив спеціально для перевірки форматування засобами ruff
import os,math,re
class invalid_mail_error(Exception):
    """
    Raised when an email address is invalid 
    """
    pass
def division(a: int|float, b:int|float)->float|ZeroDivisionError:
    """
    Returns the result of dividing a by b  
  
    Raises:  
        ZeroDivisionError: If b is 0  
    """
    try:
        return a/b
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed")