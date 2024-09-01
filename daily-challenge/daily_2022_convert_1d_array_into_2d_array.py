from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        ans = [[0] * n for _ in range(m)]

        for i in range(len(original)):
            r, c = divmod(i, n)

            ans[r][c] = original[i]

        return ans

    def construct2DArray1(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if len(original) != m * n:
            return []

        ans = []
        c = 0
        curr = []

        for i in range(len(original)):

            curr.append(original[i])
            c += 1

            if c == n:
                ans.append(curr[:])
                c = 0
                curr = []

        return ans