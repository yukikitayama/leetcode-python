class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0

        res = 0

        while right < len(s):

            # Get character
            r = s[right]
            # ord() converts a character to an integer
            chars[ord(r)] += 1

            # When an element in chars array is more than 1,
            # there's duplicate character in substring
            while chars[ord(r)] > 1:
                # Here left pointer moves one by one
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1

        return res



