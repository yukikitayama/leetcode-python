"""
seats = [4,1,5,9], students = [1,3,2,6]
0 + 2 + 2 + 3 =
"""

from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        diff = [0] * max(max(seats), max(students))
        for i in range(len(seats)):
            diff[seats[i] - 1] += 1
            diff[students[i] - 1] -= 1

        # print(diff)

        ans = 0
        unmatched = 0
        for d in diff:
            ans += abs(unmatched)
            unmatched += d
        return ans

    def minMovesToSeat1(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0

        for i in range(len(seats)):
            ans += abs(seats[i] - students[i])

        return ans
