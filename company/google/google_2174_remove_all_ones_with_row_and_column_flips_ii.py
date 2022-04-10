"""
- Backtracking
"""


from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = float('inf')
        flips = 0
        seen = set()

        def backtracking():

            nonlocal flips
            nonlocal ans

            flag = False

            for x in range(m):
                for y in range(n):
                    if grid[x][y] == 1 and ('r', x) not in seen and ('c', y) not in seen:
                        flag = True
                        seen.add(('r', x))
                        seen.add(('c', y))

                        flips += 1

                        backtracking()

                        # Backtrack
                        flips -= 1
                        seen.remove(('r', x))
                        seen.remove(('c', y))

            # If flag stays False, it means no flips occurred
            # It also means that the grid are all 0ed already
            if not flag:
                ans = min(ans, flips)

        backtracking()

        return ans


if __name__ == '__main__':
    grid = [[1, 1, 1], [1, 1, 1], [0, 1, 0]]
    print(Solution().removeOnes(grid))
