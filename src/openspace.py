import table
import random

class OpenSpace:
    """This class represents an open space with a list of tables"""

    def __init__(self, number_of_tables):
        self.tables = [table.Table(4) for _ in range(number_of_tables)]

    def __str__(self) -> str:
        return f"{self.tables}"

    def organize(self, names):
        """Assign students to seats in tables at random"""
        random.shuffle(names)
        for name in names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break
  