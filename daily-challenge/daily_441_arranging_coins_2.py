"""
- Sum of consecutive integers from 1 to k is
  - (k * (k + 1)) / 2
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:

        left = 0
        right = n
        while left <= right:
            k = left + (right - left) // 2
            curr = (k * (k + 1)) // 2

            if curr == n:
                return k

            elif n < curr:
                right = k - 1

            else:
                left = k + 1

        return right



print(Solution().arrangeCoins(5))
print(Solution().arrangeCoins(8))

