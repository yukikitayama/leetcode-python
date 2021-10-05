"""
"""


from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_row = triangle[0]
        for row in range(1, len(triangle)):

            curr_row = []

            for col in range(row + 1):

                if col == 0:
                    value = triangle[row][col] + prev_row[col]

                elif col == row:
                    value = triangle[row][col] + prev_row[col - 1]

                else:
                    value = triangle[row][col] + min(
                        prev_row[col - 1],
                        prev_row[col]
                    )
                curr_row.append(value)
            prev_row = curr_row

        return min(prev_row)



triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# triangle = [[-10]]
print(Solution().minimumTotal(triangle))



