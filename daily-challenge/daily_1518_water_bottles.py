class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        empty = 0

        while numBottles > 0:
            ans += numBottles
            empty += numBottles
            numBottles, empty = divmod(empty, numExchange)

        return ans