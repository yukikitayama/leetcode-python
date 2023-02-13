from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(len(nums) - 1):

            # Even index
            if i % 2 == 0:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

            # Odd index
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

        # print(nums)


if __name__ == "__main__":
    nums = [3, 5, 2, 1, 6, 4]
    print(Solution().wiggleSort(nums))


