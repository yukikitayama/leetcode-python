"""
- Use stack
"""


class Solution:
    def makeGood(self, s: str) -> str:

        stack = []

        i = 0

        while i < len(s):

            # print(f'Before stack: {stack}')

            while (
                len(stack) > 0
                and i < len(s)
                and (
                    (s[i].islower() and stack[-1].isupper() and s[i] == stack[-1].lower())
                    or (s[i].isupper() and stack[-1].islower() and s[i].lower() == stack[-1])
                )
            ):
                stack.pop()
                i += 1

            if i < len(s):
                stack.append(s[i])
                i += 1

            # print(f'  After stack: {stack}')

        return ''.join(stack)


if __name__ == '__main__':
    s = 'leEeetcode'
    s = 'abBAcC'
    s = 's'
    s = "XxDFOBKRrkbofdXxeEijJIcCsBikPgfxXFGpKIbSemGivrqqQQRVIgMEPBWpPwbpSCWqWQqwQwcsQqasLwGWlSAQq"
    print(Solution().makeGood(s))
