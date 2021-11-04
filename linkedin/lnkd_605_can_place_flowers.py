"""
- Iterate from left to right
- If find a place able to plant, decrement n
- Return if n == 0
"""


from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True

        for i in range(len(flowerbed)):

            if (
                    flowerbed[i] == 0
                    and (i == 0 or flowerbed[i - 1] == 0)
                    # i == len(flowerbed) - 1 needs to be first, otherwise index out of bound
                    and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True

        return False


flowerbed = [1,0,0,0,1]
n = 1
flowerbed = [1,0,0,0,1]
n = 2
print(Solution().canPlaceFlowers(flowerbed, n))

