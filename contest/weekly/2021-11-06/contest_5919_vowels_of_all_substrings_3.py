"""
- a: 1
- ab: 1 + 1
- aba:
"""


class Solution:
    def countVowels(self, word: str) -> int:
        binary_word_list = []
        for i in range(len(word)):
            if word[i] in ['a', 'e', 'i', 'o', 'u']:
                binary_word_list.append(1)
            else:
                binary_word_list.append(0)

        print(f'binary_word_list: {binary_word_list}')

        dp = [0] * len(word)
        for i in range(len(binary_word_list)):
            if binary_word_list[i]:
                dp[i] = 1
            if i > 0:
                dp[i] = dp[i - 1]
                dp[i] += dp[i] * dp[i - 1]

        print(f'dp: {dp}')


word = "aba"  # 6
# word = "abc"  # 3
# word = "ltcd"  # 0
# word = "noosabasboosa"  # 237
print(Solution().countVowels(word))

