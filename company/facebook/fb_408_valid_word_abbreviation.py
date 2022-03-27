"""
- Extract numbers from abbr
- Iterate characters in word by extracted numbers
- Two pointers
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w_idx = 0
        a_idx = 0

        w_len = len(word)
        a_len = len(abbr)

        while w_idx < w_len and a_idx < a_len:

            if word[w_idx] == abbr[a_idx]:
                w_idx += 1
                a_idx += 1

            # Leading 0 is not allowed
            elif abbr[a_idx] == '0':
                return False

            # If encountering non-0-leading number
            elif abbr[a_idx].isnumeric():

                # Number could be more than 9,
                # so iterate to make a complete number
                i = a_idx
                while i < a_len and abbr[i].isnumeric():
                    i += 1
                # Here i points at non-number
                # In slicing end i is exclusive
                # Move word index by the number
                w_idx += int(abbr[a_idx:i])
                # Move abbr index to the next start index
                a_idx = i

            else:
                return False

        # print(f'w_idx: {w_idx}, a_idx: {a_idx}')

        # When a_idx reaches the end, but w_idx is still in the middle
        # While loop breaks when index >= length, so index == length, not index == (length - 1)
        return w_idx == w_len and a_idx == a_len


if __name__ == '__main__':
    word = "internationalization"
    abbr = "i12iz4n"
    # word = 'apple'
    # abbr = 'a2e'
    print(Solution().validWordAbbreviation(word, abbr))
