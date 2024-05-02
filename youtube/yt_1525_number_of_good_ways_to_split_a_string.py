import collections


class Solution:
    def numSplits(self, s: str) -> int:

        counter_left = collections.Counter()
        counter_right = collections.Counter(s)

        ans = 0

        for i in range(len(s)):

            counter_left[s[i]] += 1

            counter_right[s[i]] -= 1
            if counter_right[s[i]] == 0:
                del counter_right[s[i]]

            if len(counter_left) == len(counter_right):
                ans += 1

        return ans