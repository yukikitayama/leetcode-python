"""
Simulation
Greedy

First drinnk all bottles to maximize empty bottles
Initialize ans by the drinks and num empty bottles
while num empty bottles >= numExchange
  Increment ans by 1
  Reduce num empty bottles by numExchange
  Increment numExchange
"""


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        ans += numBottles
        num_empty_bottle = numBottles

        while num_empty_bottle >= numExchange:
            # Exchange empty bottle with one water bottle
            num_empty_bottle -= numExchange

            # Drink
            ans += 1
            # Get one extra empty bottle because the drink
            num_empty_bottle += 1

            # Exchange requirement increases because we made one exchange
            numExchange += 1

            # print(f"ans: {ans}, num_empty_bottle: {num_empty_bottle}, numExchange: {numExchange}")

        # print()

        return ans
