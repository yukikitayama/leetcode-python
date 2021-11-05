"""
- Increment the decrease
- If the amount after decrease is negative
  - Break
- Count the increment
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        count = 0
        while n >= 0:
            n = n - i
            count += 1
            i += 1
        return count - 1


print(Solution().arrangeCoins(5))
print(Solution().arrangeCoins(8))

