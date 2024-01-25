import table
import random


class OpenSpace:
    """This class represents an open space with a list of tables"""

    filename = "result.xlsx"

    def __init__(self, number_of_tables = 6):
        self.tables = [table.Table(4) for _ in range(number_of_tables)]

    def __str__(self) -> str:
        places = []
        for table in self.tables:
            places.append(f"{table.capacity}: {table.seats}")
        return f"Open space with {len(self.tables)} tables ({places})"

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

    def display(self):
        """Display the tables and students"""
        for i, table in enumerate(self.tables, start=1):
            print(f"Table {i}:")
            for seat in table.seats:
                if seat.free:
                    print("\tEmpty")
                else:
                    print(f"\tOccupied by {seat.occupant}")
                    
    def store(self, filename):
        """Store the repartition in Excel file"""
        pass  
