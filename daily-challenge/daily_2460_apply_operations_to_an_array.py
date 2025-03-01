from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        write_idx = 0

        for i in range(len(nums)):

            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

            if nums[i] != 0:
                nums[write_idx], nums[i] = nums[i], nums[write_idx]
                write_idx += 1

        return nums

    def applyOperations2(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        insert_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_idx] = nums[i]
                insert_idx += 1

        while insert_idx < len(nums):
            nums[insert_idx] = 0
            insert_idx += 1

        return nums

    def applyOperations1(self, nums: List[int]) -> List[int]:
        ans = []
        counter = 0

        for i in range(len(nums) - 1):

            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

            # If current is 0, increment counter
            if nums[i] == 0:
                counter += 1
            # If current is not 0, append it to ans
            elif nums[i] != 0:
                ans.append(nums[i])

        # If last element is 0, increment couter
        if nums[-1] == 0:
            counter += 1

        # If last element is not 0, append it to ans
        elif nums[-1] != 0:
            ans.append(nums[-1])

        return ans + [0] * counter