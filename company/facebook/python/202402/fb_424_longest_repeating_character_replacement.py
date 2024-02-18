"""
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        ans = 0

        alphabets = set(s)

        # for alpha in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for alpha in alphabets:

            left = 0
            convert = k

            for right in range(len(s)):

                right_ch = s[right]

                if right_ch != alpha:
                    convert -= 1

                # Contract left pointer
                while convert < 0:
                    left_ch = s[left]
                    if left_ch != alpha:
                        convert += 1
                    left += 1

                ans = max(ans, right - left + 1)

        return ans
