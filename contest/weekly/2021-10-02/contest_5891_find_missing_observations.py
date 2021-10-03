"""
rolls = [3,2,4,3], mean = 4, n = 2
(3 + 2 + 4 + 3 + a + b) / 6 = 4
(12 + a + b) / 6 = 4
12 + a + b = 24
a + b = 12
a: 6, b: 6

rolls = [1,5,6], mean = 3, n = 4
(1 + 5 + 6 + a + b + c) / 7 = 3
12 + a + b + c = 21
a + b + c = 9
a: 3, b: 3, c: 3

rolls = [1,2,3,4], mean = 6, n = 4
(1 + 2 + 3 + 4 + a + b + c + d) / 8 = 6
10 + a + b + c + d = 48
a + b + c + d = 38
38 / 4 = quotient: 9, remainder: 2
"""

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sum_m = sum(rolls)
        num_total = m + n
        sum_n = mean * num_total - sum_m

        quotient, remainder = divmod(sum_n, n)

        # print(f'sum_n: {sum_n}, quotient: {quotient}, remainder: {remainder}')

        if 0 < quotient <= 6 and remainder == 0:
            return [quotient] * n
        if 0 < quotient < 6 and remainder != 0:
            ans = [quotient] * n
            # ans[0] += remainder
            i = 0
            while remainder > 0:
                if ans[i] < 6:
                    ans[i] += 1
                    remainder -= 1
                    i += 1
            return ans

        else:
            return []


rolls = [3,2,4,3]
mean = 4
n = 2
# Output: [6,6]
rolls = [1,5,6]
mean = 3
n = 4
# Output: [2,3,2,2]
rolls = [1,2,3,4]
mean = 6
n = 4
# Output: []
rolls = [1]
mean = 3
n = 1
# Output: [5]
# rolls = [3,5,3]
# mean = 5
# n = 3
# Output: []
rolls = [4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5]
mean = 4
n = 40
# Expected: [4,4,4,4,4,4,5,5,4,4,4,5,4,4,4,4,4,4,4,4,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5]
print(Solution().missingRolls(rolls, mean, n))

