class Solution:
    def isPathCrossing(self, path: str) -> bool:

        curr = (0, 0)
        locations = set([(curr)])

        for direction in path:

            curr_x, curr_y = curr

            if direction == "N":
                curr_y += 1

            elif direction == "E":
                curr_x += 1

            elif direction == "S":
                curr_y -= 1

            elif direction == "W":
                curr_x -= 1

            if (curr_x, curr_y) in locations:
                return True

            curr = curr_x, curr_y

            locations.add(curr)

        return False


if __name__ == "__main__":
    path = "NES"
    path = "NESWW"
    # path = "SS"
    print(Solution().isPathCrossing(path))

