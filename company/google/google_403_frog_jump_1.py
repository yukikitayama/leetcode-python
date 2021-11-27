"""
stones = [0,1,3,5,6,8,12,17]

index: 0, stones[index]: 0, last jump: 0, current jump: 1 because we assumes the first jump must be 1 unit. jump_to: 1
index: 1, stones[index]: 1, current jump: last jump + 1 = 1 + 1 = 2, jump_to: 3
index: 2, stones[index]: 3, current jump: last jump = 2, jump_to: 5,
index: 3, stones[index]: 5, current jump: last jump + 1 = 2 + 1 = 3, jump_to: 8
index: 5, stones[index]: 8, current jump: last jump + 1 = 3 + 1 = 4, jump_to: 12,
index: 6, stones[index]: 12, current jump: last jump + 1 = 4 + 1 = 5, jump_to: 17

- Brute force with recursion function
"""


from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:

        def can_cross(stones, ind, jumpsize):
            for i in range(ind + 1, len(stones)):
                gap = stones[i] - stones[ind]

                print(f'gap: {gap}')

                # if jumpsize - 1 <= gap <= jumpsize + 1:
                if gap in [jumpsize - 1, jumpsize, jumpsize + 1]:

                    # print(f'  jumpsize: {jumpsize}, gap: {gap}, ind: {ind}, i: {i}')
                    print(f'  i: {i}, jumpsize: {jumpsize}')

                    if can_cross(stones, i, gap):
                        return True

            return ind == len(stones) - 1

        return can_cross(stones, 0, 0)


# stones = [0,1,3,5,6,8,12,17]
stones = [0,1,2,3,4,8,9,11]
print(Solution().canCross(stones))


