"""
Greedy
Sort
Two pointers
"""

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0

        people.sort()

        left = 0
        right = len(people) - 1

        while left <= right:

            if people[left] + people[right] <= limit:
                ans += 1
                left += 1
                right -= 1
            else:
                ans += 1
                right -= 1

        return ans
