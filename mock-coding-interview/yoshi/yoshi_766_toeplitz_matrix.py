from typing import List
import collections


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0 or c == 0:
                    continue
                else:
                    if matrix[r - 1][c - 1] != matrix[r][c]:
                        return False

        return True

    def isToeplitzMatrix1(self, matrix: List[List[int]]) -> bool:
        key_to_val = collections.defaultdict(int)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                k = r - c

                if k not in key_to_val:
                    key_to_val[k] = matrix[r][c]

                else:
                    if key_to_val[k] != matrix[r][c]:
                        return False

        return True
