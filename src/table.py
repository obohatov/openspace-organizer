class Seat:
    def __init__(self):
        self.free = True
        self.student = None

    def __str__(self) -> str:
        return f"{self.free} {self.student}"

    def set_student(self, name):
        if self.free:
            self.student = name
            self.free = False

    def remove_student(self):
        student = self.student
        self.student = None
        self.free = True
        return student

class Table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]
    
    def __str__(self) -> str:
        return f"{self.capacity} {self.seats}"
    