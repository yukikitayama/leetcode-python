from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        start = 0

        for i in range(rows):

            # Fill the current row with 1 length left
            start += cols - 1

            # Assume the length of every word in sentence is less than or equal to cols
            # to avoid a word being split into two lines

            # If current start is at space, before going to the next time, just fill the remaining one space,
            # because every word needs to be separated by one space, meaning
            # we cannot fill additional word to the current row
            if s[start % len(s)] == ' ':
                start += 1

            # If current start at the end of the word, meaning the current start + 1 is empty space,
            # need to fill 2 spaces. So it will be "--" (space and space) or "-a" (space and additional word)
            elif s[(start + 1) % len(s)] == ' ':
                start += 2

            # In the middle of a word, so the word cannot fit in a row,
            # so move cursor back until space
            else:
                while start > 0 and s[(start - 1) % len(s)] != ' ':
                    start -= 1

        return int(start / len(s))


# sentence = ["a", "bcd", "e"]
# rows = 3
# cols = 6
sentence = ["a", "bc", "def", "ghij"]
rows = 3
cols = 4
s = " ".join(sentence) + " "
print(f'len(s): {len(s)}')
"""
Explanation:
a-bcd- 
e-a---
bcd-e-
"""
print(Solution().wordsTyping(sentence, rows, cols))
