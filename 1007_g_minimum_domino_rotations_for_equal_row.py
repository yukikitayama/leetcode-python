from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        def check(x):
            rotations_a = rotations_b = 0
            for i in range(n):

                # Both top and bottom do not have x,
                # so it's impossible to make a row of x in either top and bottom
                if tops[i] != x and bottoms[i] != x:
                    return -1

                # Because of the first if statement, it's guaranteed that
                # bottoms[i] is x with below
                elif tops[i] != x:
                    rotations_a += 1

                elif bottoms[i] != x:
                    rotations_b += 1

            return min(rotations_a, rotations_b)

        n = len(tops)

        rotations = check(tops[0])

        # We need also to check bottom first element,
        # because sometimes, bottoms[0] has the number for all rows,
        # but by chance tops[0] does not

        # If one could make all elements in A or B equal to A[0]
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        # If one could make all elements in A or B equal to B[0]
        else:
            return check(bottoms[0])


"""
Time complexity
Let n be the length of tops and bottoms.
O(n) because only once for loop works

Space complexity
O(1) because we don't include tops ad bottoms
"""


tops = [
    1,2,1,1,1,2,2,2
]
bottoms = [
    2,1,2,2,2,2,2,2
]
# answer: 1 by rotation 2nd element
print(Solution().minDominoRotations(tops, bottoms))
