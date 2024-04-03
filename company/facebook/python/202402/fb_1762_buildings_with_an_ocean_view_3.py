from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        min_so_far = 0
        ans = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > min_so_far:
                ans.append(i)
                min_so_far = heights[i]

        ans.reverse()

        return ans