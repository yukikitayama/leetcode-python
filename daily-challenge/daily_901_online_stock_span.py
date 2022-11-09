class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_ans = self.stack.pop()
            ans += prev_ans

        self.stack.append([price, ans])

        return ans
