"""
- 'a', 'bb'
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

                # print(f'  curr: {curr}')

                num_spaces = maxWidth - num_char

                # Assign spaces after the words except the last word
                i = 0
                while num_spaces:
                    curr[i] = curr[i] + ' '
                    num_spaces -= 1
                    i += 1
                    if len(curr) - 1 > 0:
                        i = i % (len(curr) - 1)
                    else:
                        i = 0

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
