from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            price = prices[i]
            profit = price - min_so_far
            ans = max(ans, profit)
            min_so_far = min(min_so_far, price)

        return ans


"""
prices: [7,1,5,3,6,4]
min_so_far: 7
ans: 0
i: 1, price: 1, profit: 1 - 7 = -6, ans: 0, min_so_far: 1
i: 2, price: 5, profit: 5 - 1 = 4, ans: 4, min_so_far: 1

"""
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))


