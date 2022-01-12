class Solution:
    def reorderSpaces(self, text: str) -> str:

        # Count the number of words in text
        words = text.split()
        # print(f'Words in text: {words}')

        num_words = len(words)
        # print(f'Number of words: {num_words}')

        # Count number of spaces that text has
        num_spaces = text.count(' ')
        # print(f'Number of spaces: {num_spaces}')

        num_spaces_between = 0 if num_words == 1 else num_spaces // (num_words - 1)
        # print(f'Number of spaces between: {num_spaces_between}')

        ans = ''
        for i, word in enumerate(words):
            ans += word
            if i != (len(words) - 1):
                ans += (' ' * num_spaces_between)
                num_spaces -= num_spaces_between

        # print(f'num_spaces: {num_spaces}')

        if num_spaces:
            ans += (' ' * num_spaces)

        return ans


if __name__ == '__main__':
    text = "  this   is  a sentence "
    # It has 9 spaces
    text = " practice   makes   perfect"
    # "practice   makes   perfect "
    text = 'a'
    print(f'"{Solution().reorderSpaces(text)}"')
