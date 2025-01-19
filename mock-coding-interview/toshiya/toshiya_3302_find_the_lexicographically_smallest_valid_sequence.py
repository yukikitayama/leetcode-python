"""
Brute force
  maybe TLE

Two pointers
Backtracking
3 choices for each character
  - Use it becuase same character
  - Convert to word2 character becuase different
    - How to know?
  - Skip
    - How to know?

Dynamic programming
  pointer
  backtracking
  smallest answer
"""

from typing import List


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:

        ans = []

        # Recursion
        def dp(p1, p2, converted):

            # p2 at the end, good

            # p1 at the end, but p2 not at the end, not good

            # same character
            if word1[p1] == word2[p2]:
                res1 = dp(p1 + 1, p2 + 1, convert)

            # different character, convert
            elif word1[p1] != word2[p2] and not converted:
                res2 = dp(p1 + 1, p2 + 1, True)

            # different character skip
            elif word1[p1] != word2[p2]L
                res3 = dp(p1 + 1, p2, convert)

            min_ind = min(res1, res2, res3)

            ans.append(min_ind)

            return

        dp(0, 0, False)

        return ans