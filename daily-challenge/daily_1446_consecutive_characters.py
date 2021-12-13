class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        curr = 1
        for i in range(1, len(s)):

            if s[i] == s[i - 1]:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 1

        return ans


s = "leetcode"
s = "abbcccddddeeeeedcba"
s = "tourist"
print(Solution().maxPower(s))
