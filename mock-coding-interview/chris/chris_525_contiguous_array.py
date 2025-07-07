"""
[0, 1, 0]

counter
  1: X
  0: Y

[0, 1]
[0, -1, 0]

{1: 5, 0: 4}
[0, 1, 1, 1, 1, 1, 0, 0, 0]
increment if 1, decrement if 0
[-1, 0, 1, 2, 3, 4, 3, 2, 1]
iterate
  if current preprocess number in hashmap
    difference between current index and prev index
    take max
  hashmap
    k: preprocess number
    v: min index

"""

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        preprocess = [0]
        curr = 0
        for num in nums:
            curr += 1 if num == 1 else -1
            preprocess.append(curr)

        counter = dict()
        ans = 0
        for i, p in enumerate(preprocess):
            if p in counter:
                ans = max(
                    ans,
                    i - counter[p]
                )

            if p not in counter:
                counter[p] = i

        return ans