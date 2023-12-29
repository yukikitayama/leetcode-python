"""
If there are single characters, we should delete them first
We should delete characters of appearing twice

First create counter, and then iterate

Combining effect after deleting

'', 3
  a, 3
    ab, 3
      abb, 3
      ab, 2
    a, 2
      ab, 2
      a, 1
  '', 2
    b, 2
      bb, 2
      b, 1
    '', 1
      b, 1
      '', 0

(ab, 2), (b, 1), repeating sub-problems
Memoization
"""

import functools


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(i, last_char, last_char_count, k):
            """Returns an optimized minimum length so far"""

            if k < 0:
                # inf will be gone by min() eventually
                return float("inf")

            if i == len(s):
                # print("i == len(s)")
                return 0

            # If we don't take the current character (delete)
            delete_char = dp(i + 1, last_char, last_char_count, k - 1)

            # If we take the current character and if it's the same as the last character
            if s[i] == last_char:
                # Length increases by 1. e.g. a -> a2, a9 -> a10, a99 -> a100
                if last_char_count in [1, 9, 99]:
                    keep_char = dp(i + 1, last_char, last_char_count + 1, k) + 1
                else:
                    keep_char = dp(i + 1, last_char, last_char_count + 1, k)

            # If we take the current character and if it's different from the last character
            else:
                keep_char = dp(i + 1, s[i], 1, k) + 1

            # Take min of either not taking a character or taking a character
            # print(f"keep_char: {keep_char}, delete_char: {delete_char}")
            return min(keep_char, delete_char)

        return dp(0, "", 0, k)


if __name__ == "__main__":
    s = "aabbaa"
    k = 2
    print(Solution().getLengthOfOptimalCompression(s, k))
