"""
Idea
- Replace linear scan with binary search to make things faster
- It's fine because sub is increasing order

Algorithm
-

"""


from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for num in nums[1:]:
            i = bisect.bisect_left(sub, num)

            # If current num is greater than any element in sub
            # bisect_left gives us the last index plust one to insert
            # so i will be len(sub)
            if i == len(sub):
                sub.append(num)

            # If current num is smaller than or equal to an element in sub
            # bisect_left gives us the index to insert which means
            # the current num is firstly smaller than an element
            # so that's the position to replace
            else:
                sub[i] = num

        return len(sub)


nums = [10,9,2,5,3,7,101,18]
nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
print(Solution().lengthOfLIS(nums))

