"""
- brute force to keep track of four corners of a rectangle to get an area
- left and top are inclusive
- right and bottom are exclusive
"""


from typing import List


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        left = y
        right = y
        top = x
        bottom = x
        for row in range(len(image)):
            for col in range(len(image[0])):
                if image[row][col] == '1':
                    left = min(left, col)
                    right = max(right, col + 1)
                    top = min(top, row)
                    bottom = max(bottom, row + 1)

        return (right - left) * (bottom - top)


image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]]
x = 0
y = 2
print(Solution().minArea(image, x, y))







