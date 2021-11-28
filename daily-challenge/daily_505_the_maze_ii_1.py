from typing import List
import sys


class Solution:
    def __init__(self):
        self.distance = [[sys.maxsize] * len(maze) for _ in range(len(maze))]

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        # start position we can always reach
        self.distance[start[0]][start[1]] = 0

        self.recursive_visit(maze, start)

        if self.distance[destination[0]][destination[1]] == sys.maxsize:
            return -1
        else:
            return self.distance[destination[0]][destination[1]]

    def recursive_visit(self, maze: List[List[int]], start: List[int]) -> None:
        # direction [row, column]: right, left, up, down
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        for direction in directions:
            row = start[0] + direction[0]
            col = start[1] + direction[1]

            count = 0

            while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0:

                row += direction[0]
                col += direction[1]
                count += 1

            # Went one step too much by adding direction, so come back one step by subtracting one direction
            if self.distance[start[0]][start[1]] + count < self.distance[row - direction[0]][col - direction[1]]:
                self.distance[row - direction[0]][col - direction[1]] = self.distance[start[0]][start[1]] + count
                self.recursive_visit(maze, [row - direction[0], col - direction[1]])



# maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
# start = [0,4]
# destination = [4,4]
maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [3,2]
# [print(row) for row in maze]
answer = Solution().shortestDistance(maze, start, destination)
print(f'Answer: {answer}')
