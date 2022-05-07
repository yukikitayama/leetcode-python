"""
- Use stack
- Use i < j < k
- Push possible nums[k] to stack
- Make min array for nums[i]
- Use nums[j] to identify i
"""


from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        # Edge case
        if len(nums) < 3:
            return False

        # Make min so far array
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        for i in range(1, len(nums)):
            min_array[i] = min(min_array[i - 1], nums[i])

        # print(f'min_array: {min_array}')

        stack = []

        # Iterate backward to find nums[k]
        for j in range(len(nums) - 1, -1, -1):

            # print(f'j: {j}, nums[j]: {nums[j]}, min_array[j]: {min_array[j]}')

            # min_array[j] needs to be 1 of 132, and nums[j] needs to be 3 of 132
            # so if nums[j] is smaller or equal to min_array[j], it won't be 13, so skip it
            # we don't even need to think about nums[k]
            if nums[j] <= min_array[j]:
                continue

            # A number from stack will be 2 of 132, so if stack number is smaller or equal to
            # min_array number. we remove it
            while stack and stack[-1] <= min_array[j]:
                stack.pop()

            # Because of all the code above, stack number is guaranteed to be bigger than min_array
            # number, if stack is not empty.
            if stack and stack[-1] < nums[j]:
                return True

            stack.append(nums[j])

            # print(f'  stack: {stack}')

        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    nums = [3, 1, 4, 2]
    print(Solution().find132pattern(nums))
