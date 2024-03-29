import pandas as pd

from src.table import Table
from random import shuffle


class OpenSpace:
    """This class represents an open space with a list of tables"""

    def __init__(self, number_of_tables = 6):
        self.tables = [Table(4) for _ in range(number_of_tables)]
    
    def __str__(self) -> str:
        return f"Open space with {len(self.tables)} tables: {[str(table) for table in self.tables]}"

    def organize(self, names):
        """Assign students to seats in tables at random"""
        people_count = len(names)
        total_seats = len(self.tables) * self.tables[0].capacity
        if people_count > total_seats:
            print(f"There are {people_count} students in the room! Not enough seats")
        shuffle(names)
        while names:
            for table in self.tables:
                if table.has_free_spot() and names:
                    name = names.pop()
                    table.assign_seat(name)

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
        data = {'Table': [], 'Seat': [], 'Occupant': []}

        for i, table in enumerate(self.tables, start=1):
            for j, seat in enumerate(table.seats, start=1):
                data['Table'].append(i)
                data['Seat'].append(j)
                data['Occupant'].append(seat.occupant if seat.occupant else "Empty")

        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
