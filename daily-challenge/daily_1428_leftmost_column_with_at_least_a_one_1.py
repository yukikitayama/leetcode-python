from typing import List
import bisect


class BinaryMatrix:
    def get(self, row: int, col: int) -> int:
        return 0

    def dimensions(self) -> List[int]:
        return [0, 0]


class Solution:
    def leftMostColumnWithOne(self, mat: List[List[int]]) -> int:

        [print(row) for row in mat]

        ans = float('inf')

        for row in mat:
            index = bisect.bisect_left(row, 1)

            ans = min(ans, index)

            # print(f'index: {index}')

        return ans if ans != float('inf') else -1


mat = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1]
]
print(Solution().leftMostColumnWithOne(mat))
