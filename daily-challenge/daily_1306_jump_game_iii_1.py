from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True

            # Constraints says we only have positive values, so we mark it negative when we visit the vertex.
            # so we can omit using visited set for DFS
            arr[start] = -arr[start]

            # DFS
            return self.canReach(arr, start - arr[start]) or self.canReach(arr, start + arr[start])

        return False


"""
Time complexity
O(n) in worst case we need to visit all the vertices

Space complexity
O(n) for recursion stack calls
"""


arr = [4,2,3,0,3,1,2]
start = 5
# arr = [3,0,2,1,2]
# start = 2
print(Solution().canReach(arr, start))
