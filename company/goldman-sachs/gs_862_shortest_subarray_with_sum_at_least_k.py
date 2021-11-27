"""
- dp?
- two pointers?
- prefix sum?

nums: [1, 2]
prefix sum: [1, 3]

nums: [2, -1, 2]
prefix sum: [2, 1, 3]

- Keep the following equation, and increase P[x]
  - So sum is at least K and minimize the sum because increasing P[x] makes subtraction bigger
P[y] - P[x] >= K
     - P[x] >= -P[y] + K
       P[x] <= P[y] - k
Also
P[y] >= P[x] + K
"""


from typing import List
import collections


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        print(f'prefix_sum: {prefix_sum}')

        # Answer is the length of shortest subarray
        # so it won't be bigger than n, but use n + 1 as placeholder to be updated
        # if it stays the same, it indicates that there's no such subarray so return -1
        ans = n + 1

        # Queue contains indices to prefix_sum
        queue = collections.deque()
        for i, py in enumerate(prefix_sum):

            print(f'  i: {i}, py: {py}')

            # If it finds smaller prefix sum than the prefix sum pointed by the index in queue
            # remove the stack top index, because we won't need it anymore
            # But at the end, it append the current index, so first at the queue is the index gives
            # us the smallest prefix_sum, and the next smallest prefix_sum follows
            while queue and py <= prefix_sum[queue[-1]]:

                print(f'    py: {py}, prefix_sum[queue[-1]]: {prefix_sum[queue[-1]]}')

                popped = queue.pop()

                print(f'    popped: {popped}')

            while queue and py - prefix_sum[queue[0]] >= k:
                # Answer is length
                popped_left = queue.popleft()
                # the start element of prefix_sum is 0, and it works because
                # when getting length of subarray by index, it doesn't add 1 as typically does
                # j - i + 1, but here, it's just j - i
                ans = min(ans, i - popped_left)

                print(f'    popped_left: {popped_left}')

            queue.append(i)

            print(f'    queue: {queue}')

        return ans if ans < n + 1 else -1


nums = [2,-1,2]
k = 3
print(Solution().shortestSubarray(nums, k))






