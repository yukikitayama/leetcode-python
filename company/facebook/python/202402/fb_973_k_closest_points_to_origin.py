"""
iterate points
  compute each distance
sort
Return the first k points

T: N(NlogN)
S: O(N)
"""

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # def distance_to_origin(p):
        #     return (p[0] ** 2 + p[1] ** 2 ) ** (1 / 2)

        # distances = []
        # for i in range(len(points)):
        #     d = distance_to_origin(points[i])
        #     distances.append((d, i))

        # distances.sort()

        # ans = []

        # for i in range(k):
        #     idx = distances[i][1]
        #     ans.append(points[idx])

        # return ans

        points.sort(key=lambda p: (p[0] ** 2 + p[1] ** 2))

        return points[:k]