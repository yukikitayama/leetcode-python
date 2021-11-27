"""
- TLE by O(n)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            # Move negative sign from n to x
            x = 1 / x
            # Remove negative sign from n
            n = -n

        # Initialize ans to 1 because n cloud be 0
        # when n is 0, for loop is skipped
        ans = 1
        for i in range(n):
            ans = ans * x
        return ans


x = 2.00000
n = 10
x = 2.10000
n = 3
x = 2.00000
n = -2
x = 10
n = 0
print(Solution().myPow(x, n))
