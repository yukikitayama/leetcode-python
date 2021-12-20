import collections
import math
from typing import List


class Solution:
    def calculateEntropy(self, input: List[int]) -> float:
        counter = collections.Counter(input)
        ans = 0
        for count in counter.values():
            p = count / len(input)
            ans += -1 * p * math.log2(p)
        return ans
