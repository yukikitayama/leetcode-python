from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        rest = 0
        held = float('-inf')
        sold = float('-inf')

        for price in prices:

            prev_rest = rest
            prev_held = held
            rest = max(prev_rest, sold)
            held = max(prev_held, prev_rest - price)
            sold = prev_held + price

        return max(rest, sold)


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    # 3
    prices = [1]
    # 0
    print(Solution().maxProfit(prices))


