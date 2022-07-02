"""
- After applying horizontal cut, we will know the biggest height
- After applying vertical cut, we will know the biggest width
- Return max height * max width
"""


from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        max_height = 0
        # Edge case
        max_height = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            max_height = max(max_height, horizontalCuts[i] - horizontalCuts[i - 1])

        max_width = 0
        # Edge case
        max_width = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(len(verticalCuts)):
            max_width = max(max_width, verticalCuts[i] - verticalCuts[i - 1])

        # print(max_height, max_width)

        return max_height * max_width % (10**9 + 7)


if __name__ == '__main__':
    h = 5
    w = 4
    horizontalCuts = [1, 2, 4]
    verticalCuts = [1, 3]
    h = 5
    w = 4
    horizontalCuts = [3, 1]
    verticalCuts = [1]

    print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))
