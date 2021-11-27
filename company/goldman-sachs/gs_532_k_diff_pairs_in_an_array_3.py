"""
- Using counter can avoid duplicate counts
- Iterate keys in counter
  - Increment answer if another key of key + k exist in the counter
  - If k is 0, increment answer if a key has at least two counts, and can form different 0 with
    the two values
"""


from typing import List
import collections


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        counter = collections.Counter(nums)

        for num in counter:
            if k > 0 and num + k in counter:
                ans += 1
            elif k == 0 and counter[num] > 1:
                ans += 1

        return ans


"""
Complexity
- Time is O(n) to iterate keys in counter
- Space is O(n) for counter
"""


nums = [3,1,4,1,5]
k = 2
# 2
nums = [1,2,3,4,5]
k = 1
# 4
nums = [1,3,1,5,4]
k = 0
# 1
nums = [1,2,4,4,3,3,0,9,2,3]
k = 3
# 2
nums = [-1,-2,-3]
k = 1
# 2
print(Solution().findPairs(nums, k))

