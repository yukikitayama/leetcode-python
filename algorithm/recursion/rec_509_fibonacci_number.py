"""
- Time: 2m
- Solved: 1
- Saw solution: 0
- Optimized: 1
"""


class Solution:
    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:

        if n < 2:
            return n

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]


if __name__ == '__main__':
    print(Solution().fib(1))
    print(Solution().fib(2))
    print(Solution().fib(3))
    print(Solution().fib(4))
