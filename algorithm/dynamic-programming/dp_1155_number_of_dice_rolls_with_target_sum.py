"""
- Counting DP
- State
  - d: number of dices
  - f: max number that a dice has
  - remaining: target - so far
- Base case
  - d == 0
    - If target is bigger than 0, then the number of possible ways is 0
      because there are no more dice left to throw to reach the remaining target
    - otherwise, it means target is 0, there's one way to reach 0 target, which is no throwing a dice
      in fact, there's no dice to throw because of d == 0
- Recurrence relation
  - dp(d, f, target) = dp(d - 1, f, target - 1) + dp(d - 1, f, target - 2) + ... + dp(d - 1, f, target - f)
    - d - 1: use another dice
    - target - 1: when the dice returns 1
    - target - f: whne the dice returns f
  - Iterate dice
    - Iterate number on a dice
      -
- Top-down dp
"""


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        memo = {}

        def dp(d, target):
            # Base case
            # If no more dice is left
            if d == 0:
                # There's no way to reach the target if target > 0
                if target > 0:
                    return 0
                # There's one way to reach target 0 with 0 dice, which is not throwing a dice
                else:
                    return 1

            if (d, target) in memo:
                return memo[(d, target)]

            ans = 0
            # ?
            # e.g. f: 6, target: 3, dice can return 1 to 6,
            # when throwing a dice, next target could be (0, 1, 2), because there's no negative target
            #   0: current dice is 3, 1: dice is 2, 2: dice is 3
            #   there's no 3 because every dice needs to return at least 1
            # target - f: -3
            # range: (0, 1, 2)
            #
            # e.g. f: 6, target: 7,
            # range: 1, 2, ... 6
            for i in range(max(0, target - f), target):
                ans += dp(d - 1, i)

            memo[(d, target)] = ans

            return ans

        return dp(d, target) % 1_000_000_007


d = 1
f = 6
target = 3
d = 2
f = 6
target = 7
print(Solution().numRollsToTarget(d, f, target))

