class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 0 if n == 0 else 1

        current = 0
        prev1 = 1
        prev2 = 1
        prev3 = 0

        for _ in range(3, n + 1):
            current = prev1 + prev2 + prev3
            prev3 = prev2
            prev2 = prev1
            prev1 = current

        return current


"""
Time complexity
O(n)

Space complexity
O(1)
"""


print(Solution().tribonacci(25))
