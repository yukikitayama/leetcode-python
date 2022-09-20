"""
- 2 pointers sliding window
"""


import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = right = 0

        ans = 1
        num_to_count = collections.defaultdict(int)

        while left < len(s) and right < len(s):

            # print(f'left: {left}, right: {right}')

            if len(num_to_count.keys()) < 2:
                num_to_count[s[right]] += 1
                ans = max(ans, right - left + 1)
                right += 1
            elif s[right] in num_to_count.keys():
                num_to_count[s[right]] += 1
                ans = max(ans, right - left + 1)
                right += 1
            else:
                num_to_count[s[left]] -= 1
                if num_to_count[s[left]] == 0:
                    del num_to_count[s[left]]
                left += 1

            # print(f'num_to_count: {num_to_count}')

        return ans


if __name__ == '__main__':
    s = "eceba"
    # 3
    # s = "ccaabbb"
    # 5
    print(Solution().lengthOfLongestSubstringTwoDistinct(s))
