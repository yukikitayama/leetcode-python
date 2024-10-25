class Solution:
    def minimumSteps(self, s: str) -> int:
        left = 0
        ans = 0

        for right in range(len(s)):

            if s[right] == "0":

                ans += right - left
                left += 1

        return ans