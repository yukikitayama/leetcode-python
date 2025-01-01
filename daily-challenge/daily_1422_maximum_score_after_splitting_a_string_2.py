class Solution:
    def maxScore(self, s: str) -> int:
        count_one = 0
        for ch in s:
            if ch == "1":
                count_one += 1

        count_zero = 0
        ans = 0
        for ch in s[:-1]:
            if ch == "0":
                count_zero += 1
            elif ch == "1":
                count_one -= 1
            ans = max(
                ans,
                count_zero + count_one
            )

        return ans