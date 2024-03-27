import collections


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counter = collections.Counter()

        ans = 0
        left = 0

        for right in range(len(s)):

            curr_char = s[right]

            counter[curr_char] += 1

            if max(counter.values()) < 3:
                ans = max(ans, right - left + 1)
            else:
                while max(counter.values()) > 2:
                    counter[s[left]] -= 1
                    left += 1

        return ans

