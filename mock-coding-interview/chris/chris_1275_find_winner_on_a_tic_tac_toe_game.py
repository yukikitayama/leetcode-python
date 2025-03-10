from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        diagonal = anti_diagonal = 0

        for i, (r, c) in enumerate(moves):

            offset = 1 if i % 2 == 0 else -1

            rows[r] += offset
            cols[c] += offset
            # Diagonal
            if r == c:
                diagonal += offset
            # Anti diagonal, [0, 2], r + c = 2, [1, 1] = 2, [2, 0] =
            if r + c == 2:
                anti_diagonal += offset

            if rows[r] == 3 or cols[c] == 3 or diagonal == 3 or anti_diagonal == 3:
                return "A"
            elif rows[r] == -3 or cols[c] == -3 or diagonal == -3 or anti_diagonal == -3:
                return "B"

        if len(moves) == 9:
            return "Draw"
        elif len(moves) < 9:
            return "Pending"