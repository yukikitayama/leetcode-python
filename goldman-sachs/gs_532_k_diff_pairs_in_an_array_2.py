"""
"""


from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = 1
        ans = 0
        while left < len(nums) and right < len(nums):
            if left == right or nums[right] - nums[left] < k:
                right += 1

            elif nums[right] - nums[left] > k:
                left += 1

            else:
                left += 1
                ans += 1
                while left < len(nums) and nums[left] == nums[left - 1]:
                    left += 1
        return ans


"""
- Time is O(nlogn) for sort and O(n) for two pointers
- Space is O(n) for sort
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

