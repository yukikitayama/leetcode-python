"""
- dfs starting from (sr, sc)
  - Record the value of the starting cell
  - modify input matrix with newColor integer
  - visiting the next cell as long as it is the same value as the starting cell
  - Repeat until no more cells which has the same value as the starting cell
"""


from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        # Edge case
        if image[sr][sc] == newColor:
            return image

        def dfs(image, row, col, start_color):

            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != start_color:
                return

            image[row][col] = newColor
            dfs(image, row + 1, col, start_color)
            dfs(image, row - 1, col, start_color)
            dfs(image, row, col + 1, start_color)
            dfs(image, row, col - 1, start_color)

        dfs(image, sr, sc, image[sr][sc])

        return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
print(Solution().floodFill(image, sr, sc, newColor))

