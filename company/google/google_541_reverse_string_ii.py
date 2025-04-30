"""
k: 2
first 2 characters for every 4 characters
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = list(s)
        for i in range(0, len(ans), 2 * k):
            ans[i:i + k] = reversed(ans[i: i + k])
            # print(ans)

        return "".join(ans)