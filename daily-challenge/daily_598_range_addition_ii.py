from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # When there's no operation
        if len(ops) == 0:
            return m * n

        # Minimum of x and y in operations is the lower right corner which experienced max operation intersections
        xs, ys = [], []
        for op in ops:
            xs.append(op[0])
            ys.append(op[1])
        x = min(xs)
        y = min(ys)
        # Calculating area gives us the count of max numbers in the intersection
        return x * y


m = 3
n = 3
# ops = [[2,2],[3,3]]
# ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
ops = []
print(Solution().maxCount(m, n, ops))