from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        count = 1

        while i < len(nums):

            # Same number
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    nums.pop(i)

                    # Decrement index because the next number comes at current i because of deletion
                    # But we increment i at the bottom of the while loop, so to avoid skipping
                    i -= 1

            # Different number
            else:
                # Reset count
                count = 1

            # Iterate to next index
            i += 1

        # print(nums)

        return len(nums)


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(Solution().removeDuplicates(nums))
