from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Base case
        answer = [
            [1],
            [1, 1]
        ]

        if numRows == 1:
            return [answer[0]]

        elif numRows == 2:
            return answer

        else:
            for r in range(2, numRows):
                row = [1]
                for c in range(1, r):
                    summed = answer[r - 1][c - 1] + answer[r - 1][c]
                    row.append(summed)
                row.append(1)
                answer.append(row)

            return answer

"""
row0: [1]
row1: [1, 1]
row2: [1, (sum of current index - 1 and current index in previous row), 1]
  - sum from 1 to row index exclusively
row3: [
    1,
    (sum of current index - 1 and current index in previous row),
    (sum of current index - 1 and current index in previous row), 
    1]
  - sum from 1 to row index exclusively
"""
print(Solution().generate(5))

