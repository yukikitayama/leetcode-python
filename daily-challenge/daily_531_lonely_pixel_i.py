from typing import List


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row_count = [0] * len(picture)
        col_count = [0] * len(picture[0])

        for row in range(len(picture)):
            for col in range(len(picture[0])):
                if picture[row][col] == 'B':
                    row_count[row] += 1
                    col_count[col] += 1

        ans = 0

        for row in range(len(picture)):
            for col in range(len(picture[0])):
                if picture[row][col] == 'B' and row_count[row] == 1 and col_count[col] == 1:
                    ans += 1

        return ans


if __name__ == '__main__':
    picture = [["W", "W", "B"], ["W", "B", "W"], ["B", "W", "W"]]
    picture = [["B", "B", "B"], ["B", "B", "W"], ["B", "B", "B"]]
    print(Solution().findLonelyPixel(picture))
