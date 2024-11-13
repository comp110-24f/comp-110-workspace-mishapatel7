"""File to define Fish class."""

__author__ = "730742455"


class Fish:
    """Fish class."""

    age: int

    def __init__(self):
        """__init__ function for fish class."""
        self.age = 0
        return None

    def one_day(self):
        """one_day function for Bear class."""
        self.age += 1
        return None
