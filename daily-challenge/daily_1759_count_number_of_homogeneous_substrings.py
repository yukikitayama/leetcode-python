"""
Two pointers, one pass, time O(n)
"""


class Solution:
    def countHomogeneous(self, s: str) -> int:
        ans = 0
        streak = 0
        mod = 10**9 + 7

        for i in range(len(s)):

            if i == 0 or s[i] == s[i - 1]:
                streak += 1

            else:
                streak = 1

            ans = (ans + streak) % mod

        return ans


if __name__ == "__main__":
    s = "abbcccaa"
    print(Solution().countHomogeneous(s))

