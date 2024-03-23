"""
Num % value

[1,-10,7,13,6,8], 5
Module
[1, 0, 2, 3, 1, 3]
Sort
[0, 1, 1, 2, 3, 3]
counter: 0

[1,-10,7,13,6,8], value: 7
Module
[1, 3, 0, 6, 6, 1]
Sort
[0, 1, 1, 3, 6, 6]
COunter: 0

T: O(NlogN)
S: O(1)

[3,0,3,2,4,2,1,1,0,4], 5
Module
Same
Sort
[0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
Add
[0, 5, 1, 6, 2, 7, 3, 8, 4, 9]
Ans: 10

[0, 0, 0,]
[0, 5, 10]

Apply module to num
Hashmap
  k: after module num
  v: count
From hashmap create array
  k * v
  decrement v
  continue until hashmap is empty
"""

from typing import List
import collections


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        modulos = []
        for i in range(len(nums)):
            modulos.append(nums[i] % value)

        counter = collections.Counter(modulos)

        # print(counter)

        scan_array = []
        for k, v in counter.items():

            while v > 0:
                # [0: 2]
                scan_array.append(k + (v - 1) * value)
                v -= 1

        # print(scan_array)

        scan_array.sort()

        ans = 0

        for i in range(len(scan_array)):

            if i > 0 and scan_array[i] == scan_array[i - 1]:
                continue

            if scan_array[i] == ans:
                ans += 1
            elif scan_array[i] != ans:
                return ans

        return ans
