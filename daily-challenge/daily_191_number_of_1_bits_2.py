class Solution:
    def hammingWeight(self, n: int) -> int:

        ans = 0

        while n:
            ans += 1

            # n & (n - 1) flips the least significant 1 bit to 0
            n = n & (n - 1)

        return ans



