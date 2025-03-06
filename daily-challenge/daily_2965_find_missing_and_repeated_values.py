from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        nums_set = set()
        ans = [0] * 2

        # Nested for loop
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # If current num in set, add to ans
                if grid[r][c] in nums_set:
                    ans[0] = grid[r][c]
                nums_set.add(grid[r][c])

        # For loop from 1 to n*2
        for num in range(1, len(grid) ** 2 + 1):
            # If current num is not in set, add to ans
            if num not in nums_set:
                ans[1] = num

        return ans