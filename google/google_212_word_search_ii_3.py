"""
word: 'abc'
trie: {
    'a': {
        'b': {
            'c': {
                '$': 'abc'
            }
        }
    }
}
"""


from typing import List
import pprint


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        key_to_word = '$'

        # Make a trie
        trie = {}
        for word in words:
            node = trie
            for char in word:
                # setdefault() returns a value. Here it's {}
                # To recursively go to the subsequent values of dictionary,
                # overwrite node with value
                node = node.setdefault(char, {})
            node[key_to_word] = word

        # pprint.pprint(trie)

        def backtracking(row, col, parent):

            # To recover board, save the current letter
            curr_letter = board[row][col]

            # Go to the next level in trie
            curr_node = parent[curr_letter]

            # If match, append the current word to ans
            word_match = curr_node.pop(key_to_word, False)
            if word_match:
                ans.append(word_match)

            # Mark the current cell as visited
            board[row][col] = '#'

            # Go to next
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row = row + x
                next_col = col + y

                # If not out of boundary and not visited, go to the next cell
                if 0 <= next_row < len(board) \
                    and 0 <= next_col < len(board[0]) \
                    and board[next_row][next_col] in curr_node:
                    backtracking(next_row, next_col, curr_node)

            # When it reaches here, backtracking finished, so recover board for the next iteration
            board[row][col] = curr_letter

            # Remove leaf
            if not curr_node:
                parent.pop(curr_letter)

        ans = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return ans


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(Solution().findWords(board, words))

