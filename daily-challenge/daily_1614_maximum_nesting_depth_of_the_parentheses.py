class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        balance = 0

        for i in range(len(s)):

            if s[i] == "(":
                balance += 1

            elif s[i] == ")":
                balance -= 1

            ans = max(ans, balance)

        return ans
