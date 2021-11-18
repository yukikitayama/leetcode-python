"""
- BFS from each gate
  - Update distance by distance = min(distance, curr distance)
- Iterate each row and col to append all the gate cells to queue
  - BFS

- Time is O(mn)
  - Because one it visits a room, set is as visited, so each room is visited at most once
  - Time does not depend on how many gates there are
"""


from typing import List
import collections


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m = len(rooms)
        n = len(rooms[0])
        queue = collections.deque()
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()
            for offset_row, offset_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_row = row + offset_row
                next_col = col + offset_col

                if 0 <= next_row < m and 0 <= next_col < n and rooms[next_row][next_col] == 2147483647:
                    # A gate cell in rooms has 0, so starting from there plus 1 can get distance
                    # to each empty cell
                    rooms[next_row][next_col] = rooms[row][col] + 1
                    queue.append((next_row, next_col))

        # [print(row) for row in rooms]


rooms = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]
]
print(Solution().wallsAndGates(rooms))
