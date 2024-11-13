"""File to define Bear class."""

__author__ = "730742455"


class Bear:
    """Class defining Bears."""

    age: int
    hunger_score: int

    def __init__(self):
        """__init__ function for Bear class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """One_day function for Bear class."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Eat function for Bear class."""
        self.hunger_score += num_fish
        return None
