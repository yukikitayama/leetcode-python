from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            # % 1000 gives number below 1000
            # 1000 * moves the number above 1000
            # += saves the number above 1000
            nums[i] += 1000 * (nums[nums[i]] % 1000)

        for i in range(len(nums)):
            nums[i] //= 1000

        return nums

    def buildArray1(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(nums[num])
        return ans