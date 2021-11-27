from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        answers = []

        answer = ''

        def word_break(s, word_dict, start, answer):
            if start == len(s):
                return answer

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict:
                    answer += word + ' '
                    return word_break(s, word_dict, end, answer)

        answer = word_break(s, wordDict, 0, answer)
        answer = answer.strip()
        answers.append(answer)

        return answers


s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
print(Solution().wordBreak(s, wordDict))
