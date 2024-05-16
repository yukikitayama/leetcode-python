"""
after cleaning, in-place modify a cell to be -1 to avoid visiting again

[
    [0,0,0,1],
    [0,1,0,1],
    [1,0,0,0]
]
exp: 7
Ans
  if robot visits a cell for the second time with the same direction, a cycle has begun
"""

from typing import List


class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        cleaned = set()

        def dfs(r, c, d):

            if (r, c, d) in visited:
                return len(cleaned)

            visited.add((r, c, d))
            cleaned.add((r, c))

            next_r = r + directions[d][0]
            next_c = c + directions[d][1]

            if 0 <= next_r < len(room) and 0 <= next_c < len(room[0]) and room[next_r][next_c] == 0:
                return dfs(next_r, next_c, d)

            else:
                return dfs(r, c, (d + 1) % 4)

        return dfs(0, 0, 0)

    def numberOfCleanRooms1(self, room: List[List[int]]) -> int:

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        ans = 0

        def dfs(r, c, d):
            nonlocal ans

            ans += 1
            room[r][c] = -1

            next_r = r + directions[d][0]
            next_c = c + directions[d][1]

            if 0 <= next_r < len(room) and 0 <= next_c < len(room[0]) and room[next_r][next_c] == 0:
                dfs(next_r, next_c, d)

            elif (
                    (next_r < 0 or len(room) <= next_r or next_c < 0 or len(room[0]) <= next_c)
                    or (0 <= next_r < len(room) and 0 <= next_c < len(room[0]) and room[next_r][next_c] == 1)
            ):
                new_d = (d + 1) % 4
                next_r = r + directions[new_d][0]
                next_c = c + directions[new_d][1]
                if 0 <= next_r < len(room) and 0 <= next_c < len(room[0]) and room[next_r][next_c] == 0:
                    dfs(next_r, next_c, new_d)

                # found = False
                # i = 0
                # while not found and i < 4:
                #     new_d = (d + 1) % 4
                #     next_r = r + directions[new_d][0]
                #     next_c = c + directions[new_d][1]
                #     if 0 <= next_r < len(room) and 0 <= next_c < len(room[0]) and room[next_r][next_c] == 0:
                #         found = True

        dfs(0, 0, 0)

        return ans
