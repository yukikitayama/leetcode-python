class Solution:
    def sortSentence(self, s: str) -> str:
        word_nums = s.split(' ')
        ans = [None] * len(word_nums)

        for wordnum in word_nums:
            word = wordnum[:-1]
            num = int(wordnum[-1])

            ans[num - 1] = word

        return ' '.join(ans)


if __name__ == '__main__':
    s = "is2 sentence4 This1 a3"
    print(Solution().sortSentence(s))
