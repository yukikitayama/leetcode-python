from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ans = []

        for i in range(numRows):
            curr = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    curr.append(1)
                else:
                    num = ans[-1][j - 1] + ans[-1][j]
                    curr.append(num)
            ans.append(curr)

        return ans
