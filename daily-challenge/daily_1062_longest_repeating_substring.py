import collections


class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        ans = 0

        for left in range(1, n + 1):
            for right in range(left + 1, n + 1):
                if s[left - 1] == s[right - 1]:
                    dp[left][right] = dp[left - 1][right - 1] + 1
                    ans = max(
                        ans,
                        dp[left][right]
                    )

        for row in dp:
            print(row)

        return ans

    def longestRepeatingSubstring1(self, s: str) -> int:
        counter = collections.Counter()
        for left in range(len(s)):
            for right in range(left, len(s)):
                sub = s[left:right + 1]
                counter[sub] += 1

        max_freq = max(counter.values())

        # print(f"max_freq: {max_freq}")
        # print(counter)

        if max_freq == 1:
            return 0

        ans = ""
        for k, v in counter.items():
            if v > 1:
                if len(k) > len(ans):
                    ans = k

        return len(ans)
