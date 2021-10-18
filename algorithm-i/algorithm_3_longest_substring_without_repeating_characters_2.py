class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        mp = {}

        left = 0
        for right in range(n):

            # Set the previously seen index plus 1 to left pointer if duplicate found
            if s[right] in mp:
                # mp[s[right]] gives us the index of the current character previously seen plus 1
                # It's not getting current right pointer index, just using the right pointer to
                # get a specific character
                left = max(mp[s[right]], left)

            ans = max(ans, right - left + 1)
            mp[s[right]] = right + 1

        return ans


"""
s: "abbc"
mp: {'a': 1, 'b': 2}
left: 0, right: 2, s[right]: b, if: T, mp[s[right]]: mp[b] = 2, left: max(2, 0) = 2

s: 'abcb'
mp: {'a': 1, 'b': 2, 'c': 3}
"""