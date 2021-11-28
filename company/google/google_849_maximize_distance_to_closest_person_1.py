from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        N = len(seats)

        # left and right arrays can be initialized with any numbers
        left = [N] * N
        right = [N] * N
        # print(f'left: {left}, right: {right}')

        for i in range(N):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                # i - 1 to get the distance from filled seat
                # left only works for the distance to the left of i
                # +1 for the distance incremented
                left[i] = left[i - 1] + 1
        # print(f'left: {left}')

        for i in range(N - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < N - 1:
                # +1 for the distance incremented as getting far away
                right[i] = right[i + 1] + 1

        # min to get the closest direction
        # max to maximize the distance
        # if not seat because seated seat is 0 in left and right, but it does not mean you can sit there
        return max(min(left[i], right[i]) for i, seat in enumerate(seats) if not seat)


"""
Time complexity
Let n be the length of seats, O(n + n) = O(n)

Space complexity
O(n) for left array and O(n) for right array, so O(n + n) = O(2n) = O(n)
"""


seats = [1,0,0,0,1,0,1]
print(f'Seats: {seats}')
print(Solution().maxDistToClosest(seats))
