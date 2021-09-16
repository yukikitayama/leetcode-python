from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        # Sort by ascending x, if x are the same, sort by ascending y
        points.sort(key=lambda x: (x[0], x[1]))

        # print(f'points: {points}')

        # Need self.dist(points[0], points[1]) != 0 to avoid p1: [0, 0], p2: [0, 0], p3: [0, 0], p4: [0, 0]
        return self.dist(points[0], points[1]) != 0 \
               and self.dist(points[0], points[1]) == self.dist(points[1], points[3]) \
               and self.dist(points[1], points[3]) == self.dist(points[3], points[2]) \
               and self.dist(points[3], points[2]) == self.dist(points[2], points[0]) \
               and self.dist(points[0], points[3]) == self.dist(points[1], points[2])

    def dist(self, p1: List[int], p2: List[int]) -> float:

        # Use Pythagorean theorem, a * a + b * b = c * c
        return (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2



p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]
print(Solution().validSquare(p1, p2, p3, p4))
print(Solution().dist(p1, p4))
