from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[1], p[0]))

        curr_end = points[0][1]
        ans = 1

        for i in range(1, len(points)):

            if points[i][0] <= curr_end:
                continue

            else:
                ans += 1
                curr_end = points[i][1]

        return ans

    def findMinArrowShots1(self, points: List[List[int]]) -> int:
        points.sort()

        # print(points)

        stack = []

        for i in range(len(points)):

            if stack and points[i][0] <= stack[-1][1]:
                stack[-1][0] = max(stack[-1][0], points[i][0])
                stack[-1][1] = min(stack[-1][1], points[i][1])

            else:
                stack.append(points[i])

            # print(stack)

        return len(stack)
