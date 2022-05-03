"""
Follow up: Can you solve it in O(n) time complexity?
"""


from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        # Find left boundary
        left = len(nums)
        stack = []
        for i in range(len(nums)):
            # When we find downward slope
            while stack and nums[stack[-1]] > nums[i]:
                left = min(left, stack.pop())
            stack.append(i)

        # Find right boundary
        right = 0
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            # When we find upward slope
            while stack and nums[i] > nums[stack[-1]]:
                right = max(right, stack.pop())
            stack.append(i)

        # print(f'left: {left}, right: {right}')

        if right - left > 0:
            return right - left + 1
        else:
            return 0


class Solution3:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_copy = nums[:]
        nums_copy.sort()

        left = len(nums)
        right = 0

        for i in range(len(nums)):
            if nums_copy[i] != nums[i]:
                left = min(left, i)
                right = max(right, i)

        if right - left < 0:
            return 0
        else:
            return right - left + 1


class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # These will be updated
        left = len(nums)
        right = 0

        # -1 and + 1 because we want i and j won't be overlapped
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):

                # If not ascending order, update pointers
                if nums[i] > nums[j]:
                    left = min(left, i)
                    right = max(right, j)

        # When everything is ascending right and left pointers are opposite,
        # so it should be negative, so no need to sort, so return 0
        if (right - left) < 0:
            return 0
        # Otherwise return left
        # +1 because left and right both are inclusive pointers
        else:
            return right - left + 1


class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        ans = len(nums)

        for i in range(len(nums)):
            for j in range(i, len(nums) + 1):

                # Find min and max in current subarray
                min_ = float('inf')
                max_ = float('-inf')
                for k in range(i, j):
                    min_ = min(min_, nums[k])
                    max_ = max(max_, nums[k])

                # print(f'min_: {min_}, max_: {max_}, i: {i}, j: {j}')

                # Continue because
                # when left outside of subarray is bigger than subarray min,
                # or when right outside of subarray is smaller than subarray max,
                # it's pointless to consider sorting subarray, because even if sorting the subarray,
                # the whoe array won't be sorted
                if (i > 0 and nums[i - 1] > min_) or (j < len(nums) and max_ > nums[j]):
                    continue

                prev = float('-inf')
                k = 0
                # Terminates when k == i or prev is bigger than current (not ascending)
                while k < i and prev <= nums[k]:
                    prev = nums[k]
                    k += 1
                # 0 to i - 1 needs to be ascending order
                # Because of the above while loop, if k is not i,
                # 0 to i - 1 is not ascending order, so it's pointless to update ans
                # so continue
                if k != i:
                    continue

                # j is right outside of subarray
                # Checking whether j to len(nums) - 1 is ascending order
                k = j
                while k < len(nums) and prev <= nums[k]:
                    prev = nums[k]
                    k += 1
                # Finally, if k == len(nums), left outside of subarray and right outside of subarray
                # are ascending, so it's okay to update answer for the length of non sorted subarray
                if k == len(nums):
                    ans = min(ans, j - i)

                # print(f'  ans: {ans}')

        return ans


if __name__ == '__main__':
    nums = [2, 6, 4, 8, 10, 9, 15]
    # 5
    # nums = [1, 2, 3, 4]
    # 0
    # nums = [1]
    # 0
    print(Solution().findUnsortedSubarray(nums))
