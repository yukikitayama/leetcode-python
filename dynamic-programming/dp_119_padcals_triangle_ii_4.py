from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        # rowIndex: 0 skips this for loop
        for i in range(rowIndex):

            print(f'i: {i}')

            # rowIndex : 1 skips this for loop
            for j in range(i, 0, -1):

                print(f'j: {j}')

                row[j] = row[j] + row[j - 1]
            print(f'  before: {row}')
            row.append(1)
            print(f'  after: {row}')
            print()

        return row


print(Solution().getRow(3))

