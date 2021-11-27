"""
- dp[i] represents the probability of i coins getting head
- when i is 0, just getting the multiples of 1 - each p in prob
- when i is 1,
- dp[1], probability of getting 1 coin head
  -
"""


from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [1] + [0] * target

        # print(f'dp: {dp}')

        for p in prob:

            # print(f'  p: {p}')

            for k in range(target, -1, -1):

                # print(f'    k: {k}')

                # If k is 0, the prob we should get is tail, which is 1 - p
                dp[k] = (dp[k - 1] if k else 0) * p + dp[k] * (1 - p)

        # print(f'dp: {dp}')

        return dp[target]


"""
prob: [0.5,0.5,0.5,0.5,0.5]
target: 1
dp: [1, 0]
p: 0.5, k: 1, dp[0] * p + dp[1] * (1 - p): 1 * 0.5 + 0 * 0.5 = 0.5, dp[1]: 0.5
  k: 0, 0 * 0.5 + dp[0] * 0.5: 1 * 0.5 = 0.5, 
"""


# 0.4
prob = [0.4]
target = 1
# 0.03125
prob = [0.5,0.5,0.5,0.5,0.5]
target = 0
target = 1
print(Solution().probabilityOfHeads(prob, target))



