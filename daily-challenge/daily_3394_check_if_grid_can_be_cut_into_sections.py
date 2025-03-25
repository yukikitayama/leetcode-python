from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        def check_cuts(dim):
            res = 0

            # dim: 0, sort by bottom left x
            # dim: 1, sort by bottom left y
            rectangles.sort(key=lambda x: x[dim])
            # dim(0) + 2: top right x
            # dim(1) + 2: top right y
            furthest_end = rectangles[0][dim + 2]
            for i in range(1, len(rectangles)):
                if furthest_end <= rectangles[i][dim]:
                    res += 1
                furthest_end = max(furthest_end, rectangles[i][dim + 2])

            return res >= 2

        return check_cuts(0) or check_cuts(1)
