from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        row_ones = [0] * len(mat)
        col_ones = [0] * len(mat[0])

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    row_ones[r] += 1
                    col_ones[c] += 1

        ans = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1 and row_ones[r] == 1 and col_ones[c] == 1:
                    ans += 1
        return ans


if __name__ == "__main__":
    mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
    mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(Solution().numSpecial(mat))

