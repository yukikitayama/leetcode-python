class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if 0 < n <= 2:
            return 1

        t_n = 0
        t_n_1 = 1
        t_n_2 = 1

        for _ in range(3, n + 1):
            t_n_3 = t_n + t_n_1 + t_n_2
            t_n = t_n_1
            t_n_1 = t_n_2
            t_n_2 = t_n_3

        return t_n_3


"""
Time: O(n), Space: O(1)
"""


print(Solution().tribonacci(4))
print(Solution().tribonacci(25))
