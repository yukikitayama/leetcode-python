class Solution:
    def climbStairs(self, n: int) -> int:

        def climb_stairs(current, end):
            # Because we cannot go downstairs, there's no way
            if current > end:
                return 0

            # Because current reached at end, so we found a way, so return 1
            if current == end:
                return 1

            else:
                # Every time we can either climb 1 or 2 steps
                return climb_stairs(current + 1, end) + climb_stairs(current + 2, end)

        # We start from current 0 steps to n steps by brute force
        return climb_stairs(0, n)


"""
Time limit exceeded
Time complexity
O(2^n) because every time we have 2 functions to run 
"""


print(Solution().climbStairs(3))
