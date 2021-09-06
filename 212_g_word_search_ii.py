from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Initialize Trie for word prefix
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            # This tells that a word exists in Trie
            node['$'] = word

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):
            """parent: trie node"""
            letter = board[row][col]
            currNode = parent[letter]

            # $ is a key for the value True, meaning a word exists in Trie,
            # otherwise Python dictionary.pop(something, False) returns False
            # so word_match: {Python string word, False}
            word_match = currNode.pop('$', False)

            if word_match:
                matchedWords.append(word_match)

            # Before exploration, check it's visited to avoid cycling
            board[row][col] = '#'

            # Up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset

                # If a new cell is out of bound
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                # If the current letter is not in a Node in the Trie
                # currNode is a dictionary, so the below check whether a letter is in dictionary keys
                if board[newRow][newCol] not in currNode:
                    continue

                backtracking(newRow, newCol, currNode)

            # After exploration, restore the cell for a new exploration
            board[row][col] = letter

            # ?
            if not currNode:
                parent.pop(letter)

        # Start exploring all the cells in the board
        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(Solution().findWords(board, words))
