"""
- 3 - 1 = 2
  - 1 + 2 = 3
"""


from typing import List
import collections


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        counter = collections.Counter(nums)

        # Not for num in nums, because it will double-count
        # Iterate counter key for unique pair
        for num in counter:

            if k > 0 and num + k in counter:
                ans += 1

            elif k == 0 and counter[num] > 1:
                ans += 1

            print(f'num: {num}, ans: {ans}')

        return ans


if __name__ == '__main__':
    nums = [3, 1, 4, 1, 5]
    k = 2
    print(Solution().findPairs(nums, k))
