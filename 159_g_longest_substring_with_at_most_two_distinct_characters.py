from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)

        if n < 3:
            return n

        left, right = 0, 0

        hashmap = defaultdict()

        max_len = 2

        while right < n:

            hashmap[s[right]] = right
            right += 1

            if len(hashmap) == 3:
                del_idx = min(hashmap.values())
                # print(f'Before del: {hashmap}')
                del hashmap[s[del_idx]]
                # print(f'After del: {hashmap}')
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len


"""
Time complexity
Let n be the length of s, O(n) for right pointer to scan from left to right

Space complexity
O(1) because hashmap length is at most 3, which does not scale up with input, so it's constant
"""


s = "eceba"
print(Solution().lengthOfLongestSubstringTwoDistinct(s))
