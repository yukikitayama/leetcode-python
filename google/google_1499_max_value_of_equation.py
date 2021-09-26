from typing import List
import heapq


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # q is priority queue by using heapq max heap
        q = []
        heapq.heapify(q)
        # Answer variable is initialized to be negative infinity
        # because we wanna get the maximum value, so every time, push it up
        res = float('-inf')

        for x, y in points:

            # q[0] is maximum xi - yi, q[0][1] is the xi to give us the maximum xi - yi
            # q[0][1] < x - k finds out the xi and xj, whose absolute difference is less than or equal to k
            # Inside while loop it does heappop, so q[0][1] is a x which is not meeting the requirement.
            # Requirement is |xi - xj| <= k.
            # If the absolute is positive, xi - xj <= k -> xi <= xj + k
            # If that's negativem -xi + xj <= k -> -xi <= -xj + k -> xi >= xj - k
            # xi - xj < - k -> -xi + xj > k
            # ???
            # if q: print(f'out while, q[0][1]: {q[0][1]}, x: {x}')

            # while q and q[0][1] < x - k:
            # To me, this is more intuitive.
            # If absolute difference is bigger than k, it doesn't meet the requirement, so pop it from the heap
            while q and abs(q[0][1] - x) > k:

                # print(f'in while, q[0][1]: {q[0][1]}, x: {x}')

                heapq.heappop(q)

            if q:
                # Multiply - to q[0][0] because the value is stored as negative in heap to make it max heap
                # The below does (yi - xi) + (yj + xj)
                res = max(res, -q[0][0] + y + x)


            # We wanna find out the maximum of yi - xi, so
            # -(yi - xi) is xi - yi. So below is multiplying negative one to (yi - xi)
            # so it implements max heap by negative one
            heapq.heappush(q, (x - y, x))

        return res


"""
Time complexity
O(nlogn) because of the priority queue by heapq max heap

Space complexity
O(n) for heap
"""



points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1
print(Solution().findMaxValueOfEquation(points, k))
