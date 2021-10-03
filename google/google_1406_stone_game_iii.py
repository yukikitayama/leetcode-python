"""
Question
One stone at each index in the array, but each stone has a different score
Players are allowed to take at most 3 stones at a time.
Score could be negative
"""


from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0] * (len(stoneValue) + 1)

        # print(f'stoneValue: {stoneValue}')
        # print(f'Before dp: {dp}')

        # stoneValue: [1,2,3,7]
        # dp: [0, 0, 0, 0, 0]
        # range: (3, 2, 1, 0)

        # Iterate from the end
        # len(stoneValue) - 1 because stoneValue is 1 length less than dp array
        for i in range(len(stoneValue) - 1, -1, -1):
            # Up date best by max() so initialize with small number
            best = float('-inf')

            # When at the end of the stoneValue
            if i == len(stoneValue) - 1:
                best = stoneValue[i]

            elif i == len(stoneValue) - 2:
                # Alice takes the stone at the second last and bob takes the last stone
                take_one_stone = stoneValue[i] - stoneValue[i + 1]
                # Alice takes both second last and the last stones and bob get 0 scores
                take_two_stones = stoneValue[i] + stoneValue[i + 1]
                # Best score that Alica can make, not bob
                best = max(take_one_stone, take_two_stones)

            # The last 3 stones or the remaining from 0 index
            else:
                take_one_stone = stoneValue[i] - dp[i + 1]
                take_two_stones = stoneValue[i] + stoneValue[i + 1] - dp[i + 2]
                take_three_stones = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3]
                best = max(take_one_stone, take_two_stones, take_three_stones)

            dp[i] = best

        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'



"""
Algorithm
- dp array represents best difference of alice score minus bob score, starting at index i of stoneValue
- so if dp[0] is positive, alice winds, negative bob, otherwise Tie
"""
values = [1,2,3,7]
values = [1,2,3,-9]
values = [1,2,3,6]
print(Solution().stoneGameIII(values))

