"""
Brute force
T: O(N**2)

eg1
  {2, 5}
  iterate
    i: 0
      k - 0
"""

from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices = []
        for i in range(len(nums)):
            if nums[i] == key:
                key_indices.append(i)

        ans = []

        # Brute force
        for i in range(len(nums)):
            for j in key_indices:
                if abs(i - j) <= k:
                    ans.append(i)
                    break

        return ans
