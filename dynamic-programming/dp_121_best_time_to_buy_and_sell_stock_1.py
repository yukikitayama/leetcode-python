from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize base case
        min_so_far = prices[0]
        # Initialize answer with 0, which will be returned if we can't find positive profit
        answer = 0

        for i in range(1, len(prices)):
            # This profit could be negative
            profit = prices[i] - min_so_far
            if profit > 0:
                answer = max(answer, profit)
            # Keep minimum stock price so far to make one pass possible
            min_so_far = min(min_so_far, prices[i])

        return answer


"""
Time: O(n), Space: O(1)
"""


prices = [7, 1, 5, 3, 6, 4]
"""
i: 1, profit: 0, min: 1,
i: 2, profit: 4, min: 1,
"""
prices = [7,6,4,3,1]
"""
min: 7, answer: 0
i: 1, profit: 0, 
"""

