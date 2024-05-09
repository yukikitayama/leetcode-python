"""
Prefix sum
arr: [1, 3, 5]
prefix sum: [0, 1, 4, 9]
  1 - 0 (o - e), [1]
  4 - 1 (e - o) = 3, [3]
  9 - 0 (o - e), [1, 3, 5]
  9 - 4 (o - e) = 5, [5]
o - o: 5 - 3 = 2
e - e: 4 - 2 = 2
Hashmap
  k: prefix sum
  v: index
  {
    0: -1,
    1: 0,
    4: 1,
    9: 2
  }
  k: diff,
  v: count
  {
    even: 2,
    odd: 1
  }
"""

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        prefix_sum = 0
        counter = {
            0: 1,
            1: 0
        }

        ans = 0
        MOD = 10 ** 9 + 7

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum % 2 == 0:
                ans = (ans + counter[1]) % MOD
                counter[0] += 1

            elif prefix_sum % 2 != 0:
                ans = (ans + counter[0]) % MOD
                counter[1] += 1

        return ans