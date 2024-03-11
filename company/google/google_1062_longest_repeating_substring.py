"""
Save substrings in hashset
"""


class Solution:
    def search(self, mid, n, s):

        # print(f"search, mid: {mid}")

        seen = set()

        for start in range(n - mid + 1):
            tmp = s[start:start + mid]

            # print("  ", tmp)

            if tmp in seen:
                return start
            seen.add(tmp)
        return -1

    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)

        # ?
        left = 1
        # ?
        right = n

        while left <= right:

            mid = (left + right) // 2

            # print(f"left: {left}, mid: {mid}, right: {right}")

            # If found duplicated substrings
            if self.search(mid, n, s) != -1:
                # Make substring longer
                left = mid + 1

            # If not found
            else:
                # Make substring shorter
                right = mid - 1

        return left - 1