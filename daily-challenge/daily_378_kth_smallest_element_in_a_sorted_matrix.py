from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        min_heap = []
        for r in range(min(k, n)):
            min_heap.append((matrix[r][0], r, 0))
        heapq.heapify(min_heap)

        while k:
            value, r, c = heapq.heappop(min_heap)
            # n - 1 because matrix is square in this problem
            if c < (n - 1):
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
            k -= 1

        return value


if __name__ == '__main__':
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(Solution().kthSmallest(matrix, k))
