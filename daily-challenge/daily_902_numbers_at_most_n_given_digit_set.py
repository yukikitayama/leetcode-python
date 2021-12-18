"""
Result
- Start: 8:25
- End: 9:17
- Solved: 1
- Saw solution: 1
- Optimized: 1

-
Constrains
- digits only contains 1 to 9. It doesn't contain 0
- ALl the values in digits are unique

Example
Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation:
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
100 has 3 digits
N: 100, K: 3, D.length: 4,

- Length: 1
  - 1, 3, 5, 7
- Length: 2
  - 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77
"""


from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        k = len(s)

        # For numbers whose digit length is equal to the digit length of n
        # +[1] is base case
        # Constraints says 1 <= n, and digits from 1
        dp = [0] * k + [1]

        # print(f'digits: {digits}')
        # print(f'n: {n}, s: {s}, k: {k}')
        # print(f'dp: {dp}')

        for i in range(k - 1, -1, -1):

            # print(f'  i: {i}')

            for d in digits:

                # print(f'    d: {d}, s[i]: {s[i]}')

                if d < s[i]:

                    dp[i] += len(digits) ** (k - i - 1)

                elif d == s[i]:

                    dp[i] += dp[i + 1]

        # print(f'dp: {dp}')

        # range(1, k) because of numbers whose digit length is less than digit length of n
        # len(digits) ** i because values in digits are unique and digits doesn't contain 0
        # so len(digits) ** i can calculate all the combination
        summed = 0
        for i in range(1, k):
            v = len(digits) ** i

            # print(f'v: {v}')

            summed += v
        # print(f'summed: {summed}')

        return dp[0] + sum(len(digits) ** i for i in range(1, k))


digits = ["1","3","5","7"]
n = 100
digits = ['1', '2']
n = 12
print(Solution().atMostNGivenDigitSet(digits, n))
