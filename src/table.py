class Seat:
    """Define a seat with a student"""
    
    def __init__(self):
        self.free = True
        self.student = None

    def __str__(self) -> str:
        return f"{self.free} {self.student}"

    def set_student(self, name):
        """Assign a seat if it's free"""
        if self.free:
            self.student = name
            self.free = False

    def remove_student(self):
        """Remove a student and return the student's name"""
        student = self.student
        self.student = None
        self.free = True
        return student

class Table:
    """This class represents a table with a list of seats"""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]
    
    def __str__(self) -> str:
        return f"{self.capacity} {self.seats}"
    