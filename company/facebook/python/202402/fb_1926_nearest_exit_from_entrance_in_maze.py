"""
BFS
  visited set to avoid visiting again
  steps starts with 0
  terminate
    when queue is empty
    or current cell is at the border
      border: r is 0, r is n - 1, c is 0 or c is m - 1
      return steps
return -1
"""

from typing import List
import collections


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        visited.add((entrance[0], entrance[1]))
        steps = 0
        queue = collections.deque()
        queue.append(entrance)

        while queue:

            # print(steps, queue)

            for _ in range(len(queue)):

                curr_r, curr_c = queue.popleft()

                if (curr_r, curr_c) != (entrance[0], entrance[1]):
                    if curr_r == 0 or curr_r == len(maze) - 1 or curr_c == 0 or curr_c == len(maze[0]) - 1:
                        return steps

                for offset_r, offset_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    next_r = curr_r + offset_r
                    next_c = curr_c + offset_c
                    # print(next_r, next_c)

                    if 0 <= next_r < len(maze) and 0 <= next_c < len(maze[0]) and maze[next_r][next_c] == "." and (
                    next_r, next_c) not in visited:
                        visited.add((next_r, next_c))
                        queue.append([next_r, next_c])

            steps += 1

            # print(steps, queue)

        return -1