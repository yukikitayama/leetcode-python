class MyCalendarTwo:

    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        # Find triple booking from double booking
        for s, e in self.overlaps:
            if start < e and s < end:
                return False

        # Compute double booking
        for s, e in self.calendar:
            if start < e and s < end:
                overlap_start = max(start, s)
                overlap_end = min(end, e)
                self.overlaps.append([overlap_start, overlap_end])

        # Save all the data
        self.calendar.append([start, end])

        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)