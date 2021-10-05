"""
- Make a list in a for loop
- first and second lists are manually made
- from the third list, use the previous list to make the current list
  - current list[i] = previous list[i - 1] + previous list[i]
  - i from 1 to current list length - 2
"""


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            ans = []
            ans.append([1])
            ans.append([1, 1])

            for i in range(2, numRows):
                row = [1]
                for j in range(1, i):
                    value = ans[-1][j - 1] + ans[-1][j]
                    row.append(value)
                row.append(1)
                ans.append(row)

            return ans


"""
n: 4
i: (2, 3)
i: 2
j: (1,)
i: 3
k: (1, 2)
"""



ans = Solution().generate(4)
[print(row) for row in ans]