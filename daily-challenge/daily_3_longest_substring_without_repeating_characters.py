"""
- Two pointers, sliding windows
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        mp = {}
        i = 0
        for j in range(n):
            if s[j] in mp:
                i = max(i, mp[s[j]])

            ans = max(ans, j - i + 1)

            # +1 because we will use this number to exclude at j
            mp[s[j]] = j + 1

        return ans


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        curr = set()

        ans = 0

        while left < len(s) and right < len(s):

            if s[right] not in curr:
                curr.add(s[right])
                ans = max(ans, right - left + 1)
                right += 1
            else:
                curr.remove(s[left])
                left += 1

        return ans


if __name__ == '__main__':
    s = "abcabcbb"
    # 3
    s = "bbbbb"
    # 1
    s = "pwwkew"
    # 3
    print(Solution().lengthOfLongestSubstring(s))
