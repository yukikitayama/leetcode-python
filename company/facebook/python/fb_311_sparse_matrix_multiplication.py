"""
- Intentionally do not follow the way of dot product
- Instead create layers of matrices to sum up
- Optimize for sparse matrix
"""


from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        # Row-wise iteration
        for r, mat1_row in enumerate(mat1):

            # Column-wise iteration because mat1_row is a row, so iterate to columns
            for e, mat1_row_val in enumerate(mat1_row):

                # If mat1 value is 0, no iteration because it won't add anything
                if mat1_row_val:

                    # Column-wise iteration because mat2[e] selects one row so iterate to columns in the row
                    for c, mat2_col_val in enumerate(mat2[e]):

                        # Matrix multiplication by layers
                        ans[r][c] += mat1_row_val * mat2_col_val

        return ans


if __name__ == '__main__':
    mat1 = [[1, 0, 0], [-1, 0, 3]]
    mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    print(Solution().multiply(mat1, mat2))
