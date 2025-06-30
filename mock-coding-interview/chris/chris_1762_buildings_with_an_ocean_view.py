from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_so_far = 0
        ans = []
        # Iterate
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_so_far:
                ans.append(i)
            max_so_far = max(max_so_far, heights[i])
        ans.reverse()

        return ans
