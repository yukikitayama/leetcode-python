"""
Max so far from right
Iterate from right
collect index higher than max so far
update max so far
Reverse the indices
"""

from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        n = len(heights)
        max_so_far = heights[n - 1]
        ans = [n - 1]

        for i in range(n - 2, -1, -1):

            if heights[i] > max_so_far:
                ans.append(i)
                max_so_far = max(max_so_far, heights[i])

        ans.reverse()

        return ans



