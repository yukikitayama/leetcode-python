"""
sliding window
  hashset
Hashmap
  k: ch
  v: last index

ans
  If we find a substring that contains at least one occurrence of each required character, then any larger substring that includes it must also be valid.
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        ch_to_i = {
            "a": -1,
            "b": -1,
            "c": -1
        }
        ans = 0

        for i in range(len(s)):
            ch_to_i[s[i]] = i
            ans += 1 + min(ch_to_i.values())

        return ans

    def numberOfSubstrings1(self, s: str) -> int:

        def has_all_chars(freq):
            return all(f > 0 for f in freq)

        left = ans = 0
        freq = [0] * 3

        for right in range(len(s)):

            freq[ord(s[right]) - ord("a")] += 1

            while has_all_chars(freq):
                ans += len(s) - right

                # Contract
                freq[ord(s[left]) - ord("a")] -= 1
                left += 1

        return ans