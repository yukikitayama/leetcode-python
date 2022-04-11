"""
- frequency of c in the same character prefix substring + 1
  - +1 because of the current new character
  - Adding to the previous frequency because current character can form substring
    begin and end with the current character with all the previous same characters
"""


import collections


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0

        char_to_count = collections.defaultdict(int)

        for c in s:

            char_to_count[c] += 1

            # Incremented by current char and previous frequency
            ans += char_to_count[c]

            print(f'c: {c}, char_to_count: {char_to_count}, ans: {ans}')

        return ans


if __name__ == '__main__':
    s = "abcba"
    # 7
    s = "abacad"
    # 9
    print(Solution().numberOfSubstrings(s))
