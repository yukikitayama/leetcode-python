from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:

        # left to right, right to left
        words = [word, word[::-1]]

        n = len(word)

        # * is unpacking, zip() use each unpacked
        # for b in board: each row
        # for b in zip(*board): unpacked to rows, zip the same column index in each row
        for b in [board, zip(*board)]:
            for row in b:

                # '#' will be '' length 0 string
                row_str = ''.join(row).split('#')

                # print(f'row_str: {row_str}')

                for w in words:

                    for s in row_str:

                        # To fill a word, a place needs to be the same length by empty and character
                        if len(s) == n and all(s[i] == w[i] or s[i] == ' ' for i in range(n)):
                            return True

        return False


if __name__ == '__main__':
    board = [
        ["#", " ", "#"],
        [" ", " ", "#"],
        ["#", "c", " "]
    ]
    word = "abc"
    print(Solution().placeWordInCrossword(board, word))
