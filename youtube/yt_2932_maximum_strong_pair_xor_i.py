"""
3 XOR 4
3: "011"
4: "100"
011
100
XOR
111: 7

5 XOR 5
5: 101
5: 101
101
101
XOR
000

"""

from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        # Sort
        nums.sort()

        # Define binary search
        def binary_search(left, target):
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1

            return left - 1

        # For each left number
        ans = 0
        for left in range(len(nums)):

            target = nums[left] * 2

            # Binary search to find the upper found
            right_bound = binary_search(left, target)

            # print(f"target: {target}, left: {left}, nums[left]: {nums[left]}, right_bound: {right_bound}, nums[right_bound]: {nums[right_bound]}")

            # For each number in the bound, compute XOR and update answer
            # left + 1 because even if we can form a pair with the same number, but their XOR will be 0
            # right_bound + 1 because right_bound is an index that we need to include
            for right in range(left + 1, right_bound + 1):
                # This satisfy abs(a - b) <= min(a, b)
                ans = max(ans, nums[left] ^ nums[right])

        return ans

    def maximumStrongPairXor1(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(len(nums)):

                # Check strong pair
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    # XOR
                    ans = max(ans, nums[i] ^ nums[j])

        return ans
