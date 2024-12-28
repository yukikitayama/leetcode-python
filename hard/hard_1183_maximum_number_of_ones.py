"""
height: 9
sideLength: 3
r: 0
-r for removing current position so far
-1 for removing itself
(height - r - 1) // sideLength = (9 - 0 - 1) // 3 = 8 // 3 = 2

height: 9
sideLength: 3
r: 1
(9 - 1 - 1) // 3 = 7 // 3
"""


class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        count = []
        for r in range(sideLength):
            for c in range(sideLength):
                num = (
                    (1 + (width - c - 1) // sideLength)
                    * (1 + (height - r - 1) // sideLength)
                )
                count.append(num)
        count.sort(reverse=True)
        return sum(count[:maxOnes])