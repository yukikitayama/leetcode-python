from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        curr_r = rStart
        curr_c = cStart
        ans.append([curr_r, curr_c])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        curr_unit = 1

        while len(ans) < (rows * cols):

            for _ in range(2):

                for _ in range(curr_unit):
                    offset_r, offset_c = directions[dir_idx]
                    curr_r += offset_r
                    curr_c += offset_c
                    if 0 <= curr_r < rows and 0 <= curr_c < cols:
                        ans.append([curr_r, curr_c])

                dir_idx += 1
                dir_idx %= 4

            curr_unit += 1

        return ans

    def spiralMatrixIII1(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        curr_r = rStart
        curr_c = cStart
        ans.append([curr_r, curr_c])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        curr_unit = 1

        while len(ans) < (rows * cols):

            for _ in range(curr_unit):
                offset_r, offset_c = directions[dir_idx]
                curr_r += offset_r
                curr_c += offset_c
                if 0 <= curr_r < rows and 0 <= curr_c < cols:
                    ans.append([curr_r, curr_c])

            dir_idx += 1
            dir_idx %= 4

            for _ in range(curr_unit):
                offset_r, offset_c = directions[dir_idx]
                curr_r += offset_r
                curr_c += offset_c
                if 0 <= curr_r < rows and 0 <= curr_c < cols:
                    ans.append([curr_r, curr_c])

            dir_idx += 1
            dir_idx %= 4

            curr_unit += 1

        return ans