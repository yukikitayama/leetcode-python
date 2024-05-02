from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:

        def check_balance(r, c):
            balance = 0
            balance += int(grid[r][c] == "B")
            balance += int(grid[r + 1][c] == "B")
            balance += int(grid[r][c + 1] == "B")
            balance += int(grid[r + 1][c + 1] == "B")
            return abs(balance) != 2

        for r in range(2):
            for c in range(2):
                if check_balance(r, c):
                    return True

        return False