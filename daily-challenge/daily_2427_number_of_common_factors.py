class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0

        for factor in range(1, min(a, b) + 1):

            if (a % factor == 0) and (b % factor == 0):
                ans += 1

        return ans