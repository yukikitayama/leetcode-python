from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_sor_far = prices[0]
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - min_sor_far)
            min_sor_far = min(min_sor_far, prices[i])
        return ans


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
