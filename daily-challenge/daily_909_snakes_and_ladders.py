from typing import List
import collections


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)

        cells = [None] * (n**2 + 1)
        label = 1

        columns = list(range(n))
        # From the bottom row
        for row in range(n - 1, -1, -1):

            #
            for column in columns:

                cells[label] = (row, column)
                label += 1

            # Alternate direction each row
            columns.reverse()

        # print(cells)

        # Distance to each cell
        dist = [-1] * (n**2 + 1)

        queue = collections.deque([1])
        dist[1] = 0
        while queue:

            curr = queue.popleft()

            for next_ in range(curr + 1, min(curr + 6, n**2) + 1):

                row, column = cells[next_]

                # If ladder or snake
                if board[row][column] != -1:
                    destination = board[row][column]
                # Otherwise go to the within 6 cell
                else:
                    destination = next_

                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    queue.append(destination)

        return dist[n**2]


if __name__ == "__main__":
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]
    print(Solution().snakesAndLadders(board))

