"""
There are 2 types of white triangles which will be red
  - Originally has at least 2 red neighbors
  - When we color white triangles, a white triangle gains at least 2 red neighbors
"""

from typing import List


class Solution:
    def colorRed(self, n: int) -> List[List[int]]:
        ans = []

        for i in range(n, 0, -1):

            # ?
            p = (n - i) % 4

            if p == 0:
                for j in range(2 * i - 1, 0, -2):
                    ans.append([i, j])

            elif p == 1:
                if 2 <= i:
                    ans.append([i, 2])

            elif p == 2:
                for j in range(2 * i - 1, 2, -2):
                    ans.append([i, j])

            elif p == 3:
                ans.append([i, 1])

            # print(f"i: {i}, p: {p}, ans: {ans}")

        # print(p)

        if 1 <= p <= 2:
            ans.append([1, 1])

        return ans[::-1]
