"""
Two pointers, extra space for set
"""


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)

        ans = 0

        for letter in letters:

            i = s.index(letter)
            j = s.rindex(letter)

            middle_letter_set = set()

            # If i and j are adjacent, this skips
            for k in range(i + 1, j):
                middle_letter_set.add(s[k])

            ans += len(middle_letter_set)

        return ans


if __name__ == "__main__":
    s = "aa"
    print(Solution().countPalindromicSubsequence(s))
