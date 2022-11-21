"""
- BFS
"""


from typing import List
import collections


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        queue = collections.deque()
        queue.append((entrance[0], entrance[1], 0))
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:

            curr_r, curr_c, step = queue.popleft()

            if (
                (curr_r == 0 or curr_r == len(maze) - 1 or curr_c == 0 or curr_c == len(maze[0]) - 1)
                and step != 0
            ):
                return step

            for offset_r, offset_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                next_r = curr_r + offset_r
                next_c = curr_c + offset_c

                if 0 <= next_r < len(maze) and 0 <= next_c < len(maze[0]) and maze[next_r][next_c] == '.':

                    if (next_r, next_c) not in visited:

                        queue.append((next_r, next_c, step + 1))
                        visited.add((next_r, next_c))

        return -1


if __name__ == '__main__':
    maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
    entrance = [1, 2]
    maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    entrance = [1, 0]
    maze = [[".", "+"]]
    entrance = [0, 0]
    maze = [
        ["+", ".", "+", "+", "+", "+", "+"],
        ["+", ".", "+", ".", ".", ".", "+"],
        ["+", ".", "+", ".", "+", ".", "+"],
        ["+", ".", ".", ".", "+", ".", "+"],
        ["+", "+", "+", "+", "+", ".", "+"]
    ]
    entrance = [0, 1]
    # 12
    print(Solution().nearestExit(maze, entrance))
