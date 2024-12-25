from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices[:]
        stack = []
        for i in range(len(prices)):

            while stack and prices[i] <= prices[stack[-1]]:
                prev_i = stack.pop()
                ans[prev_i] -= prices[i]

            stack.append(i)

        return ans

    def finalPrices1(self, prices: List[int]) -> List[int]:

        ans = []

        for i in range(len(prices)):
            discount = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break

            # print(f"i: {i}, j: {j}, discount: {discount}, prices[i]: {prices[i]}, prices[j]: {prices[j]}")

            ans.append(prices[i] - discount)

        return ans