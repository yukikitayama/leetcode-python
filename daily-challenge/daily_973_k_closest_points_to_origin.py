"""
Result
- Time: 14m
- Solved: 1
- Saw solution: 0
- Optimized: 0

- Iterate points
  - Calculate euclidean distance
- Heap

"""


from typing import List
import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quick_select(points, k)

    def quick_select(self, points, k):
        left, right = 0, len(points) - 1
        pivot_index = len(points)
        while pivot_index != k:
            pivot_index = self.partition(points, left, right)
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1
        return points[:k]

    def partition(self, points, left, right):
        # point in the middle
        pivot = self.choose_pivot(points, left, right)
        pivot_dist = self.squared_distance(pivot)
        while left < right:
            if self.squared_distance(points[left]) >= pivot_dist:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1
        if self.squared_distance(points[left]) < pivot_dist:
            left += 1

        return left

    def choose_pivot(self, points, left, right):
        return points[left + (right - left) // 2]

    def squared_distance(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] ** 2


class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        def euclidean_distance(p):
            return math.sqrt((p[0] - 0)**2 + (p[1] - 0)**2)

        for point in points:
            dist = euclidean_distance(point)

            # print(f'  point: {point}, dist: {dist}')

            if len(max_heap) == k:
                if -max_heap[0][0] > dist:
                    heapq.heappop(max_heap)
                else:
                    continue

            heapq.heappush(max_heap, (-dist, point[0], point[1]))

        ans = [[item[1], item[2]] for item in max_heap]

        return ans


points = [[1,3],[-2,2]]
k = 1
# [[-2, 2]]
points = [[3,3],[5,-1],[-2,4]]
k = 2
# [[3, 3], [-2, 4]]
print(Solution().KClosest(points, k))
