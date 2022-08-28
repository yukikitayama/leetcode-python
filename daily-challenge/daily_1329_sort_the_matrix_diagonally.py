from typing import List
import collections
import heapq
import pprint


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        # Extract diagonal as list
        diagonals = collections.defaultdict(list)
        for row in range(m):
            for col in range(n):
                # diagonal shares row - col as index
                i = row - col
                diagonals[i].append(mat[row][col])

        # pprint.pprint(diagonals)

        # Not diagonals: because it's dictionary, so if in diagonals:, keys are iterated,
        # but we wanna iterate lists which are values of the dictionary
        # The dictionary will have heaps in each key, so it's sorted as min heap
        for diagonal in diagonals.values():
            heapq.heapify(diagonal)

        # pprint.pprint(diagonals)

        for row in range(m):
            for col in range(n):
                # Extract a value by min heap order
                value = heapq.heappop(diagonals[row - col])
                mat[row][col] = value

        return mat


if __name__ == '__main__':
    mat = [
        [3, 3, 1, 1],
        [2, 2, 1, 2],
        [1, 1, 1, 2]
    ]
    ans = Solution().diagonalSort(mat)
    for row in ans:
        print(row)

