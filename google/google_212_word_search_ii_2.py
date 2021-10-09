"""
- For each row and column, use it as the starting cell of dfs
- in each iteration, check where the current sequence of characters is in words
- No more cells to go, break out of DFS, and go back to the nested for loops and start from
  the next row and column cell as starting cell.
"""


from typing import List
import pprint


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Make a trie from a list of words, which share prefix
        WORD_KEY = '$'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            # Trie needs to have a node indicating a leaf, that is the end of word
            # To indicate that, put dummy $ mark to hashmap key and set the word as value
            node[WORD_KEY] = word

        # pprint.pprint(trie)

        rowNum = len(board)
        colNum = len(board[0])

        # Define backtracking function
        def backtracking(row, col, parent):
            # Temporarily need to save the current letter
            # to reset the board at the end of this backtracking function
            letter = board[row][col]

            # currNode is also a dictionary with key a character and value dictionary
            currNode = parent[letter]

            # Check if we find a match of word
            # dictionary.pop(key, default) removes and returns an element
            # default is a value returned when the key is not in the dictionary
            # When popped, the value of the key contains the default of setdefault when made trie
            # e.g. letter: h, {'h': {'$': 'oath'}}. After pop, this will be
            # {'h': {}}
            # At the end of backtracking(), this key with empty dictionary as value will be removed
            word_match = currNode.pop(WORD_KEY, False)

            # WORD_KEY contains $. When $ is found in trie dictionary,
            # word_match contains a string word
            # then the following if statement is True for any string word
            # It will be False as long as the above pop gives us False in word_match
            if word_match:
                matchedWords.append(word_match)

            # Mark as visited
            # In the iteration, we always check the next character in board is in Trie
            # and in trie, there's no #. So by marking the visited with #
            # we can avoid visiting here again
            board[row][col] = '#'

            # Find the next cell to iterate
            for (rowOffset, colOffset) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                newRow = row + rowOffset
                newCol = col + colOffset

                # Don't visit if the next cell is out of boundary
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue

                # Also don't visited if already visited ('#') or not in the trie
                if not board[newRow][newCol] in currNode:
                    continue

                # Otherwise okay to visit
                backtracking(newRow, newCol, currNode)

            # Reset the visited cell because we will start a new backtracking from
            # a new starting cell in the nested for loop outside of this backtracking function
            board[row][col] = letter

            # e.g. the below is True is currNode is {}, and from {'h': {}} for example
            if not currNode:
                parent.pop(letter)


        # Backtracking
        matchedWords = []
        for row in range(rowNum):
            for col in range(colNum):

                # The reason for checking trie of words before backtracking is
                # if the first character from board is not even included in the first
                # character in trie of words, we don't have to backtrack the sequence of
                # characters starting from the character.
                if board[row][col] in trie:

                    backtracking(row, col, trie)

        return matchedWords




board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
# words = ["oath", 'oat',"pea","eat","rain"]
print(Solution().findWords(board, words))



