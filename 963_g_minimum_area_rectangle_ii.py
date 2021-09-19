from typing import List
from collections import defaultdict
import pprint


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:

        # Find two pairs of points which share the same distance between points and midpoint
        # It means that 2 diagonal of a rectangle crosses, so it can shape rectangle
        # If the length of the list in the value in the dictionary is 1, it cannot find a point to form a rectangle
        # Key: (distance, midpoint), Value: [(point1, point2), (point3, point4), ...]
        diagonal_and_midpoints = defaultdict(list)

        for point1, point2 in self.generate_distinct_pairs(points):
            diagonal = self.get_distance(point1, point2)
            midpoint = self.get_midpoint(point1, point2)
            # This is same as defaultdict_object[diagonal, midpoint].append(something)
            diagonal_and_midpoints[(diagonal, midpoint)].append((point1, point2))

        # pprint.pprint(diagonal_and_midpoints)

        ans = float('inf')

        for pairs in diagonal_and_midpoints.values():

            # print(f'pairs: {pairs}, len(pairs): {len(pairs)}')

            for pair1, pair2 in self.generate_distinct_pairs(pairs):

                # print(f'pair1: {pair1}, pair2: {pair2}')

                curr_area = self.get_area(pair1, pair2)

                # print(f'curr_area: {curr_area}')

                ans = min(ans, curr_area)

        return 0 if ans == float('inf') else ans

    def generate_distinct_pairs(self, items):
        # It's distinct because i+1
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                # Yield to come back
                yield items[i], items[j]

    def get_distance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        # Get slope length by Pythagorean Theorem
        # **0.5 for square root
        length = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return length

    def get_midpoint(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        x_mid = (x1 + x2) / 2
        y_mid = (y1 + y2) / 2
        return x_mid, y_mid

    def get_area(self, pair1, pair2):
        (point1, _) = pair1
        (point3, point4) = pair2
        area = self.get_distance(point1, point3) * self.get_distance(point1, point4)
        return area


# points = [[1, 2], [2, 1], [1, 0], [0, 1]]
# points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
# points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
points = [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
print(Solution().minAreaFreeRect(points))
