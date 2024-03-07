"""
two pointers?
dp?
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last = {s[i]: i for i in range(len(s))}

        ans = []

        right = 0
        left = 0

        for i in range(len(s)):

            # Expand window to contain current character
            right = max(right, last[s[i]])

            # print(f"i: {i}, left: {left}, right: {right}")

            if i == right:
                ans.append(i - left + 1)
                # Reset left to start a new partition
                left = i + 1

        return ans