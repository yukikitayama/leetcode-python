from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []

        nums.sort()

        for i, num in enumerate(nums):
            if num == target:
                ans.append(i)

        return ans


nums = [1, 2, 5, 2, 3]
target = 2
nums = [1,2,5,2,3]
target = 3
nums = [1,2,5,2,3]
target = 5
nums = [1,2,5,2,3]
target = 4
print(Solution().targetIndices(nums, target))
