"""
- Try all the integers which are n % i == 0
- Backtrack these integers to make combinations

Result
- TLE
"""


from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        if n < 2:
            return []

        factors = [i for i in range(2, n) if n % i == 0]

        # print(f'factors: {factors}')

        ans = []

        def backtracking(curr_list, curr_product, index):

            # print(f'curr_list: {curr_list}')

            if curr_product > n:
                return

            if curr_product == n:
                ans.append(curr_list[:])
                return

            for i in range(index, len(factors)):
                curr_list.append(factors[i])
                curr_product *= factors[i]

                backtracking(curr_list, curr_product, i)

                curr_list.pop()
                curr_product //= factors[i]

        backtracking([], 1, 0)
        return ans


n = 1
# n = 12
n = 37
n = 2
n = 32
# Output: [[2,16],[4,8],[2,2,8],[2,4,4],[2,2,2,4],[2,2,2,2,2]]
print(Solution().getFactors(n))





