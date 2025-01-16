import pytest
from src.assert_examples import(
    division,
    square_root,
    validate_email,
    delete_file,
    invalid_email_error,
)


def test_division_zero_division_error():
    """
    Test that a ZeroDivisionError is raised when the second argument is 0  
    """
    