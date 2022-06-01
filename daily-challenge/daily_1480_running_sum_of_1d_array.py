from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


class Solution1:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            ans.append(curr)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    # nums = [1, 1, 1, 1, 1]
    print(Solution().runningSum(nums))
