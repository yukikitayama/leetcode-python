"""
- Stack
  - Count stack
    - It needs to create
  - String stack
    - Current characters to be multiplied is not in stack
    - Decoded characters are in stack
"""


class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        current_string = ''
        k = 0

        for i, char in enumerate(s):

            print(f'  char: {char}, i: {i}')

            if char.isdigit():

                # inter could be more than 9, but get integer one by one
                # so when multiple integers come in, it needs to create multiple digits integer
                k = k * 10 + int(char)

            elif char == '[':

                count_stack.append(k)
                string_stack.append(current_string)
                # Reset current string and current integer
                current_string = ''
                k = 0

            elif char == ']':

                decoded_string = string_stack.pop()

                current_k = count_stack.pop()
                while current_k > 0:
                    decoded_string += current_string
                    current_k -= 1

                current_string = decoded_string

            else:
                current_string += char

            print(f'    count_stack: {count_stack}')
            print(f'    string_stack: {string_stack}')
            print(f'    current_string: {current_string}')
            print(f'    k: {k}')

        return current_string


s = "3[a]2[bc]"
# s = "10[a]2[bc]"
# s = "3[a2[c]]"
print(Solution().decodeString(s))

