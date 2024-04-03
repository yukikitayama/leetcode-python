"""
arr = [2,3,4,7,11], k = 5
max: 11
length: 5
6 numbers are missing: [1, 5, 6, 8, 9, 10]

Ans
  Binary search to find how many integers are missing before a particular element in arr
"""

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            num_missing = arr[mid] - (mid + 1)

            # [2, 3, 4, 7, 11]
            # [1, 2, 3, 4, 5]
            # [1, 1, 1, 3, 6]
            if num_missing < k:
                left = mid + 1
            elif num_missing > k:
                right = mid - 1
            elif num_missing == k:
                right = mid - 1

        # Here right < left, left exceeded right
        # Kth missing integer is between arr[right] and arr[left]
        # We need to subtract the number of missing before arr[right] from k
        # to get between arr[right] and arr[left]
        # arr[right] + k - (arr[right] - (right + 1))
        # = k + right + 1

        return k + right + 1