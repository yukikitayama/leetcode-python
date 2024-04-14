from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = [nums[0]]

        def binary_search(array, target):
            left = 0
            right = len(array) - 1
            while left <= right:
                mid = (left + right) // 2
                if array[mid] == target:
                    return mid
                elif array[mid] > target:
                    right = mid - 1
                elif array[mid] < target:
                    left = mid + 1
            return left

        for i in range(1, len(nums)):

            if nums[i] > stack[-1]:
                stack.append(nums[i])

            else:
                j = binary_search(stack, nums[i])
                stack[j] = nums[i]

            # print(stack)

        return len(stack)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):

            if not stack:
                stack.append(nums[i])

            elif nums[i] > stack[-1]:
                stack.append(nums[i])

            elif nums[i] < stack[-1]:
                j = 0
                while j < len(stack):
                    if stack[j] >= nums[i]:
                        stack[j] = nums[i]
                        break
                    j += 1

            # print(stack)

        return len(stack)

    def lengthOfLIS1(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for right in range(1, len(nums)):
            for left in range(right):
                if nums[right] > nums[left]:
                    dp[right] = max(dp[right], 1 + dp[left])

        # print(dp)

        return max(dp)