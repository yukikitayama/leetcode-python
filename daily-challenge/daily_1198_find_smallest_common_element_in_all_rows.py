from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        counter = [0 for _ in range(10 ** 4 + 1)]

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                counter[mat[r][c]] += 1

        for i in range(1, len(counter)):
            if counter[i] == len(mat):
                return i

        return -1


if __name__ == '__main__':
    mat = [[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]
    print(Solution().smallestCommonElement(mat))
