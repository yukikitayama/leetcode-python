"""
Starts
Hashset
Iterate row += 1 col += 1
"""

from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # n = len(matrix)
        # m = len(matrix[0])

        # starts = []
        # for r in range(n - 1, -1, -1):
        #     starts.append((r, 0))
        # for c in range(1, m):
        #     starts.append((0, c))

        # for r, c in starts:
        #     curr = set()
        #     while 0 <= r < n and 0 <= c < m:
        #         curr.add(matrix[r][c])
        #         if len(curr) > 1:
        #             return False
        #         r += 1
        #         c += 1

        # return True

        hash_to_val = collections.defaultdict(int)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                hash_ = r - c
                if hash_ not in hash_to_val:
                    hash_to_val[hash_] = matrix[r][c]
                else:
                    if hash_to_val[hash_] != matrix[r][c]:
                        return False
        return True


