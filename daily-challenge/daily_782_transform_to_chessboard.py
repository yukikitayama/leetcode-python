from typing import List
from collections import Counter


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        ans = 0

        # print('Row')
        # print(Counter(map(tuple, board)))
        # print('Column')
        # print(Counter(zip(*board)))

        # map(tuple, board) because Counter cannot use list of list
        # Counter(map(tuple, board)) returns a dictionary with Key row pattern and Value count of the pattern
        # Because board is list of list, zip(*board) extracts elements at the same index from each list,
        # make it tuple together, and gives us the items of tuples. So from each row, getting items, so gives us column
        # Counter(zip(*board)) give us a dictionary with Key column pattern and Value count of the pattern
        for count in (Counter(map(tuple, board)), Counter(zip(*board))):
            # print(f'count: {count}')

            # print(count.values())
            # The number of kinds of lines need to be 2
            # n / 2 for even length board, and (n + 1) / 2 for odd length board
            # First condition checks pattern has only 2 to be chessboard
            # Second condition checks number of each pattern needs to be
            # half fo the board size or half plus one for odd length
            if len(count) != 2 or sorted(count.values()) != [n // 2, (n + 1) // 2]:
                return - 1


            # Get only pattern
            line1, line2 = count

            # print(f'line1: {line1}, line2: {line2}')

            # Two line needs to be opposite
            # ^ gives us the opposite idea
            # ^ gives us true if one of the operands is true
            # 0^0: 0, 1^1: 0, 0^1: 1, 1^0: 1
            if not all(x ^ y for x, y in zip(line1, line2)):
                return -1

            # print(f'line1.count(1): {line1.count(1)}')
            # print(f'line1.count(1) * 2: {line1.count(1) * 2}')
            # print(f'line1.count(1) * 2 > n: {line1.count(1) * 2 > n}')
            # print(f'+(line1.count(1) * 2 > n): {+(line1.count(1) * 2 > n)}')

            # line1.count(1) gives us the number of appearance of the second pattern
            # if n % 2 gets odd length board
            # +() to make boolean 1 0 integer
            starts = [+(line1.count(1) * 2 > n)] if n % 2 else [0, 1]

            # print(f'starts: {starts}')

            """
            I couldn't understand below
            """

            # To transform line1 into the ideal line [i%2 for i ...],
            # we take the number of differences and divide by two
            ans += min(sum((i-x) % 2 for i, x in enumerate(line1, start))
                       for start in starts) / 2

        return int(ans)


board = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
# board = [[1, 0, 1], [1, 0, 1], [0, 1, 0]]
# board = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
print(Solution().movesToChessboard(board))
