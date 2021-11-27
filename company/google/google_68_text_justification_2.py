class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []

        curr_line = []
        num_of_char = 0

        for word in words:

            if num_of_char + len(word) + len(curr_line) > maxWidth:

                for i in range(maxWidth - num_of_char):
                    curr_line[i % (len(curr_line) - 1 or 1)] += ' '

                line = ''.join(curr_line)
                ans.append(line)

                # Reset
                curr_line = []
                num_of_char = 0

            curr_line += [word]
            num_of_char += len(word)

        # The remaining last line
        line = ' '.join(curr_line).ljust(maxWidth)
        ans.append(line)

        return ans