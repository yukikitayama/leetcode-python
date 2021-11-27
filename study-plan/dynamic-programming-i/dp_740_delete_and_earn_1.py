from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)

        # prev is the previous number in iteration
        prev = None

        # Avoid is the answer if we don't take k
        # Using is the answer if we take k
        avoid = using = 0

        for k in sorted(count):

            if k - 1 != prev:

                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)

            # when a new k is one integer higher than prev
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid

            prev = k

        return max(avoid, using)


"""
Time complexity
O(nlogn) for sort counter by letting n be the distinct numebr in nums

Space complexity
O(n) for counter
"""


nums = [3,4,2]
nums = [2,2,3,3,3,4]
print(Solution().deleteAndEarn(nums))

