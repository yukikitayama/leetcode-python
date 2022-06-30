"""
- Put from smallest boxes
- Preprocess warehouse to be a non-increasing sequence
"""


from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        # Preprocess warehouse
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i - 1], warehouse[i])

        # Sort boxes
        boxes.sort()

        # Put smallest box into rightmost warehouse
        ans = 0
        i = 0
        for height in warehouse[::-1]:
            # If warehouse width is bigger than boxes length,
            # we will use up all boxes, but we still iterating warehouse,
            # so it will be out of range
            if i < len(boxes) and boxes[i] <= height:
                i += 1
                ans += 1

        return ans


if __name__ == '__main__':
    boxes = [4, 3, 4, 1]
    warehouse = [5, 3, 3, 4, 1]
    boxes = [2, 3]
    warehouse = [6, 5, 5, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    boxes = [1, 2, 3]
    warehouse = [2, 1]
    print(Solution().maxBoxesInWarehouse(boxes, warehouse))
