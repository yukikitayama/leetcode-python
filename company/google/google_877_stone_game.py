from typing import List
from functools import lru_cache


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        # dp(i, j) is the largest score that Alice can get
        # from left end piles[i] to right end piles[j]
        # At return statement, we will check whether dp(i, j) is positive or negative
        # If it's positive, Alice got a bigger score, so return True
        # If it's negative, Bob got more score, and Alice's score became negative, so return False to say Bob won
        @lru_cache(maxsize=None)
        def dp(i, j):

            # print(f'In dp: i: {i}, j: {j}')

            if i > j:
                return 0

            # In Alice's turn, there are even items,
            # With even item, last index - first index will be odd,
            # so odd % 2 gives us 1
            # In Bob's turn, there are odd items,
            # With odd item, last index - first index will be even
            # so even % 2 gives us 0
            # n: 4, i: 0, j: 3, j - i - n: 3 - 0 - 4 = -1, -1 % 2: 1
            # n: 4, i: 1, j: 3, j - i - n: 3 - 1 - 4 = 0, 0 % 2: 0
            # parity is 1 if it's Alice's turn
            # parity is 0 if it's Bob's turn
            parity = (j - i - n) % 2

            # print(f'  parity: {parity}')
            if parity == 1:
                # In Alice's turn, Alice wants to maximize its score
                # print(f'    Alice')
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:
                # In Bob's turn, Bob wants to minimize the score Alice gets
                # So the score that Bob gets is negative according to Alice
                # so in min(), multiply -1 to piles[i] or [j]
                # And Bob wants to minimize Alice's score, so min(negative score)
                # print(f'    Bob')
                return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))

        return dp(0, n - 1) > 0


piles = [5,3,4,5]
print(Solution().stoneGame(piles))
