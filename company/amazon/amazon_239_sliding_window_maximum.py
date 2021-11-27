from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        # If nums is empty, or window size is 0,
        # we cannot return any number list
        if n * k == 0:
            return []

        # If the window size is 1, we don't have to care about taking maximum
        # from multiple numbers in a window.
        # Just return nums as is
        if k == 1:
            return nums

        def clean_deque(i):
            # deq[0] contains the left most index in the previous window
            # if deq[0] == i - k, from the current iteration, deq[0] index
            # is out of window k, so pop the deq[0] index from deq
            if deq and deq[0] == i - k:
                # popleft() because we wanna remove the oldest index in deque
                deq.popleft()

            # by this while loop, the first element of deque will always be the largest number index
            # because it keep removing from the right of the deque until
            # the right end of the deque is bigger than the current num
            while deq and nums[i] > nums[deq[-1]]:
                # By removing from the right, and outside of this function,
                # the current number is appended to deque,
                # deque keeps the descending order
                deq.pop()

        # Initialize dequ and output
        deq = collections.deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)

            # Compute max
            if nums[i] > nums[max_idx]:
                max_idx = i

        output = [nums[max_idx]]

        print(f'deq: {deq}')
        print(f'output: {output}')

        # Build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])

        print(f'deq: {deq}')
        print(f'output: {output}')

        return output


"""
- Time is O(n) because it has the for loop to iterate from 0 to n,
  and clean_deque only does O(1) pop operations. deque doesn't grow so clean_deque while loop
  does not take O(n)
- Space is O(n) for the output array
"""


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
