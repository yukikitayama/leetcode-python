"""
- Top down dynamic programming with memoization and binary search
- memo storing -1 or 1 works, but memo storing True or False gives TLE. I don't know why.
- memo[index][jumpsize] represent from index with jumpsize of the last jumpsize whether it can reach the last index
"""


from typing import List
import bisect


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = [[-1] * len(stones) for _ in range(len(stones))]

        def binary_search(a, x, start, end):
            i = bisect.bisect_left(a, x, start, end)
            if i != len(a) and a[i] == x:
                return i
            else:
                return -1

        def can_cross(stones, ind, jumpsize, memo):
            print(f'In can_cross: ind: {ind}, jumpsize: {jumpsize}')

            if memo[ind][jumpsize] >= 0:
                print(f'  Memoization with ind: {ind}, jumpsize: {jumpsize}')
                return memo[ind][jumpsize]

            ind1 = binary_search(stones, stones[ind] + jumpsize, ind + 1, len(stones))
            # print(f'  ind1: {ind1}')
            if ind1 >= 0 and can_cross(stones, ind1, jumpsize, memo) == 1:
                memo[ind][jumpsize] = 1
                return 1

            ind2 = binary_search(stones, stones[ind] + jumpsize - 1, ind + 1, len(stones))
            # print(f'  ind2: {ind2}')
            if ind2 >= 0 and can_cross(stones, ind2, jumpsize - 1, memo) == 1:
                memo[ind][jumpsize - 1] = 1
                return 1

            ind3 = binary_search(stones, stones[ind] + jumpsize + 1, ind + 1, len(stones))
            # print(f'  ind3: {ind3}')
            if ind3 >= 0 and can_cross(stones, ind3, jumpsize + 1, memo) == 1:
                memo[ind][jumpsize + 1] = 1
                return 1

            memo[ind][jumpsize] = 1 if ind == len(stones) - 1 else 0

            if ind == len(stones) - 1:
                print(f'  Reached the last index')

            print(f'ind: {ind}, stones[ind]: {stones[ind]}, jumpsize: {jumpsize}, '
                  f'jumpsize choices: ['
                  f'{stones[ind] + jumpsize - 1}, '
                  f'{stones[ind] + jumpsize}, '
                  f'{stones[ind] + jumpsize + 1}], '
                  f'ind1: {ind1}, ind2: {ind2}, ind3: {ind3}, '
                  f'memo[ind][jumpsize]: {memo[ind][jumpsize]}')

            return memo[ind][jumpsize]

        return can_cross(stones, 0, 0, memo) == 1


stones = [0,1,3,5,6,8,12,17]  # True
# stones = [0,1,2,3,4,8,9,11]  # False
print(Solution().canCross(stones))


