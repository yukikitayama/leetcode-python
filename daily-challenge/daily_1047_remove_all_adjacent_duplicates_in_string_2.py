class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        i = 0

        while i < len(s):

            if len(stack) == 0:
                stack.append(s[i])
                i += 1
            elif len(stack) and stack[-1] == s[i]:
                stack.pop()
                i += 1
            elif len(stack) and stack[-1] != s[i]:
                stack.append(s[i])
                i += 1

        return ''.join(stack)


if __name__ == '__main__':
    s = 'abbaca'
    print(Solution().removeDuplicates(s))
