"""
k: 1
  1 * 2 / 2 = 1
k: 2
  2 * 3 / 2 = 3
k: 3, 6
  3 * 4 / 2 = 6
k(k + 1)/2

Find max k s.t. k(k + 1)/2
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2

            total_coin = mid * (mid + 1) / 2

            if total_coin == n:
                return mid

            # Invalid
            elif total_coin > n:
                right = mid - 1

            # Valid
            elif total_coin < n:
                left = mid + 1

        return left - 1
