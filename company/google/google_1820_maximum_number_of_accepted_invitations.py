from typing import List


class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        ans = 0

        m = len(grid)
        n = len(grid[0])

        matching = [-1] * n

        def dfs(node, seen):
            for nei in range(n):

                # If ith girl is not invited yet
                if grid[node][nei] and not seen[nei]:
                    # Mark ith girl as invited
                    seen[nei] = True

                    if matching[nei] == -1 or dfs(matching[nei], seen):
                        matching[nei] = node
                        return True
            return False

        # Iterate guy
        for i in range(m):
            # Flag whether ith girl is already invited
            seen = [False] * n
            if dfs(i, seen):
                ans += 1

        return ans


if __name__ == '__main__':
    grid = [[1, 1, 1],
            [1, 0, 1],
            [0, 0, 1]]
    print(Solution().maximumInvitations(grid))
