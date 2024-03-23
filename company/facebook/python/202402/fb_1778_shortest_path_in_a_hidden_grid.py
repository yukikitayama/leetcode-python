"""
[1,2],
[-1,0]
U,R

[0,0,-1],
[1,1,1],
[2,0,0]
D,L,L,D

[-1,0],
[0,2]

BFS
  Get 4 directions
    if canMove is true

Backtracking
  Move all the way to target
  Once target is found
    backtrack and try another path all the way to target
  Every time reaching the target, update answer with minimum so far
"""

import collections


# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
# class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#
#
#    def move(self, direction: str) -> bool:
#
#
#    def isTarget(self) -> None:
#
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:

        directions = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)
        }
        back_directions = {
            "U": "D",
            "D": "U",
            "L": "R",
            "R": "L"
        }

        # Graph metadata for BFS
        # Keys will be the path that BFS can take
        valid_cell_to_is_target = {(0, 0): master.isTarget()}

        def dfs(r, c):

            for direction in directions.keys():
                offset_r, offset_c = directions[direction]
                next_r = r + offset_r
                next_c = c + offset_c

                # If this key doesn't exist, we haven't visited yet
                if (next_r, next_c) not in valid_cell_to_is_target and master.canMove(direction):
                    master.move(direction)
                    # Save graph metadata
                    valid_cell_to_is_target[(next_r, next_c)] = master.isTarget()

                    # Recursively try the next cell
                    dfs(next_r, next_c)

                    # Backtracking
                    back_direction = back_directions[direction]
                    master.move(back_direction)

        # Hypothetical start cell
        # We have no grid information, so the cell will be identified relatively to this origin
        dfs(0, 0)

        # print(valid_cell_to_is_target)

        queue = collections.deque()
        # [(r, c, step),]
        queue.append((0, 0, 0))
        visited = set()

        while queue:

            r, c, step = queue.popleft()

            if valid_cell_to_is_target[(r, c)]:
                return step

            for offset_r, offset_c in directions.values():
                next_r = r + offset_r
                next_c = c + offset_c
                if (next_r, next_c) in valid_cell_to_is_target and (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    queue.append((next_r, next_c, step + 1))

        return -1
