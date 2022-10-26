class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n != 0:
            ans += 1
            # Every time one 1-bit disappears
            n = n & (n - 1)

        return ans
