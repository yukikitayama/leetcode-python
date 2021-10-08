"""
Top down dynamic programming
"""


from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def top_down_dp(p1, p2):

            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Option 1 to not include a character in text1
            # There's no plus 1 outside of top_down_dp()
            option_1 = top_down_dp(p1 + 1, p2)

            # Option 2 to include a character in text2
            # find(string to find, start)
            first_occurence = text2.find(text1[p1], p2)
            # text1 character might not be in text2, so in that case, we don't need recursion
            # so return 0 because it's not common character
            option_2 = 0
            if first_occurence != -1:
                # Move both one character forward for text1 and text2 indices
                # Because each character was found in text1 and text2
                option_2 = 1 + top_down_dp(p1 + 1, first_occurence + 1)

            return max(option_1, option_2)

        # First and second arguments are indices to text1 and text2
        return top_down_dp(0, 0)


text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2))
