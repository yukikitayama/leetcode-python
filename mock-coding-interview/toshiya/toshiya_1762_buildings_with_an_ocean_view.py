from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        max_so_far = 0

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_so_far:
                ans.append(i)
            max_so_far = max(max_so_far, heights[i])

        # ans = ans[::-1]
        ans.reverse()

        return ans

"""
T: O(2N)
S: O(1)
"""