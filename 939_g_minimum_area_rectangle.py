from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # To start with lower left (smallest x and smallest y), first sort points in an ascending order
        # Python list sort() of list of lists sorts by the first element of each inner list
        points.sort()
        # print(points)
        points_set = set(tuple(point) for point in points)
        # print(points_set)
        smallest_area = float('inf')

        # Lower left
        for i, (x1, y1) in enumerate(points):

            # Upper right
            # enumerate(iterable, start=0)
            for j, (x2, y2) in enumerate(points[i:], i):

                # x1 < x2: left and right condition
                # y1 < y2: lower and upper condition
                # (x1, y2): upper left, (x1, y2) in points_set checks if it has a point to form a valid rectangle
                # (x2, y1): lower right, (x2, y1) in points_set checks if it has a point to form a valid rectangle
                if x1 < x2 and y1 < y2 and (x1, y2) in points_set and (x2, y1) in points_set:
                    current_area = (x2 - x1) * (y2 - y1)
                    smallest_area = min(smallest_area, current_area)

        # If smallest_area is still float('inf') here, it means that
        # it couldn't find a valid rectangle, so return 0
        return smallest_area if smallest_area != float('inf') else 0


"""
Time complexity
Let n be the length of points list,
O(nlogn) to sort points, and O(n**2) for nested for loops iteration
So O(nlogn + n**2) = O(n**2)

Space complexity
O(n) for set and list
"""


points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
print(Solution().minAreaRect(points))
