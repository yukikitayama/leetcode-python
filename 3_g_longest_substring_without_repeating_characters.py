class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        char_to_count = {}

        answer = 0

        while right < len(s):
            r = s[right]
            if r not in char_to_count:
                char_to_count[r] = 1
            else:
                char_to_count[r] += 1

            while char_to_count[r] > 1:
                l = s[left]
                char_to_count[l] -= 1
                left += 1

            # right: 3, left: 0, len = 3 - 0 + 1 = 4
            # + 1 because index starts from 0
            answer = max(answer, right - left + 1)

            right += 1

        return answer

s = "abcabcbb"
s = 'bbbbb'
s = 'pwwkew'
s = ''
print(Solution().lengthOfLongestSubstring(s))
