class Solution:
    def partitionString(self, s: str) -> int:

        alphabets = [-1] * 26

        ans = 1

        start = 0

        for i in range(len(s)):

            if alphabets[ord(s[i]) - ord("a")] >= start:
                ans += 1
                start = i

            alphabets[ord(s[i]) - ord("a")] = i

        return ans

