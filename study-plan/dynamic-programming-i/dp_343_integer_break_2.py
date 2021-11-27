"""
- implicit differentiation
  - https://www.khanacademy.org/math/ap-calculus-ab/ab-differentiation-2-new/ab-3-2/v/implicit-differentiation-1
- derivative of x ^ x
  - https://www.youtube.com/watch?v=9_EAZExCJkQ

f(x) = x^(n/x)
y = x^(n/x)
- derivative of x^x and implicit differentiation is in instagram
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        # n: 0 to 6
        case = [0, 0, 1, 2, 4, 6, 9]
        if n < 7:
            return case[n]

        # n - 6 because e.g. n: 7, we only need to append one cell for n: 7
        dp = case + [0] * (n - 6)
        for i in range(7, n + 1):
            dp[i] = 3 * dp[i - 3]

        return dp[-1]