"""
"""


from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        def get_factors(n, i, combination, ans):

            while i * i <= n:

                quotient, remainder = divmod(n, i)

                if remainder == 0:

                    ans.append(combination + [i, quotient])

                    get_factors(quotient, i, combination + [i], ans)

                i += 1

            return ans

        return get_factors(n, 2, [], [])


n = 1
n = 12
# n = 37
# n = 2
# n = 32
# Output: [[2,16],[4,8],[2,2,8],[2,4,4],[2,2,2,4],[2,2,2,2,2]]
print(Solution().getFactors(n))





