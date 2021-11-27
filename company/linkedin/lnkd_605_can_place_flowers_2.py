"""
- Modify the input flowerbed in place when putting a new flower
- Decrement the input n in place
- Return whether n is 0 or not
"""


from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True

        for i in range(len(flowerbed)):

            # Out of bound when i is 0
            # Out of bound when i is len(flowerbed) - 1
            if (
                    flowerbed[i] == 0
                    and (i == 0 or flowerbed[i - 1] == 0)
                    and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    break

        # print(f'flowerbed: {flowerbed}')

        return n == 0


flowerbed = [1,0,0,0,1]
n = 1
flowerbed = [1,0,0,0,1]
n = 2
flowerbed = [0]
n = 1
flowerbed = [0, 0, 1, 0, 0]
n = 1
flowerbed = [0,0,0,0,0,1,0,0]
n = 0
print(Solution().canPlaceFlowers(flowerbed, n))

