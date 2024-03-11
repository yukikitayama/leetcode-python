"""
[("a", 1)]
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i in range(len(s)):

            if stack and s[i] == stack[-1][0]:

                ch, count = stack.pop()
                count += 1

                if count == k:
                    continue
                else:
                    stack.append((ch, count))

            else:
                stack.append((s[i], 1))

        ans = []
        while stack:
            ch, count = stack.pop()
            ans.append(ch * count)

        ans.reverse()

        return "".join(ans)
