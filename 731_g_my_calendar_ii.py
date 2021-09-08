class MyCalendarTwo:
    def __init__(self):
        # Store all the intervals
        self.calendar = []
        # ?
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # Track triple book
        for start_double_booked, end_double_booked in self.overlaps:
            # If the current book request is overlap with double book intervals
            # It's triple book,so return False
            if start < end_double_booked and end > start_double_booked:
                return False
        # Track double book
        for start_every_booked, end_every_booked in self.calendar:
            if start < end_every_booked and end > start_every_booked:
                # Update double book interval
                start_updated = max(start, start_every_booked)
                end_updated = min(end, end_every_booked)
                self.overlaps.append((start_updated, end_updated))

        # Store new data
        self.calendar.append((start, end))
        return True


"""
Time complexity
Let n the number of events booked, O(n)?

Space complexity
O(n) because calendar plus overlap lists are O(n + n) = O(2n) = O(n)
"""

