"""
- collections.Counter
- sum up where count is 1
- T: O(N), S: O(N)
"""


from typing import List
import collections


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(k for k, v in collections.Counter(nums).items() if v == 1)


if __name__ == '__main__':
    nums = [1, 2, 3, 2]
    print(Solution().sumOfUnique(nums))
