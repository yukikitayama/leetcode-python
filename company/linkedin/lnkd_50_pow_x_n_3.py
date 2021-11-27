class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        ans = 1
        for _ in range(n):
            ans = ans * x
        return ans


"""
- Time is O(n), space is O(1)
"""


x = 2.00000
n = 10
# x = 2.10000
# n = 3
# x = 2.00000
# n = -2
print(Solution().myPow(x, n))

