from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        def check(num):
            rotations_top = 0
            rotations_bottom = 0

            for i in range(len(tops)):
                if tops[i] != num and bottoms[i] != num:
                    return -1
                elif tops[i] != num:
                    rotations_top += 1
                elif bottoms[i] != num:
                    rotations_bottom += 1

            return min(rotations_top, rotations_bottom)

        rotations_top = check(tops[0])
        if rotations_top != -1:
            return rotations_top
        else:
            return check(bottoms[0])