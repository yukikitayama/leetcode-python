"""
Base case return 1 as length of itself
Otherwise return max length

dp(0)
  - skip 0 then dp(1)
    - skip 1 then dp(2)
    - include 1 then dp(2)
  - include 0 the dp(1)
    - skip 1 then dp(2)
    - include 1 then dp(2)
"""

from typing import List
import functools


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort()

        @functools.lru_cache(maxsize=None)
        def dp(curr):

            # Base is 1 to include itself to the chain
            ans = 1

            for i in range(curr + 1, len(pairs)):
                # Chain formulation condition
                if pairs[curr][1] < pairs[i][0]:
                    # +1 to include itself
                    ans = max(ans, dp(i) + 1)

            return ans

        ans = 0

        for i in range(len(pairs)):
            ans = max(ans, dp(i))
        return ans


if __name__ == "__main__":
    pairs = [[1, 2], [2, 3], [3, 4]]
    pairs = [[1, 2], [7, 8], [4, 5]]
    print(Solution().findLongestChain(pairs))

