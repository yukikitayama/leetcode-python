"""
- Combinations of first element and end element
"""


from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        min_so_far = arrays[0][0]
        max_so_far = arrays[0][-1]

        for i in range(1, len(arrays)):
            ans = max(ans, abs(arrays[i][0] - max_so_far), abs(arrays[i][-1] - min_so_far))
            max_so_far = max(max_so_far, arrays[i][-1])
            min_so_far = min(min_so_far, arrays[i][0])

        return ans


arrays = [[1,2,3],[4,5],[1,2,3]]
print(Solution().maxDistance(arrays))

