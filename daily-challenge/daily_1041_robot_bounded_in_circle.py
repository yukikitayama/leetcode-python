class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # North, east, south, west
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Initial position
        x = 0
        y = 0
        # Initially face north
        idx = 0

        for i in instructions:

            if i == 'L':
                idx = (idx + 3) % 4

            elif i == 'R':
                idx = (idx + 1) % 4

            else:
                x += directions[idx][0]
                y += directions[idx][1]

        return (x == 0 and y == 0) or idx != 0
