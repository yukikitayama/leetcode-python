from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = [None for _ in range(len(prices) + 1)]
        held = [None for _ in range(len(prices) + 1)]
        rest = [None for _ in range(len(prices) + 1)]

        sold[0] = float('-inf')
        held[0] = float('-inf')
        rest[0] = 0

        for i in range(len(prices)):
            sold[i + 1] = held[i] + prices[i]
            held[i + 1] = max(rest[i] - prices[i], held[i])
            rest[i + 1] = max(rest[i], sold[i])

        return max(sold[-1], rest[-1])


"""
Time: O(n), Space: O(n)
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
