class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        current = 0
        prev1 = 1
        prev2 = 0

        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return current
