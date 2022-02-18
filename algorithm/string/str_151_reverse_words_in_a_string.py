import collections


class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s) - 1

        # Find start and end index after removing spaces
        while left < right and s[left] == ' ':
            left += 1

        while left < right and s[right] == ' ':
            right -= 1

        list_of_words = collections.deque()
        curr_word = []

        while left <= right:
            if s[left] == ' ' and curr_word:
                word = ''.join(curr_word)

                # By appending from left, first word from s will be later in the output list
                list_of_words.appendleft(word)
                # Reset
                curr_word = []

            elif s[left] != ' ':
                curr_word.append(s[left])

            left += 1

        # Remaining
        word = ''.join(curr_word)
        list_of_words.appendleft(word)

        # print(f'list_of_words: {list_of_words}')

        # Insert one space between words and connect
        return ' '.join(list_of_words)


if __name__ == '__main__':
    s = "the sky is blue"
    print(Solution().reverseWords(s))
