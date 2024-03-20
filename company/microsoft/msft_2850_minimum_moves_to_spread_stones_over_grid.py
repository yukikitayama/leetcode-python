"""
Backtracking of pairs of source cell and destination cell
  source cell is cell which is more than 1
    duplicate this cell by the number exceeding 1
  destination cell is 0 cell
"""

from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:

        more_than_ones = []
        zeros = []

        for r in range(3):
            for c in range(3):

                if grid[r][c] == 0:
                    zeros.append([r, c])

                else:
                    # Get how many 1s can move
                    move = grid[r][c] - 1

                    while move > 0:
                        more_than_ones.append([r, c])
                        move -= 1

        # print("more_than_ones", more_than_ones)
        # print("zeros", zeros)

        ans = float("inf")
        visited = [False] * len(zeros)

        def backtracking(more_than_ones, zeros, fills, total_distance, from_):
            nonlocal ans

            # Terminate
            if fills == len(zeros):
                ans = min(ans, total_distance)
                return

            for i in range(len(zeros)):

                if visited[i]:
                    continue

                visited[i] = True

                # Compute manhattan distance
                distance = abs(zeros[i][0] - more_than_ones[from_][0]) + abs(zeros[i][1] - more_than_ones[from_][1])

                backtracking(
                    more_than_ones,
                    zeros,
                    # Filled one 0 cell, so go to next
                    fills=fills + 1,
                    # Increment total distance by the current distance gained
                    total_distance=total_distance + distance,
                    # Go to the next more then one cell
                    from_=from_ + 1
                )

                # Backtracking
                visited[i] = False

        backtracking(
            more_than_ones,
            zeros,
            fills=0,
            total_distance=0,
            from_=0
        )

        return ans
