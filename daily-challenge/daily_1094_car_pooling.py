"""
- stack
"""


from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0] * 1001
        for trip in trips:
            timestamp[trip[1]] += trip[0]
            timestamp[trip[2]] -= trip[0]

        used_capacity = 0
        for t in timestamp:
            used_capacity += t
            if used_capacity > capacity:
                return False
        return True


class Solution2:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = []
        for trip in trips:
            # trip: [numPassenger, from, to]
            timestamp.append([trip[1], trip[0]])
            # -trip to decrease number of passenger later
            timestamp.append([trip[2], -trip[0]])

        timestamp.sort()

        used_capacity = 0
        for time, passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True


"""
- sort time O(NlogN)
"""


class Solution1:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr = 0
        prev = 0
        to = []
        for t in trips:

            if to and to[-1] > t[1]:
                curr += t[0]
                # print(f'  if1')
            elif to and to[-1] <= t[1]:
                curr -= prev
                curr += t[0]
                to.pop()
                # print(f'  if2')
            elif not to:
                curr += t[0]
                # print(f'  if3')

            if curr > capacity:
                # print(f'  curr: {curr}, capacity: {capacity}')
                return False

            prev = curr
            to.append(t[2])

            # print(f'curr: {curr}')

        return True


if __name__ == '__main__':
    trips = [[1, 1, 2], [1, 3, 4]]
    capacity = 2  # true
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 5  # true
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4  # false
    trips = [[2, 1, 5], [3, 5, 7]]
    capacity = 3  # true
    trips = [[2, 2, 6], [2, 4, 7], [8, 6, 7]]
    capacity = 11
    print(Solution().carPooling(trips, capacity))
