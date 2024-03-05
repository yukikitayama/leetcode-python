from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):

            if flowerbed[i] == 0:

                left_empty = i == 0 or flowerbed[i - 1] == 0
                right_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1

                    if count >= n:
                        break

        return count >= n

    def canPlaceFlowers1(self, flowerbed: List[int], n: int) -> bool:

        # Edge
        if n == 0:
            return True

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            n -= 1
            return n == 0

        for i in range(len(flowerbed)):

            # Edge
            if i == 0 and i + 1 < len(flowerbed) and flowerbed[i + 1] != 1 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

            if i - 1 > 0 and i + 1 < len(flowerbed) and flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1 and flowerbed[
                i] == 0:
                flowerbed[i] = 1
                n -= 1

            # Edge
            if i == len(flowerbed) - 1 and i - 1 > 0 and flowerbed[i - 1] != 1 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

            if n == 0:
                break

        return n == 0
