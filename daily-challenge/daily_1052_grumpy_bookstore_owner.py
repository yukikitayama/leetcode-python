"""
2 pass
first pass
  count customers where grumpy is 0
second pass
  find max so far
  minutes length window
  iterate from left to right
    Increment customer right pointer is grumpy 1
    Shrink window if length > minutes
    Decrement customer if left pointer is grumpy 1
return first pass count + second pass max so far
"""

from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                ans += customers[i]

        left = 0
        max_so_far = 0
        curr = 0
        for right in range(len(customers)):
            if grumpy[right] == 1:
                curr += customers[right]

            if right - left + 1 > minutes:
                if grumpy[left] == 1:
                    curr -= customers[left]
                left += 1

            max_so_far = max(max_so_far, curr)

        return ans + max_so_far