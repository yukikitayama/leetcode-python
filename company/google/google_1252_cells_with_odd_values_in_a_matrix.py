from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        odd_rows = [False] * m
        odd_cols = [False] * n

        for r, c in indices:
            odd_rows[r] ^= True
            odd_cols[c] ^= True

        ans = 0
        for row in odd_rows:
            for col in odd_cols:
                # print(f'row: {row}, col: {col}')
                ans += row ^ col
        return ans


if __name__ == '__main__':
    m = 2
    n = 3
    indices = [[0, 1], [1, 1]]
    # 6
    print(Solution().oddCells(m, n, indices))
