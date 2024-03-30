"""
save coordinates to hashset
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coordinates = set()
        curr_x = 0
        curr_y = 0
        coordinates.add((curr_x, curr_y))

        offsets = {
            "N": [-1, 0],
            "E": [0, 1],
            "S": [1, 0],
            "W": [0, -1]
        }

        for i in range(len(path)):

            offset_x, offset_y = offsets[path[i]]
            next_x = curr_x + offset_x
            next_y = curr_y + offset_y

            if (next_x, next_y) in coordinates:
                return True

            coordinates.add((next_x, next_y))
            curr_x = next_x
            curr_y = next_y

        return False
