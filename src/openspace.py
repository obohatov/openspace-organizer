from src.table import Table
from random import shuffle


class OpenSpace:
    """This class represents an open space with a list of tables"""

    filename = "result.xlsx"

    def __init__(self, number_of_tables = 6):
        self.tables = [Table(4) for _ in range(number_of_tables)]

    def __str__(self) -> str:
        places = []
        for table in self.tables:
            places.append(f"{table.capacity}: {table.seats}")
        return f"Open space with {len(self.tables)} tables ({places})"

    def __str__(self) -> str:
        return f"{self.tables}"

    def organize(self, names):
        """Assign students to seats in tables at random"""
        people_count = len(names)
        total_seats = len(self.tables) * self.tables[0].capacity
        if people_count > total_seats:
            print(f"There are {people_count} students in the room! Not enough seats")
        shuffle(names)
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

    def total_people(self):
        """Return total number of students in openspace"""
        total_people = 0
        for table in self.tables:
            total_people += table.capacity - table.capacity_left()
        return total_people

    def total_seats_left(self):
        """Return number of available seats in openspace"""
        total_seats_left = 0
        for table in self.tables:
            total_seats_left += table.capacity_left()
        return total_seats_left
                    
    def store(self, filename):
        """Store the repartition in Excel file"""
        pass  
