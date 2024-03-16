"""
- Hashmap and two pointers?
"""


from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {0: -1}
        ans = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            # If count already exist in map, don't update map
            # It allows to keep minimum index so far for a count
            if count in map:
                ans = max(ans, i - map[count])
            else:
                map[count] = i
        return ans