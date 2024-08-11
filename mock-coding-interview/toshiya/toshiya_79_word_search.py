"""
DFS(r, c, i)
dirs: [(0, 1), (0, -1), (), ()]

"ABCESEEEFS"
[
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]]
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ans = False

        def dfs(r, c, i, visited):
            nonlocal ans

            if i == len(word):
                ans = True
                return

            for offset_r, offset_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nei_r = r + offset_r
                nei_c = c + offset_c
                if 0 <= nei_r < len(board) and 0 <= nei_c < len(board[0]):
                    if (nei_r, nei_c) not in visited and board[nei_r][nei_c] == word[i]:
                        visited.add((nei_r, nei_c))
                        dfs(nei_r, nei_c, i + 1, visited)
                        # Backtrack
                        visited.discard((nei_r, nei_c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    vis = set()
                    vis.add((r, c))
                    dfs(r, c, 1, vis)

        return ans
