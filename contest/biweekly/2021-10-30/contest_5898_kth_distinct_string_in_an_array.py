"""
- counter
- iterate enumerate arr
  - if counter value is 1 and index + 1 is k, return the char
- Time is O(n)
"""


from typing import List
import collections


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = collections.Counter(arr)

        num = 0
        for i, char in enumerate(arr):

            if c[char] == 1:
                num += 1

            if c[char] == 1 and num == k:
                return char

        return ''


arr = ["d", "b", "c", "b", "c", "a"]
k = 2
arr = ["aaa","aa","a"]
k = 1
arr = ["a","b","a"]
k = 3
print(Solution().kthDistinct(arr, k))
