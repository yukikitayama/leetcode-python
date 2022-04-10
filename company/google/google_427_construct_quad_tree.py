"""
- Divide and conquer
"""


from typing import List


# QuadTree node
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        # print(f'grid: {grid}')

        if not grid:
            return None

        if self.is_leaf(grid):
            # print(f'grid: {grid}')
            return Node(grid[0][0] == 1, True, None, None, None, None)

        n = len(grid)

        # '*' because if it's not isLeaf, set val to any value
        return Node(
            val='*',
            isLeaf=False,
            topLeft=self.construct([row[:(n // 2)] for row in grid[:(n // 2)]]),
            topRight=self.construct([row[(n // 2):] for row in grid[:(n // 2)]]),
            bottomLeft=self.construct([row[:(n // 2)] for row in grid[(n // 2):]]),
            bottomRight=self.construct([row[(n // 2):] for row in grid[(n // 2):]])
        )

    # To check the current grid has all the same values
    # either 0 or 1 is fine, so use grid[0][0] for reference
    def is_leaf(self, grid):
        flag = True
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != grid[0][0]:
                    flag = False

        # print(f'flag: {flag}')

        return flag


if __name__ == '__main__':
    grid = [[0, 1], [1, 0]]
    ans = Solution().construct(grid)
    print(f'ans.isLeaf: {ans.isLeaf}, ans.val: {ans.val}')
    top_left = ans.topLeft
    print(f'top_left.isLeaf: {top_left.isLeaf}, top_left.val: {top_left.val}')
    top_right = ans.topRight
    print(f'top_right.isLeaf: {top_right.isLeaf}, top_right.val: {top_right.val}')
    bottom_left = ans.bottomLeft
    print(f'bottom_left.isLeaf: {bottom_left.isLeaf}, bottom_left.val: {bottom_left.val}')
    bottom_right = ans.bottomRight
    print(f'bottom_right.isLeaf: {bottom_right.isLeaf}, bottom_right.val: {bottom_right.val}')

