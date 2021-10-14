"""
- if rowIndex is 0, return [1]
- If rowIndex is 1, return [1, 1]
- If row index is greater than or equal to 2, row is created by the previous row
  - current row[i] = previous row[i - 1] + previous row[i]
"""


from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            prev_row = [1, 1]
            for row in range(2, rowIndex + 1):
                current_row = [1]

                # print(f'row: {row}')

                for col in range(1, row):

                    # print(f'col: {col}')

                    value = prev_row[col - 1] + prev_row[col]
                    current_row.append(value)
                current_row.append(1)
                prev_row = current_row
            return current_row


"""
Test
rowIndex: 3
prev_row: [1, 1]
row: 2, current_row: [1], 
  col: 1, value: prev_row[0] + prev_row[1] = 2, current_row: [1, 2]
  current_row: [1, 2, 1], prev_row: [1, 2, 1]
row: 3, current_row: [1],
  col: 1, value: prev_row[0] + prev_row[1] = 3, current_row: [1, 3]
    col: 2, value: prev_row[1] + prev_row[2] = 3, current_row: [1, 3, 3]
  current_row: [1, 3, 3, 1], prev_row: [1, 3, 3, 1]
"""


print(Solution().getRow(4))



