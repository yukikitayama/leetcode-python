class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for i in range(len(s)):

            if stack and abs(ord(stack[-1]) - ord(s[i])) == 32:
                stack.pop()
                # No append
                continue

            stack.append(s[i])

        return "".join(stack)

    def makeGood1(self, s: str) -> str:
        stack = []

        for i in range(len(s)):

            if stack and stack[-1] != s[i] and stack[-1].lower() == s[i].lower():
                stack.pop()
                # No append
                continue

            stack.append(s[i])

        return "".join(stack)
