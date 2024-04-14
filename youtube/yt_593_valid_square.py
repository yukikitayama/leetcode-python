from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        points.sort()

        def compute_distance(pi, pj):
            return (pi[0] - pj[0])**2 + (pi[1] - pj[1])**2

        d01 = compute_distance(points[0], points[1])
        d02 = compute_distance(points[0], points[2])
        d13 = compute_distance(points[1], points[3])
        d23 = compute_distance(points[2], points[3])

        if d01 == 0 or d02 ==0 or d13 == 0 or d23 == 0:
            return False

        d03 = compute_distance(points[0], points[3])
        d12 = compute_distance(points[1], points[2])

        return d01 == d02 == d13 == d23 and d03 == d12
