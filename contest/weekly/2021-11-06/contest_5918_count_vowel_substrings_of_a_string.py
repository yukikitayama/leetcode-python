"""
- Brute force
  - start index
  - end index
  - Take set of the current substring
"""


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0

        for start in range(len(word)):

            # +1 because end slice is exclusive
            for end in range(start + 5, len(word) + 1):

                char_set = set(word[start:end])

                if char_set == {'a', 'e', 'i', 'o', 'u'}:
                    ans += 1

        return ans


word = "aeiouu"  # 2
word = "unicornarihan"  # 0
word = "cuaieuouac"  # 7
print(Solution().countVowelSubstring(word))
