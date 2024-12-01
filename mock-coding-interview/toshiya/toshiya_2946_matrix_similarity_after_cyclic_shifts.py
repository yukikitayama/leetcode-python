from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        copy = []

        for m in range(len(mat)):
            row = [0] * len(mat[0])
            for n in range(len(mat[0])):
                if m % 2 == 0:
                    # n: 0, k: 4, n - k: -4, -4 % 4
                    i = (n - k) % len(mat[0])
                    row[i] = mat[m][n]
                elif m % 2 != 0:
                    i = (n + k) % len(mat[0])
                    row[i] = mat[m][n]
            copy.append(row[:])

        for m in range(len(mat)):
            for n in range(len(mat[0])):
                if mat[m][n] != copy[m][n]:
                    return False
        return True