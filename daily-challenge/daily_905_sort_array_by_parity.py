from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:

            # even numbers come earlier than odd numbers
            # even number % 2 is 0, so if nums[left] % 2 is 1
            # and bigger than nums[right] % 2's 0, swap to corrent them
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]

            # If current left is correctly even, go to next
            if nums[left] % 2 == 0:
                left += 1

            # If current right correctly odd, go to next
            if nums[right] % 2 != 0:
                right -= 1

        return nums


if __name__ == '__main__':
    nums = [3, 1, 2, 4]
    print(Solution().sortArrayByParity(nums))
