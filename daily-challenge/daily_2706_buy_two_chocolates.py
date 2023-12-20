from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        smallest = float("inf")
        second_smallest = float("inf")

        for price in prices:

            if price < smallest:
                second_smallest = smallest
                smallest = price
            elif price < second_smallest:
                second_smallest = price

        if smallest + second_smallest <= money:
            return money - (smallest + second_smallest)
        else:
            return money


if __name__ == "__main__":
    prices = [1, 2, 2]
    money = 3
    prices = [3, 2, 3]
    money = 3
    print(Solution().buyChoco(prices, money))

