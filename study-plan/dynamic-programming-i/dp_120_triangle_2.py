from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_row = triangle[0]
        for row in range(1, len(triangle)):
            curr_row = []

            for col in range(row + 1):
                smallest_above = float('inf')
                # middle and right edge case
                if col > 0:
                    smallest_above = prev_row[col - 1]
                # middle and left edge case
                if col < row:
                    smallest_above = min(smallest_above, prev_row[col])
                curr_row.append(triangle[row][col] + smallest_above)

            prev_row = curr_row

        # Don't return min(curr_row) because if triangle length is 1,
        # it doesn't go inside the for loop, so curr_row is not made
        return min(prev_row)


"""
Buttom-up dynamic programming with auxiliary space
Time: O(n^2), Space: O(n)
"""



triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]
print(Solution().minimumTotal(triangle))
