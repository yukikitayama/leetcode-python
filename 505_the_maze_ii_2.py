from typing import List
import sys


class Solution:

    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        distance = [[sys.maxsize] * len(maze[0]) for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0

        self.recursive_visit(maze, start, distance)

        if distance[destination[0]][destination[1]] == sys.maxsize:
            return -1
        else:
            return distance[destination[0]][destination[1]]

    def recursive_visit(self, maze: List[List[int]], start: List[int], distance: List[List[int]]) -> None:
        # Direction [row, column]: up, down, left, right
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for direction in directions:
            row = start[0] + direction[0]
            col = start[1] + direction[1]
            count = 0

            while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0:
                row += direction[0]
                col += direction[1]
                count += 1

            if distance[start[0]][start[1]] + count < distance[row - direction[0]][col - direction[1]]:
                distance[row - direction[0]][col - direction[1]] = distance[start[0]][start[1]] + count
                self.recursive_visit(maze, [row - direction[0], col - direction[1]], distance)


maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0,4]
destination = [4,4]
# maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
# start = [0,4]
# destination = [3,2]
answer = Solution().shortestDistance(maze, start, destination)
print(f'Answer: {answer}')
