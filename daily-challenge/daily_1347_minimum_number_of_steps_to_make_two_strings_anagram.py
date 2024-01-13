"""
positive value means the character of t should be replaced to s
negative value means the character of s should be replaced to t
but only positive value is necessary, because when we replace t character, we can use s character, so
the negative value will be fulfilled


Greedy
Counter
Keys which exist in both s and t
  count up absolute difference of value of the same keys
Keys which exist in s but don't exist in t
  count up by the values of the key in s

One step to replace affects the following steps, and we want minimum, so is this DP?

s = "bab", t = "aba"
s
  a: 1
  b: 2
t
  a: 2
  b: 1

One decrement is another increment
"""

import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:

        ch_to_count = collections.defaultdict(int)

        for i in range(len(s)):

            ch_to_count[s[i]] -= 1
            ch_to_count[t[i]] += 1

        ans = 0

        for k in ch_to_count:
            if ch_to_count[k] > 0:
                ans += ch_to_count[k]

        return ans


if __name__ == "__main__":
    s = "bab"
    t = "aba"

    s = "leetcode"
    t = "practice"
    print(Solution().minSteps(s, t))
