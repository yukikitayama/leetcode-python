"""
Idea
- DFS
- We don't know how the next cell looks like, but if it stays the same cell,
  we can know that the cell at the front is out of boundary or wall
- When it fits the boundary or wall, do turnRight() twice to come back to the
  cells it already visited until it finds the neighbors which are not visited yet.

Algorithm
-
"""


class Solution:
    def cleanRoom(self, robot):

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        # cell=(0, 0) because we use relative positions
        # We add relative positions of the random original cell to the visited set
        # d=0 because robot is originally faced up.
        def backtrack(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()

            for i in range(4):
                # Based on the previous direction, the next direction is the next right handside
                new_d = (d + i) % 4

                # All the positions are relative positions to the random original cell
                # so new cell could contain negative x and y values
                new_cell = (
                    cell[0] + directions[new_d][0],
                    cell[1] + directions[new_d][1]
                )

                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()

                robot.turnRight()

        # Directions traverses as top, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()

