from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                answer += prices[i] - prices[i - 1]
        return answer


"""
Because we are allowed to trade multiple times, we trade all the time as long as it makes profit
Time: O(n), Space: O(1)
"""


prices = [7,1,5,3,6,4]
"""

"""