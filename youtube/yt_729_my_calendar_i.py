class MyCalendar:
    def __init__(self):
        # Set: {(start1, end1), (start2, end2), ...}
        self.calendar = set()

    def book(self, start: int, end: int) -> bool:
        for bookedStart, bookedEnd in self.calendar:
            if start < bookedEnd and end > bookedStart:
                return False
        self.calendar.add((start, end))
        return True


test = [[10, 20], [15, 25], [20, 30]]
mycalendar = MyCalendar()
for start, end in test:
    print(mycalendar.book(start, end))
