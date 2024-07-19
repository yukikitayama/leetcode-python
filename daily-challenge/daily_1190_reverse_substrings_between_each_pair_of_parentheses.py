"""
"(" resets current chunk
")" pops from stack top, reverse, place back to stack by concatanate
otherwise, concatenate current character with stock top

Appened reversed curr
[ed]
[ed, et]
[ed, et, oc]
)
[ed, et], oc -> co, [ed, etco]
[ed, etco], ), etco -> octe, [ed, octe]
[ed, octe, el], edocte -> etcode
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        """T: O(N), S: O(N)"""
        n = len(s)
        opens = []
        wormhole = [0] * n

        for i in range(n):
            if s[i] == "(":
                opens.append(i)
            elif s[i] == ")":
                j = opens.pop()
                wormhole[i] = j
                wormhole[j] = i

        ans = []
        curr = 0
        direction = 1

        while curr < n:

            if s[curr] in "()":
                curr = wormhole[curr]
                direction *= -1

            else:
                ans.append(s[curr])

            curr += direction

        return "".join(ans)

    def reverseParentheses2(self, s: str) -> str:
        ans = []
        opens = []
        for ch in s:
            if ch == "(":
                opens.append(len(ans))

            elif ch == ")":
                start = opens.pop()
                ans[start:] = ans[start:][::-1]

            else:
                ans.append(ch)

            # print(ans, opens)

        return "".join(ans)

    def reverseParentheses1(self, s: str) -> str:
        stack = []
        curr = []

        for ch in s:

            if ch == "(":
                if curr:
                    stack.append("".join(curr))
                stack.append(ch)
                curr = []

            elif ch == ")":
                buffer = []
                while stack and stack[-1] != "(":
                    buffer.append(stack.pop())
                # Remove (
                stack.pop()
                buffer.reverse()
                buffer.append("".join(curr))
                curr = []
                rev = "".join(buffer)
                rev = rev[::-1]
                stack.append(rev)

            else:
                curr.append(ch)

            print(stack, curr)

        return stack[0]
