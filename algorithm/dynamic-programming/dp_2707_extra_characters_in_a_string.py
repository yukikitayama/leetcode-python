from typing import List
import functools


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        dictionary_set = set(dictionary)
        n = len(s)

        @functools.lru_cache(maxsize=None)
        def dp(start):

            # Base case: No more characters left, so no need to loop up and no need to remove extra characters
            if start == n:
                return 0

            # Case 1: Remove current character (+1 at the end) and go to the next character (start + 1)
            ans = dp(start + 1) + 1

            # Case 2: Find the substring from start to end
            for end in range(start, n):
                curr = s[start:end + 1]

                if curr in dictionary_set:

                    # Take min of case 1 or 2
                    ans = min(ans, dp(end + 1))

            return ans

        return dp(0)

