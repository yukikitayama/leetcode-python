"""
- The approach which takes advantage of the given x and y which is a coordinate of black pixels
- and all the black pixels are connected
- use DFS to traverse all the black pixels, and each time update four corners
"""


from typing import List


class Solution:
    def __init__(self):
        self.left = None
        self.right = None
        self.top = None
        self.bottom = None

    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        self.left = y
        self.right = y
        self.top = x
        self.bottom = x
        self.dfs(image, x, y)
        return (self.right - self.left) * (self.bottom - self.top)

    def dfs(self, image, x, y):
        # If out of boundary or it's not a black pixel, stop DFS
        if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] == '0':
            return

        # DSF needs to keep track of visited cells
        # Instead of using visited set, modify the input matrix from 1 to 0 to avoid visiting
        # again by the above if statement
        image[x][y] = '0'
        self.left = min(self.left, y)
        self.right = max(self.right, y + 1)
        self.top = min(self.top, x)
        self.bottom = max(self.bottom, x + 1)
        self.dfs(image, x, y - 1)
        self.dfs(image, x, y + 1)
        self.dfs(image, x - 1, y)
        self.dfs(image, x + 1, y)


image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]]
x = 0
y = 2
print(Solution().minArea(image, x, y))







