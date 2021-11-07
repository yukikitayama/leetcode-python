"""
"""


class Solution:
    def countVowels(self, word: str) -> int:
        binary_word_list = []
        for i in range(len(word)):
            if word[i] in ['a', 'e', 'i', 'o', 'u']:
                binary_word_list.append(1)
            else:
                binary_word_list.append(0)

        ans = 0
        for start in range(len(word)):
            for end in range(start, len(word) + 1):
                substring = binary_word_list[start:end]
                ans += sum(substring)

        return ans



word = "aba"  # 6
word = "abc"  # 3
word = "ltcd"  # 0
word = "noosabasboosa"  # 237
print(Solution().countVowels(word))

