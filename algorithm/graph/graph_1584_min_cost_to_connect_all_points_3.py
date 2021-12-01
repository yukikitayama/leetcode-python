"""
- Prim's algorithm
"""


from typing import List
import heapq


class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    # Less than operator
    def __lt__(self, other):
        # print('Less than')
        return self.cost < other.cost


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or not len(points):
            return 0
        n = len(points)
        heap = []
        visited = [False] * n
        ans = 0
        # Count will be decremented
        count = n - 1
        # In Prim's algorithm, the vertex first chosen is arbitrary
        x1, y1 = points[0]

        for i in range(1, n):
            x2, y2 = points[i]
            cost = abs(x1 - x2) + abs(y1 - y2)
            edge = Edge(0, i, cost)
            # Min heap will work by edge class __lt__ less than operator
            # by comparing cost to have min object to the top of the min heap
            heap.append(edge)

        heapq.heapify(heap)

        visited[0] = True

        while heap and count > 0:
            edge = heapq.heappop(heap)
            point1 = edge.point1
            point2 = edge.point2
            cost = edge.cost

            if not visited[point2]:
                ans += cost
                visited[point2] = True

                # Add new edges from point2 to other unvisited vertex
                for i in range(n):
                    if not visited[i]:
                        dist = abs(points[point2][0] - points[i][0]) + abs(points[point2][1] - points[i][1])
                        heapq.heappush(heap, Edge(point2, i, dist))

                count -= 1

        return ans


if __name__ == '__main__':
    e1 = Edge(0, 1, 1)
    e2 = Edge(2, 3, 2)
    print(e1 < e2)
    print(e1 > e2)

    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    # 20
    points = [[3,12],[-2,5],[-4,1]]
    # 18
    # points = [[0,0],[1,1],[1,0],[-1,1]]
    # 4
    # points = [[-1000000,-1000000],[1000000,1000000]]
    # 4000000
    # points = [[0,0]]
    # 0
    print(Solution().minCostConnectPoints(points))

