from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []

        for row_num in range(numRows):

            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
                print(f'row_num: {row_num}, j: {j}')

            triangle.append(row)

        return triangle


numRows = 4
print(Solution().generate(numRows))