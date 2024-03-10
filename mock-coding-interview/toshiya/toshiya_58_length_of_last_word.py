class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p = len(s)
        ans = 0

        while p > 0:
            p -= 1

            if s[p] == " " and ans == 0:
                continue

            elif s[p] != " ":
                ans += 1

            elif ans > 0:
                return ans

        return ans

    def lengthOfLastWord1(self, s: str) -> int:
        s_str = s.split(" ")
        for i in range(len(s_str) - 1, -1, -1):
            if len(s_str[i]) != 0:
                return len(s_str[i])
