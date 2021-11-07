"""
- brute force
  - iterate start index
  - iterate end index
  - For each substring, run count_vowels()
- count_vowels()
  -
"""


class Solution:
    def countVowels(self, word: str) -> int:

        def count_vowels(word):
            ans = 0
            for char in word:
                if char in ['a', 'e', 'i', 'o', 'u']:
                    ans += 1
            return ans

        ans = 0
        for start in range(len(word)):
            for end in range(start, len(word) + 1):
                substring = word[start:end]
                ans += count_vowels(substring)

        return ans


word = "aba"
word = "abc"
word = "ltcd"
word = "noosabasboosa"
print(Solution().countVowels(word))

