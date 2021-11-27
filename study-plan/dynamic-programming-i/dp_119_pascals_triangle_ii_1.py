from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            # Base case
            base = [1, 1]

            for j in range(rowIndex - 1):

                row = [1]
                for i in range(0, j + 1):
                    row.append(base[i] + base[i + 1])
                row.append(1)

                base = row

            return row


"""
Time complexity: O(rowIndex^2), Space complexity: O(rowIndex)

# rowIndex: 2
row = [1, base[0] + base[1], 1]

# rowIndex: 3
base = row
row = [1, base[0] + base[1], base[1] + base[2], 1]

base = row
row = [1, base[]]
"""
print(Solution().getRow(4))

