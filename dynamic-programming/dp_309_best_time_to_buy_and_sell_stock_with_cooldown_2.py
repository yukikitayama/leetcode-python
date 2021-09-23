from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = float('-inf')
        held = float('-inf')
        rest = 0

        for i in range(len(prices)):
            tmp_sold = sold
            sold = held + prices[i]
            held = max(held, rest - prices[i])
            rest = max(rest, tmp_sold)

        return max(rest, sold)


"""
Time: O(n), Space: O(1)
"""


prices = [1, 2, 3, 0, 2]
"""
sold: [-inf, None, None, None, None, None]
held: [-inf, None, None, None, None, None]
rest: [0, None, None, None, None, None]
i: 0, 
  held: [-inf, -1, None, None, None, None], 
  rest: [0, 0, None, None, None, None], 
  sold: [-inf, -inf, None, None, None, None]
i: 1,
  held: [-inf, -1, ]
...
i: 4  
"""
# prices = [1]
print(Solution().maxProfit(prices))
