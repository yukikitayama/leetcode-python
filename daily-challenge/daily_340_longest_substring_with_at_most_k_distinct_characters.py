import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_so_far = 0

        counter = collections.Counter()

        for right in range(len(s)):
            counter[s[right]] += 1

            if len(counter.keys()) <= k:
                max_so_far += 1

            else:
                # Doesn't contract, but stop expanding, and only slide
                # right - max_so_far is left
                counter[s[right - max_so_far]] -= 1

                if counter[s[right - max_so_far]] == 0:
                    del counter[s[right - max_so_far]]

        return max_so_far

    def lengthOfLongestSubstringKDistinct1(self, s: str, k: int) -> int:
        counter = collections.Counter()

        ans = 0

        left = 0

        for right in range(len(s)):

            counter[s[right]] += 1

            while len(counter.keys()) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans
