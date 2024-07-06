"""
n: 3
time: 7
7 // (2) = 3 (full round)
  if odd, move backward after full round
  if even, move forward
7 % 2 = 1
"""


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        full_round, remaining = divmod(time, n - 1)

        if full_round % 2 == 0:
            return remaining + 1
        else:
            return n - remaining

    def passThePillow1(self, n: int, time: int) -> int:
        ans = 1
        updater = 1
        for _ in range(time):
            ans += updater

            if ans == n:
                updater = -1
            elif ans == 1:
                updater = 1

        return ans