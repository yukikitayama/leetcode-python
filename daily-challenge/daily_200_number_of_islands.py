from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()

        def recursion(r, c):

            seen.add((r, c))

            for r_offset, c_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r_next = r + r_offset
                c_next = c + c_offset

                if 0 <= r_next < len(grid) and 0 <= c_next < len(grid[0]) and grid[r_next][c_next] == '1':
                    if (r_next, c_next) not in seen:
                        grid[r_next][c_next] = '0'
                        recursion(r_next, c_next)

        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':

                    recursion(r, c)
                    ans += 1

        return ans


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(Solution().numIslands(grid))
