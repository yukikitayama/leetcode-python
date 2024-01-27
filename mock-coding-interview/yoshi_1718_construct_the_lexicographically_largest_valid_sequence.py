"""
Backtracking,
Sequence length
  n: 3, len: 5 = 1 + (3 - 1) * 2 = 1 + 4 = 5
  n: 4, len: 1 + (4 - 1) * 2 = 1 + 6 = 7
  n: 5, len: 1 + (5 - 1) * 2 = 1 + 8 = 9

"""

from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        ans = [0] * (2 * n - 1)
        seen = set()

        def backtracking(i):

            # If we checked all the integers from 1 to n
            if len(seen) == n:
                return ans

            # If the array already contains numbers > 0, go to the next integer
            if ans[i]:
                return backtracking(i + 1)

            # By iterating from the largest integer, we will create the lexicographically largest array
            for num in range(n, 0, -1):

                if num not in seen:

                    # Dummy
                    if num == 1:
                        j = i
                    # When integer >= 2, get the other index to fill the same number
                    else:
                        j = i + num

                    # If the other number index is in bound and the array positions are not filled yet
                    if j < len(ans) and ans[i] == 0 and ans[j] == 0:

                        ans[i] = num
                        ans[j] = num
                        seen.add(num)

                        res = backtracking(i + 1)

                        if res:
                            return res

                        # Backtrack
                        seen.remove(num)
                        ans[i] = 0
                        ans[j] = 0

        return backtracking(0)


