"""
- Backtracking
- is_palindrome helper function
- If number of character with odd number of occurrences exceeds 1, no palindromic permutation
  - 1 is fine because it can be middle
"""


from typing import List
import collections


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        n = len(s)
        counter = collections.Counter(s)

        odds = []
        for k, v in counter.items():
            if v % 2 != 0:
                odds.append(k)

        # print(odds)

        # If odd occurrence number is more than 1, impossible to make palindromes
        if len(odds) > 1:
            return []

        def helper(curr):
            """From middle construct palindrome"""

            # Termination for recursion
            if len(curr) == n:
                ans.append(curr)
                return

            for k, v in counter.items():
                if v > 0:
                    # Use the current characters
                    counter[k] -= 2
                    # Construct palindrome from middle to outside
                    helper(k + curr + k)

                    # Backtrack
                    counter[k] += 2

        ans = []
        # If there is one character whose occurrence is 1,
        if len(odds) == 1:
            counter[odds[0]] -= 1
            helper(odds[0])
        else:
            helper('')

        return ans


if __name__ == '__main__':
    s = "aabb"
    # s = "abc"
    print(Solution().generatePalindromes(s))
