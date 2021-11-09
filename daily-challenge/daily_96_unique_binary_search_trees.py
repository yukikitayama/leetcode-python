"""
- G(n): The number of unique BST for a sequence of length n
- F(i, n): The number of unique BST, where the number i is root of BST
  - F(i, n) is the cartesian product of left subtrees and right subtrees
  - e.g. F(3, 7) = G(2) * G(4)
  - F(i, n) = G(i - 1) * G(n - i)
- G(n) is equal to the sum of F(i, n) from i equal to 1 to n
  - G(n) = sum of G(i - 1) * G(n - i) from i equal to 1 to n
- G(0) because there's only one combination of making empty tree
- G(1) because there's only one combination of making length 1 only root tree
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[-1]

