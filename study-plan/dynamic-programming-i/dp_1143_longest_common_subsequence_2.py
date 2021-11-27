"""
"""


from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Recursive case 1 if current characters in text1 and text2 match
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)

            # Recursive case 2. Current characters do not match, so we need to move
            # one character in either text1 or text2
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))

        return memo_solve(0, 0)


"""
Bottom up dynamic programming
"""


text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2))
