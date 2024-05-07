"""
Find maximum possible minimum sum of all subarrays
"""

from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:

        left = min(sweetness)
        right = sum(sweetness) // (k + 1)

        while left <= right:

            mid = (left + right) // 2

            # print(left, mid, right)

            # Check if current mid is workable
            curr = 0
            count = 0
            for s in sweetness:

                curr += s

                if curr >= mid:
                    count += 1
                    curr = 0

            # Workable
            if count >= k + 1:
                ans = mid

                # Find bigger workable
                left = mid + 1

            else:
                right = mid - 1

        return ans