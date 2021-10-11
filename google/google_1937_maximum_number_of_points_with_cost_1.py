"""
- bottom up dp
- start from the first row and go down
- make 2d dp
- return the max of the last row of dp matrix

- left[1] = max(pre[1], left[0] - 1)
- left[2] = max(pre[2], left[1] - 1)
- No need to add left[0] - 2 to left[2] because
  - left[1] is the result of max(pre[1], left[0] - 1)
"""


from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        # If there's only one row, just get the max
        if m == 1:
            return max(points[0])
        # If there's only one column, just sum all the rows
        if n == 1:
            return sum(sum(row) for row in points)

        def left(arr):
            lft = [arr[0]] + [0] * (n - 1)
            for i in range(1, n):
                lft[i] = max(lft[i - 1] - 1, arr[i])
            return lft

        def right(arr):
            rgt = [0] * (n - 1) + [arr[-1]]
            for i in range(n - 2, -1, -1):
                rgt[i] = max(rgt[i + 1] - 1, arr[i])
            return rgt

        pre = points[0]
        for i in range(1, m):
        # for i in range(m - 1):
            lft = left(pre)
            rgt = right(pre)
            cur = [0] * n

            for j in range(n):
                cur[j] = points[i][j] + max(lft[j], rgt[j])
                # cur[j] = points[i + 1][j] + max(lft[j], rgt[j])

            pre = cur
            # pre = cur[:]

        return max(pre)


points = [[1,2,3],[1,5,1],[3,1,1]]
print(Solution().maxPoints(points))
