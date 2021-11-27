from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # print(f'target: {target}, position: {position}, speed: {speed}')

        # Sort the given cars data by furthest from the target by sorting by start position
        # time is the time needed to arrive at the target

        # time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        time = []
        for p, s in sorted(zip(position, speed)):
            t = float(target - p) / s
            # print(f'p: {p}, s: {s}, t: {t}')
            time.append(t)

        # print()

        res = 0
        # current biggest time (slowest car)
        cur = 0

        # Loop over the cars which are the nearest to the target
        # In iteration, if we see a current car which has less time than the previous car,
        # the current car will catch up with the previous car,
        # even if the current car was originally further from the target
        for t in time[::-1]:
            # print(f't: {t}')

            # If current car time is slower than the current slowest (cur),
            # this car cannot catch up, so it needs to form one car fleet
            if t > cur:
                res += 1
                cur = t

            # Otherwise catch up, so car fleet does not increase, so do nothing
        return res




"""
target - position = distance
distance / speed = time

Time complexity
Let n be the number of cars, O(nlogn) to sort position, O(n) to iterate
so O(nlogn + n) = O(nlogn)

Space complexity
O(n) for time data and O(nlogn) for sort
"""



target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
target = 10
position = [3]
speed = [3]
print(Solution().carFleet(target, position, speed))
