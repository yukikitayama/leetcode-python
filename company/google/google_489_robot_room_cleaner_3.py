class Solution:
    def cleanRoom(self, robot):

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell=(0, 0), d=0):
            visited.add(cell)
            robot.clean()

            for i in range(4):
                # new_d from 0 to 3
                new_d = (d + i) % 4
                new_cell = (
                    cell[0] + directions[new_d][0],
                    cell[1] + directions[new_d][1]
                )

                # The below robot.move() works in for loop to try all the four directions,
                # because at the end of the for loop, robot changes the direction to do move() at the next iteration
                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()

                # Need to turn right because in the above if statement, we do robot.move() clean the cell that
                # the robot currently faces. So in for loop, when we iterate all the 4 directions, we need to turn the
                # robot as well
                robot.turnRight()


        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()
