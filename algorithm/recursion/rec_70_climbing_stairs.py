"""
- Time: 3m
- Solved: 1
- Saw solution: 0
- Optimized: 1
"""


class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]


if __name__ == '__main__':
    print(Solution().climbStairs(2))
    print(Solution().climbStairs(3))
