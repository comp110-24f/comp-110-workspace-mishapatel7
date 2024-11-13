"""File to define River class."""

__author__ = "730742455"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of the surviving fish."""
        surviving_fish: list[Fish] = []
        for fish in self.fish:  # check each fish to see if it is old enough to survive
            if fish.age <= 3:
                surviving_fish.append(fish)
            self.fish = surviving_fish

        surviving_bears: list[Bear] = []
        for bear in self.bears:  # check the age of each bear using a loop
            if bear.age <= 5:
                surviving_bears.append(bear)
            self.bears = surviving_bears

        return None

    def bears_eating(self):
        """Checks to see how many bears can eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Checks to see if any bears will die off."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """Checks to see how many fish are repopulating."""
        total: int = len(self.fish)
        new_fish_count: int = (total // 2) * 4
        for i in range(new_fish_count):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Checks to see how many bears are repopulating."""
        total: int = len(self.bears)
        new_bears_count: int = total // 2
        for i in range(new_bears_count):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """View river function for a day."""
        print(f"~~~ Day {self.day}: ~~~ ")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Produces 7 river days for a week."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int):
        """Removes amount of fish given."""
        idx: int = amount
        while idx > 0 and len(self.fish):
            self.fish.pop(0)
            idx -= 1
        return None
