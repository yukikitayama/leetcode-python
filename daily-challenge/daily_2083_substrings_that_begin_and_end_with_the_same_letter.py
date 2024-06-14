class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0

        count = [0] * 26

        for i in range(len(s)):

            count[ord(s[i]) - ord("a")] += 1
            ans += count[ord(s[i]) - ord("a")]

        return ans