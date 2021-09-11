from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        N = len(quality)

        ans = float('inf')

        for captain in range(N):
            factor = wage[captain] / quality[captain]
            prices = []
            # print(f'Captain: {captain}')

            for worker in range(N):
                price = factor * quality[worker]

                if price < wage[worker]:
                    continue

                prices.append(price)

            # print(prices)

            # Skip because if this is True, the number of hired workers is not enough for the plan to hire k
            if len(prices) < k:
                continue

            # To get the minimum coast, sort the cost in an ascending order
            prices.sort()
            # prices[:k] because we cannot hire more than k
            ans = min(ans, sum(prices[:k]))
            # print(f'Updated answer: {ans} with prices: {prices} and tried cost in this iteration: {sum(prices[:k])}')

        return float(ans)


quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
print(Solution().mincostToHireWorkers(quality, wage, k))
