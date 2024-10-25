from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        """T: O(MlogM), S: O(M)"""
        capacity.sort()
        sum_ = sum(apple)
        ans = 0

        for i in range(len(capacity) - 1, -1, -1):

            sum_ -= capacity[i]
            ans += 1

            if sum_ <= 0:
                return ans