"""
Idea
- For each num in nums
  - square it
- Sort the array
- Return the array

Complexity
- Time: O(n + nlogn) = O(nlogn)
- Space: O(n)
"""


from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        # In absolute num in nums, bigger nums are at the left and right edges of nums,
        # and absolute small values are in the middle of nums
        # So iteration starts from left end and right end. And go towards inside
        left = 0
        right = n - 1

        # By iterating from absolute large num in nums, squared value will be from largest to smallest
        # so to make an answer list, the index iterates from the last to 0
        for i in range(n - 1, -1, -1):

            # If the right absolute num is bigger, we append it to from the last of the answer array
            if abs(nums[left]) < abs(nums[right]):
                curr_num = nums[right]
                # Decrement to get the next num
                right -= 1

            # If left is bigger than or equal to right, use left
            else:
                curr_num = nums[left]
                left += 1

            result[i] = curr_num ** 2

        return result



"""
Complexity
- Time: O(n) for for loop from the last to 0
- Space: O(1) because answer list is not included

Test
nums: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
len(nums): 5
result: [0, 0, 0, 0, 0]
left: 0
right: 4
i: 4, abs(nums[left]): 4, abs(nums[right]): 10, if: T square: 10, right: 3, result: [0, 0, 0, 0, 100]
i: 3, abs(nums[left]): 4, abs(nums[right]): 3, if: F, square: 4, left: 1, result: [0, 0, 0, 16, 100]
i: 2, abs(nums[left]): 1, abs(nums[right]): 3, if: T, square: 3, right: 2, result: [0, 0, 9, 16, 100]
i: 1, abs(nums[left]): 1, abs(nums[right]): 0, if: F, square: -1, left: 2, result: [0, 1, 9, 16, 100]
i: 0, abs(nums[left]): 0, abs(nums[right]): 0, if: F, square: 0, left: 3, result: [0, 1, 9, 16, 100]
"""

