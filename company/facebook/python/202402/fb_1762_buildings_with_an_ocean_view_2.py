"""
min so far from right
push index to array
reverse the array
"""

from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        min_so_far = 0

        ans = []

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > min_so_far:
                ans.append(i)

            min_so_far = max(heights[i], min_so_far)

        ans.reverse()

        return ans
