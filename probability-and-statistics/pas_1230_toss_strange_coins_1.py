"""
- 0.5**5 = 0.03125

- dp[c][k] represents the probability of tossing the first c coins and get k coins faced up
  - c: 1, k: 1
  -


- len(prob): 1, target: 0
  - 1 - p
- len(prob): 1, target: 1
  - p
- len(prob): 2, target: 0
  - (1 - p1) * (1 - p2)


- Let n be the length of prob
- dp[i][j], i: [0, n - 1], j: [0, target]
"""


from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:

        if target == 0:
            ans = 1
            for p in prob:
                ans *= (1 - p)
            return ans

        n = len(prob)
        dp = [[0] * (n + 1) for _ in range(n)]
        # 1st coin tail
        dp[0][0] = 1 - prob[0]
        # 1st coin head
        dp[0][1] = prob[0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] * (1 - prob[i])

        print(f'dp:')
        [print(row) for row in dp]

        for j in range(1, n + 1):
            for i in range(1, n):
                dp[i][j] = dp[i - 1][j - 1] * prob[i] + dp[i - 1][j] * (1 - prob[i])

        print(f'dp:')
        [print(row) for row in dp]

        return dp[n - 1][target]


prob = [0.5,0.5,0.5,0.5,0.5]
target = 1
print(Solution().probabilityOfHeads(prob, target))



