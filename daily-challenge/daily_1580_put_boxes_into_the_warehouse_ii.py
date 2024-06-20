from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)
        i = 0

        ans = 0

        left = 0
        right = len(warehouse) - 1

        while left <= right and i < len(boxes):

            if boxes[i] <= warehouse[left]:
                left += 1
                i += 1
                ans += 1

            elif boxes[i] <= warehouse[right]:
                right -= 1
                i += 1
                ans += 1

            # Explore smaller boxes without changing left and right
            else:
                i += 1

        return ans

    def maxBoxesInWarehouse1(self, boxes: List[int], warehouse: List[int]) -> int:
        heights = [0] * len(warehouse)

        min_so_far = float("inf")
        for i in range(len(warehouse)):
            min_so_far = min(min_so_far, warehouse[i])
            heights[i] = min_so_far

        # print(heights)

        min_so_far = float("inf")
        for i in range(len(warehouse) - 1, -1, -1):
            min_so_far = min(min_so_far, warehouse[i])
            # Max allows us to find higher height if try from a different side
            heights[i] = max(heights[i], min_so_far)

        # print(heights)

        boxes.sort()
        heights.sort()
        p_box = 0
        for p_height in range(len(heights)):
            if p_box < len(boxes) and boxes[p_box] <= heights[p_height]:
                p_box += 1
        return p_box