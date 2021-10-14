class Tri:
    def __init__(self):
        # Constraints says 0 <= n <= 37, so we don't need 38
        n = 38
        # No need 38 so below is * n instead of * (n + 1)
        self.nums = nums = [0] * n
        nums[1] = nums[2] = 1
        for i in range(3, n):
            nums[i] = nums[i - 1] + nums[i - 2] + nums[i - 3]


class Solution:
    def tribonacci(self, n: int) -> int:
        t = Tri()
        return t.nums[n]


"""
Time complexity
O(1) to precompute, bounded by 38

Space complexity
O(1) as well for 38 bound
"""


print(Solution().tribonacci(25))
