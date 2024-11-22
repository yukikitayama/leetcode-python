"""
[0,0,0],
[0,0,1],
[1,1,0]

[1,1,0],
[1,1,1],
[0,0,0]

"""

from typing import List
import collections


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = collections.Counter()
        for row in matrix:
            pattern = "".join("T" if num == row[0] else "F" for num in row)
            counter[pattern] += 1
        return max(counter.values())