"""
- Iterate each row and column to find the start cell
  - start cell has a letter match with word[0]
  - Once it finds it, start DFS
    - Initialize current index to word
    - Initialize stack to contain ((row, col), index)
    - Initialize visited set
    - If a new cell has a letter identical to the next character in word
      and not visited and in boundary
      - Go to the cell
        - Append the cell to stack
        - Add it to visited sell
        - Increment index
    - Stop DFS when index is equal to len(word) - 1
      - Return True
  - Otherwise return false

- DFS or BFS?
"""


from typing import List


class Solution:
    def exist(self, board: List[List[int]], word: str) -> bool:
        self.board = board

        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.backtrack(row, col, word):
                    return True

        return False

    def backtrack(self, row, col, suffix):
        # If we find a word, suffix will eventually be the empty string
        # because we remove the first character every time we call backtrack function
        if len(suffix) == 0:
            return True

        # Return False to indicate
        # 1. get out of this recursion and try another direction
        # 2. get out of this recursive function entirely and return False as the answer to this problem
        if row < 0 \
                or row == len(self.board) \
                or col < 0 \
                or col == len(self.board[0]) \
                or self.board[row][col] != suffix[0]:
            return False

        ret = False
        # Mark the current cell as visited to avoid visiting again
        self.board[row][col] = '#'

        for rowOffset, colOffset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # suffix[1:] because we only care the next characters would match
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            if ret:
                # It doesn't return True here, because it wants to reverts '#' to the
                # original character in the board to avoid altering the input data
                break

        self.board[row][col] = suffix[0]

        return ret


"""
- Let m be the number of rows, n be the number of cols and l be the length of word
- Time is O(m*n*3^l) because spend m*n to find the starting cell in the nested for loops before backtrack,
  and in every recursive backtrack function, we have 3 choices to go for each character in word
- Space is O(l) because it has the recursion call stack. The max length is the length of the word.
"""


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(Solution().exist(board, word))

