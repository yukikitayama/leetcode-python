"""
dp(left, right)
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        """Stack"""
        stack = []
        ans = 0

        for i in range(len(s)):

            if stack and stack[-1] == "b" and s[i] == "a":
                stack.pop()
                ans += 1

            else:
                stack.append(s[i])

        return ans

    def minimumDeletions1(self, s: str) -> int:
        """Simulation"""
        count_a = [0] * len(s)
        count_b = [0] * len(s)

        c_a = 0
        for i in range(len(s) - 1, -1, -1):
            count_a[i] = c_a
            if s[i] == "a":
                c_a += 1

        c_b = 0
        for i in range(len(s)):
            count_b[i] = c_b
            if s[i] == "b":
                c_b += 1

        # print(s)
        # print(count_a)
        # print(count_b)

        ans = len(s)
        for i in range(len(s)):
            ans = min(
                ans,
                count_a[i] + count_b[i]
            )

        return ans