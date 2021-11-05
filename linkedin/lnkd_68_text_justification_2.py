"""
- Refactor the code of assigning spaces to words
"""


from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        ans = []
        curr = []
        num_char = 0

        for word in words:

            # Number of characters + number of spaces
            if num_char + len(curr) + len(word) > maxWidth:

                for i in range(maxWidth - num_char):
                    curr[i % (len(curr) - 1 or 1)] += ' '

                line = ''.join(curr)
                ans.append(line)
                curr = []
                num_char = 0

            num_char += len(word)

            curr = curr + [word]

        line = ' '.join(curr)
        line = line.ljust(maxWidth)
        ans.append(line)

        return ans


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
ans = Solution().fullJustify(words, maxWidth)
[print(line) for line in ans]
