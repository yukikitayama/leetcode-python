"""
- Brute force with recursion function with memoization
"""


from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = [[False] * len(stones) for _ in range(len(stones))]

        def can_cross(stones, curr_index, jumpsize, memo):
            if memo[curr_index][jumpsize]:
                return memo[curr_index][jumpsize]

            for next_index in range(curr_index + 1, len(stones)):
                gap = stones[next_index] - stones[curr_index]
                if gap in [jumpsize - 1, jumpsize, jumpsize + 1]:
                    if can_cross(stones, next_index, gap, memo):
                        # Why 1
                        memo[next_index][gap] = True
                        return True

            memo[curr_index][jumpsize] = True if curr_index == len(stones) - 1 else False
            return memo[curr_index][jumpsize]

        return can_cross(stones, 0, 0, memo)


stones = [0,1,3,5,6,8,12,17]
# stones = [0,1,2,3,4,8,9,11]
print(Solution().canCross(stones))


