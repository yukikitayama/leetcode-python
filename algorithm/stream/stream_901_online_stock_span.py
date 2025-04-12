"""
Store price in array
next
  iterate from right
  increment span while prev price is less than or equal to given price
Repetition

prices: [1, 2, 3]
price: 4
span: 4
prices: [1, 2, 3, 4]
price: 5
span: 5
(price, length)

T: amortized O(1)
S: O(N)
"""


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1

        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]

        self.stack.append([price, ans])

        # print(price, self.stack)

        return ans


class StockSpanner1:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        span = 0
        self.prices.append(price)
        i = len(self.prices) - 1
        while i >= 0:
            if self.prices[i] > price:
                break
            i -= 1
            span += 1
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)