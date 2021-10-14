"""
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Use the shorter string for text1 to reduce a space a little bit more
        if len(text2) < len(text1):
            text1, text2 = text2, text1

        previous = [0] * (len(text1) + 1)

        for col in reversed(range(len(text2))):

            current = [0] * (len(text1) + 1)

            for row in reversed(range(len(text1))):

                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])

            previous = current

        return previous[0]


"""
Bottom up dynamic programming optimizing space
Time: O(nm) by n length text1 and m length text2, Space: O(min(n,m))
"""


text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2))
