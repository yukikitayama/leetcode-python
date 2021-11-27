from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0

        for w in words:

            print(f'w: {w}, num_of_letters: {num_of_letters}, '
                  f'len(w): {len(w)}, len(cur): {len(cur)}')

            # If appending current word to the current line exceeds the maxWidth,
            # We don't append it and instead distribute spaces
            # len(cur) is the minimum number of spaces needs to be inserted to the current line
            # e.g. cur contains 3 words, if we wanna add one more word to the current line,
            # current line will contain 4 words, but need to add spaces between words,
            # so "word word word word" is 4 words 3 spaces.
            if num_of_letters + len(w) + len(cur) > maxWidth:

                print(f'    maxWidth - num_of_letter: {maxWidth - num_of_letters}')

                # maxWidth - num_of_letters is the number of spaces to insert to the current line
                for i in range(maxWidth - num_of_letters):

                    print(f'      i % (len(cur) - 1 or 1): {i % (len(cur) - 1 or 1)}')

                    # If there are 3 words in the current line, we append spaces to the
                    # end of first 2 words. len(cur): 3, len(cur) - 1: 2, so
                    # i % (len(cur) - 1) alternates (0, 1, 0, 1, 0, ...)

                    # We can assing more spaces to the left
                    # because this alternation starts at 0, which is the most left

                    # When len(cur) is 1, i % (len(cur) - 1) is i % 0, but
                    # you cannot use 0 at the right side of modulo %
                    # When len(cur) is 1, we wanna append as many spaces as possible
                    # to the right side of the single word, so we just need to do
                    # cur[0] += ' ', cur[0] += ' ', ...
                    # i % 1 allows us to have 0 % 0: 0, 1 % 0: 0, 2 % 0: 0,...
                    # (x or y) will be, (0 or 1): 1, (1 or 1): 1, (2 or 1): 2, ...
                    cur[i % (len(cur) - 1 or 1)] += ' '

                # Current line became maxWidth with spaces so add it to the answer
                res.append(''.join(cur))

                print(f'    cur: {cur}, len("".join(cur)): {len("".join(cur))}')

                # Current line finished, so reset the current list of words and
                # current total number of characters in a line
                cur, num_of_letters = [], 0

            cur += [w]

            num_of_letters += len(w)

            print(f'  cur: {cur}, len(cur): {len(cur)} num_of_letters: {num_of_letters}')

        # Python string ljust(value) makes a string to the length of the value
        # and move the string to the left and append space to the right until
        # it reaches the length of the value
        # e.g. 'test'.ljust(5): 'test '
        return res + [' '.join(cur).ljust(maxWidth)]


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
ans = Solution().fullJustify(words, maxWidth)
for row in ans:
    print(row)
