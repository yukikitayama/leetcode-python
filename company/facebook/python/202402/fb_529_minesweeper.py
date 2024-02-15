"""
Current cell value depends on neighbors

Recursion starts from click cell
  Neighbors
    8 directions
    in grid
    E cells

Terminate
  If current cell is E
  If current cell is number of mines nearby
"""


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        if not board:
            return board

        click_row, click_col = click

        # 1. If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
        if board[click_row][click_col] == "M":
            board[click_row][click_col] = "X"
            return board

        directions = [
            (-1, 0), (0, 1), (1, 0), (0, -1),
            (-1, -1), (-1, 1), (1, 1), (1, -1)
        ]

        def dfs(r, c):

            # Terminate
            if board[r][c] != "E":
                return

            # Check how many mines are in neighbor
            count_mine = 0
            for offset_r, offset_c in directions:
                next_r = r + offset_r
                next_c = c + offset_c

                if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]) and board[next_r][next_c] == "M":
                    count_mine += 1

            # 3. f an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
            if count_mine != 0:
                board[r][c] = str(count_mine)
                # Terminate
                return

            # 2. If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
            if count_mine == 0:
                board[r][c] = "B"

                for offset_r, offset_c in directions:
                    next_r = r + offset_r
                    next_c = c + offset_c
                    if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]):
                        dfs(next_r, next_c)

        dfs(click_row, click_col)

        return board
