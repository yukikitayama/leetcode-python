"""
- find a combination of square numbers that sum up to n
- The combination needs to be the least number
- We can reuse the same square numbers


n: 4
k = [1, 4]
n - k: {4 - 1, 4 - 4} = {3, 0}
numSquares(4), min(numSquares(4 - 1) + 1): min(numSquares(3) + 1)
  numSquares(3), min()
"""


import math


class Solution:
    def numSquares(self, n: int) -> int:

        square_nums = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]

        print(f'square_nums: {square_nums}, int(math.sqrt(n)) + 1: {int(math.sqrt(n)) + 1}')

        def minNumSquares(k):

            print(f'In minNumSquares, k: {k}')

            if k in square_nums:
                print(f'  found k: {k} in square_nums so return 1')
                return 1

            min_num = float('inf')

            for square in square_nums:

                print(f'  square: {square}, k: {k}')

                if square > k:
                    break

                # minNumSquares eventually returns 1
                # +1 because, with the current square (+1),
                # the below finds the number of square numbers for the rest (k - square)
                new_num = minNumSquares(k - square) + 1

                print(f'    new_num: {new_num}')

                min_num = min(min_num, new_num)

            print(f'return min_num: {min_num}')

            return min_num

        return minNumSquares(n)



# Least number of perfect square numbers that sum to n
# 2 = 1 + 1
# print(Solution().numSquares(2))

print(Solution().numSquares(6))  # 1 + 1 + 4 = 6, so needs 3 perfect square numbers
# print(Solution().numSquares(12))  # 4 + 4 + 4 = 6, so needs 3 perfect square numbers

