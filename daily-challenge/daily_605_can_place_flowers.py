from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):

            if (
                # Current position is empty
                flowerbed[i] == 0
                # current position is leftmost or left is empty
                and (i == 0 or flowerbed[i - 1] == 0)
                # Current position is rightmost or right is empty
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1
                if n <= 0:
                    return True

        return n <= 0


if __name__ == '__main__':
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    # n = 2
    # flowerbed = [1, 0, 1, 0, 1, 0, 1]
    # n = 0
    flowerbed = [1]
    n = 1
    print(Solution().canPlaceFlowers(flowerbed, n))
