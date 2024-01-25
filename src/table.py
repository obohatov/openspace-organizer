class Seat:
    """Define a seat with a student"""
    
    def __init__(self):
        self.free = True
        self.occupant = None

    def __str__(self) -> str:
        return f"This seat are free: {self.free} {self.occupant}"

    def set_occupant(self, name):
        """Assign a seat if it's free"""
        if self.free:
            self.occupant = name
            self.free = False

    def remove_occupant(self):
        """Remove a student and return the student's name"""
        occupant = self.occupant
        self.occupant = None
        self.free = True
        return occupant

class Table:
    """This class represents a table with a list of seats"""
    
    def __init__(self, capacity = 4):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]
    
    def __str__(self) -> str:
        return f"{self.capacity} {self.seats}"
    
    def has_free_spot(self):
        """Check is the table has free spot""" 
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name):
        """Assign someone to the first available seat in the table"""
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return

    def capacity_left(self):
        """Return the number of free seats"""
        return len([seat for seat in self.seats if seat.free])
    