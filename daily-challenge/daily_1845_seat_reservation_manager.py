"""
Boolean array
"""

import heapq


class SeatManager:
    def __init__(self, n: int):
        self.min_heap = [i for i in range(1, n + 1)]
        heapq.heapify(self.min_heap)

    def reserve(self) -> int:
        min_seat_index = heapq.heappop(self.min_heap)
        return min_seat_index

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.min_heap, seatNumber)


class SeatManager2:
    def __init__(self, n: int):
        self.min_heap = []
        heapq.heapify(self.min_heap)
        self.marker = 1

    def reserve(self) -> int:
        if self.min_heap:
            min_seat_index = heapq.heappop(self.min_heap)
            return min_seat_index
        else:
            seat_index = self.marker
            self.marker += 1
            return seat_index

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.min_heap, seatNumber)

