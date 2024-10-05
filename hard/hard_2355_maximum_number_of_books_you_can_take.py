"""
Monotonic stack
"""

from typing import List


class Solution:
    def maximumBooks(self, books: List[int]) -> int:

        def calculate_sum(l, r):
            # books[r] tells the maximum distance we can go with this available number of books
            # r - l + 1 tells the available distance given l and r
            cnt = min(books[r], r - l + 1)

            return 1 / 2 * (books[r] + books[r] - (cnt - 1)) * cnt

        n = len(books)
        stack = []
        dp = [0] * n

        for i in range(n):

            # Keep monotonically increasing stack
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                popped = stack.pop()
                # print(f"popped: {popped}, i: {i}")

            if not stack:
                dp[i] = calculate_sum(0, i)

            else:
                j = stack[-1]
                dp[i] = dp[j] + calculate_sum(j + 1, i)

            stack.append(i)

        return int(max(dp))