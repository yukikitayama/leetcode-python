from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        # Make histogram
        for i in range(m):
            for j in range(n):
                # If current element is 1 and not at the first row
                if mat[i][j] and i > 0:
                    # Accumulate to make histogram
                    mat[i][j] += mat[i - 1][j]

        ans = 0

        # For each row
        for i in range(m):
            stack = []
            cnt = 0

            # Check heights in each column
            for j in range(n):

                # When the height goes down
                while stack and mat[i][stack[-1]] > mat[i][j]:

                    # Index of previously seen higher height than current height
                    jj = stack.pop()
                    kk = stack[-1] if stack else - 1
                    height_down = mat[i][jj] - mat[i][j]
                    curr_width = jj - kk
                    # Decrement the count accumulated so far
                    cnt -= height_down * curr_width

                    # e.g. cnt: 1, stack: [0], mat[i][stack[-1]]: 1, mat[i][j]: 0,
                    # jj: 0, kk: -1, (mat[i][jj] - mat[i][j]): 1 - 0 = 1,
                    # (jj - kk): 0 + 1 = 1, cnt: 0

                    # e.g. cnt: 2, stack: [0, 1], mat[i][stack[-1]]: 1, mat[i][j]: 0,
                    # jj: 1, kk: 0, (mat[i][jj] - mat[i][j]): 1 - 0 = 1,
                    # (jj - kk): 1 - 0 = 1, cnt: 1,
                    # stack: [0], mat[i][stack[-1]]: 1, mat[i][j]: 0,
                    # jj: 0, kk: -1, (mat[i][jj] - mat[i][j]): 1 - 0 = 1,
                    # (jj - kk): 1, cnt: 0,

                # As long as height keeps going up in iterating current row,
                # cnt keeps getting bigger by height at the current cell.
                cnt += mat[i][j]
                # Accumulated count pushes up the answer count
                ans += cnt
                stack.append(j)

        return ans


if __name__ == '__main__':
    mat = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
    print(Solution().numSubmat(mat))
