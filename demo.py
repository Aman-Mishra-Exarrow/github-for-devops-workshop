"""
demo.py

This module contains a simple function demonstrating a return value.
"""


def my_function() -> int:
    """
    Return a fixed integer value.

    Returns:
        int: The integer value 5.
    """
    value = 5
    return value


if __name__ == "__main__":
    my_function()
