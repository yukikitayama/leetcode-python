from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0

        for log in logs:

            if log not in ["./", "../"]:
                ans += 1

            elif log == "../":
                if ans > 0:
                    ans -= 1

            elif log == "./":
                continue

        return ans

    def minOperations1(self, logs: List[str]) -> int:
        stack = []

        for log in logs:

            if log not in ["./", "../"]:
                stack.append(log)

            elif log == "../":
                if stack:
                    stack.pop()

            elif log == "./":
                continue

        return len(stack)