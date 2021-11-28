class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):

            if s[i] == ']':
                decoded_string = []

                while stack[-1] != '[':
                    decoded_string.append(stack.pop())

                # pop [ from the stack
                stack.pop()
                base = 1
                k = 0
                # Get the number k
                while len(stack) != 0 and stack[-1].isdigit():
                    k = k + int(stack.pop()) * base
                    base *= 10

                while k != 0:
                    for j in range(len(decoded_string) - 1, -1, -1):
                        stack.append(decoded_string[j])
                    k -= 1

            else:
                stack.append(s[i])

        # result = []
        # for i in range(len(stack) - 1, -1, -1):
        #     result.append(stack.pop())
        # print(stack)

        # return ''.join(result)
        return ''.join(stack)


s = "3[a]2[bc]"
s = "3[a2[c]]"
s = "2[abc]3[cd]ef"
print(Solution().decodeString(s))
