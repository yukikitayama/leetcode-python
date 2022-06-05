"""
    0   1   2
0       -1
1           -1
2

"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0

        def backtracking(row: int, cols: set, diags: set, anti_diags: set) -> None:

            nonlocal ans

            if row >= n:
                ans += 1
                return

            for col in range(n):
                diag = row - col
                anti_diag = row + col

                if col in cols or diag in diags or anti_diag in anti_diags:
                    continue

                cols.add(col)
                diags.add(diag)
                anti_diags.add(anti_diag)

                backtracking(row + 1, cols, diags, anti_diags)

                cols.remove(col)
                diags.remove(diag)
                anti_diags.remove(anti_diag)

        backtracking(0, set(), set(), set())

        return ans


if __name__ == '__main__':
    n = 4
    # 2
    n = 1
    # 1
    print(Solution().totalNQueens(n))
