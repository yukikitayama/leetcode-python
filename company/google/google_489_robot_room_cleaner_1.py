class Solution:
    def cleanRoom(self, robot):

        def go_back():
            # Rotate 180 degree
            robot.turnRight()
            robot.turnRight()
            # Go back
            robot.move()
            # Turn the face back to the same direction,
            # to allow the robot to try the next right direction
            robot.turnRight()
            robot.turnRight()

        # cell=(0, 0)?
        # d=0 because initially robot direction faces up
        def backtrack(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()

            for i in range(4):

                # Even if any direction comes to backtrack(),
                # it can always try clockwise, and it bounds from 0 to 3
                new_d = (d + i) % 4
                new_cell = (
                    cell[0] + directions[new_d][0],
                    cell[1] + directions[new_d][1]
                )

                # If it has not visited new_cell and roboto.move() returns True meaning can move
                # Recursively visit the new cell
                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_d)

                    # When it gets out of backtrack(), it all the directions are obstacles or visited,
                    # so it needs to go back and find another empty cell we have skipped and have not visited
                    go_back()

                # The nex direction is where 1. we have already visited, or 2. obstacle
                # so turn right to find another empty space
                robot.turnRight()

        # up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()


"""
Time complexity
Let n be the number of cells in grid, and m be the number of obstacle
O(n - m) because it will visit all the empty cell but cannot visit if it's obstacle

Space complexity
O(n - m) to store visited set
"""
