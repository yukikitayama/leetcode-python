"""

  Current element to be in current subarray
  Current element to start a new subarray
"""

from typing import List
import functools


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(i):

            # Base case
            if i >= len(arr):
                return 0

            ans = 0
            max_so_far = 0
            end = min(len(arr), i + k)

            for j in range(i, end):

                max_so_far = max(max_so_far, arr[j])

                ans = max(ans, max_so_far * (j - i + 1) + dp(j + 1))

            return ans

        return dp(0)


if __name__ == "__main__":
    arr = [1, 15, 7, 9, 2, 5, 10]
    k = 3
    # 84

    arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
    k = 4
    # 83

    print(Solution().maxSumAfterPartitioning(arr, k))


