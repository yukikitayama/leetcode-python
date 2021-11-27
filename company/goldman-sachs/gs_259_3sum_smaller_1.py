from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        if len(nums) < 3:
            return 0

        nums.sort()
        ans = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    sum_ = nums[i] + nums[j] + nums[k]
                    if sum_ < target:
                        ans += 1
                    else:
                        break

        return ans


nums = [-2,0,1,3]
target = 2
print(Solution().threeSumSmaller(nums, target))
