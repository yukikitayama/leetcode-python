from typing import List
import bisect


class BinaryMatrix:
    def get(self, row: int, col: int) -> int:
        return 0

    def dimensions(self) -> List[int]:
        return [0, 0]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        current_row = 0
        current_col = cols - 1

        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1

        return current_col + 1 if current_col != cols - 1 else -1

mat = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1]
]
