"""
- If the robot returns to the initial point after one cycle, it's the limit cycle trajectory
- If at the end of one cycle the robot does not face the north, it's the limit cycle trajectory
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # direction: [x, y]
        # Initially x: 0, y: 0, going up means x: 0, y: 1,
        # so it adds 1 to y, so [0, 1],
        # different from usual direction in 2d matrix
        # Go up, right, down, left
        directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]

        # Initial position
        x = y = 0

        # Initially facing north
        idx = 0

        for char in instructions:
            if char == 'L':
                # If currently north, incrementing idx by 3 lets us be left
                idx = (idx + 3) % 4
            elif char == 'R':
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]

        return (x == 0 and y == 0) or idx != 0


"""
- Let n be the length of instructions
- Time is O(n) for the for loop
- Space is O(1)
"""


instructions = "GGLLGG"
instructions = "GG"
print(Solution().isRobotBounded(instructions))
