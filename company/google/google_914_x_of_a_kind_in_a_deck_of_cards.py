"""
- counter
- values are all the same, and more than or equal to 2
"""


from typing import List
import math
import collections
import functools


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        vals = collections.Counter(deck).values()
        return functools.reduce(math.gcd, vals) >= 2


if __name__ == '__main__':
    deck = [1, 2, 3, 4, 4, 3, 2, 1]
    deck = [1,1,2,2,2,2]
    print(Solution().hasGroupsSizeX(deck))
