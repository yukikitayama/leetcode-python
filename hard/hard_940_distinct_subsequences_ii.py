"""
dp[k] = dp[k-1] * 2 because add current character to the end or skip current character

s: "abab"
dp[0]: 1 because ""
add "a", dp[1]: 2 because "", "a"
add "b", dp[2]: 4 because "", "a" and "b", "ab"
add "a", dp[3]: 7 because "", "a", "b", "ab" and "a", "aa", "ba", "aba", but "a" already exists before, so the 2nd "a" isn't included to dp[2]
add "b", dp[4]: 12
  "", "a", "b", "aa", "ab", "ba", "aba" and "b", "ab", "bb", "aab", "abb", "bab", "abab"
  "b", "ab" already exists
  "", "a", "b", "aa", "ab", "ba", "bb", "aab", "aba", "abb", "bab", "abab"

i: 2, ch: "a", last: {"a": 0, "b": 1}, dp[last["a"]]: dp[0]: 1, skip "" + "a"
i: 3, ch: "b", last: {"a": 2, "b": 1}, dp[last["b"]]: dp[1]: 2, skip "" + "b", "a" + "b"
"""


class Solution:
    def distinctSubseqII(self, s: str) -> int:

        # +1 for empty string
        dp = [0] * (len(s) + 1)

        # Base case: one way to create empty string
        dp[0] = 1

        last = dict()

        for i, ch in enumerate(s):

            dp[i + 1] = dp[i] * 2

            # Reduce double count
            if ch in last:
                dp[i + 1] -= dp[last[ch]]

            # Record double count
            # e.g. i: 1, ch: b
            # i: 2, ch: a
            last[ch] = i

        # -1 because we need to exclude empty string
        return (dp[-1] - 1) % (10 ** 9 + 7)