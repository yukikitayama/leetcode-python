from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        b1 = None
        b2 = None
        b1N = 0
        b2N = 0
        b2NCons = 0
        maxPick = 0

        for fruit in fruits:
            if fruit == b2:
                b2N, b2NCons = b2N + 1, b2NCons + 1

            elif fruit == b1:
                b1, b2, b1N, b2N, b2NCons = b2, b1, b2N, b1N + 1, 1

            # New fruit, put it into b2, shift b2 to b1, discard b1
            else:
                b1, b2, b1N, b2N, b2NCons = b2, fruit, b2NCons, 1, 1

            maxPick = max(maxPick, b1N + b2N)
        return maxPick


fruits = [1, 2, 3, 2, 2]
fruits = [3,3,3,1,2,1,1,2,3,3,4]
print(Solution().totalFruit(fruits))
