"""
Sliding window
  First get total of customers where grumpy is 0
  move minutes length window over grumpy
    if in window, grumpy is 1, add the corresponding customer to total
      update total
"""

from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        # Pre-compute number of customers without grumpy
        no_grumpy = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                no_grumpy += customers[i]

        # By sliding window, compute the additional number of customers by masking grumpy
        # and find the maximum additional number by sliding the window of minutes length
        addition = 0
        i = 0
        while i < len(customers) and i < minutes:
            if grumpy[i] == 1:
                addition += customers[i]
            i += 1

        ans = max(no_grumpy, no_grumpy + addition)

        while i < len(customers):

            if grumpy[i - minutes] == 1:
                addition -= customers[i - minutes]
            if grumpy[i] == 1:
                addition += customers[i]

            ans = max(ans, no_grumpy + addition)
            i += 1

        return ans
