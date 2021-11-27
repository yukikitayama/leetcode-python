"""
- Iterate each row and col
  - if the current cell is 0, skip
  - if not
    - BFS
      - It returns the distance from the start cell to the nearest 0 cell

- "But hey, this could be optimized if we start the BFS from 0s
  and thereby, updating the distances of all the 1s in the path."

- Time is O(mn) because queue is added only if the calculated distance is smaller than
  recorded distance, so it won't be added multiple times
"""


from typing import List
import collections


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        if rows == 0:
            return mat

        cols = len(mat[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        queue = collections.deque()
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    dist[row][col] = 0
                    queue.append((row, col))

        # [print(row) for row in dist]

        dir = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ]

        while queue:
            curr = queue.popleft()

            for i in range(4):
                new_r = curr[0] + dir[i][0]
                new_c = curr[1] + dir[i][1]

                if 0 <= new_r < rows and 0 <= new_c < cols:
                    # If the distance from current cell to the next is smaller than currently recorded minimum distance,
                    # Update it
                    if dist[curr[0]][curr[1]] + 1 < dist[new_r][new_c]:
                        dist[new_r][new_c] = dist[curr[0]][curr[1]] + 1
                        queue.append((new_r, new_c))

        return dist


"""
- Time is O(mn) to initialize dist matrix and add cells to queue,
  and 
"""


mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
ans = Solution().updateMatrix(mat)
[print(row) for row in ans]

