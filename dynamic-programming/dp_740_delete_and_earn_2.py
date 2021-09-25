from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Edge case
        if len(nums) == 0:
            return 0

        # Dictionary with Key the distinct number in nums
        # and Value the number of occurrence of the number in nums
        num_to_count = Counter(nums)
        keys = sorted(num_to_count.keys())

        # Base case for dynamic programming
        prev = 0
        curr = keys[0] * num_to_count[keys[0]]

        for i in range(1, len(keys)):
            # If the current num key is adjacent to the previous num key
            # We cannot use the previous curr to current curr
            # To skip, we use prev, or we don't add current curr to the previous curr
            # so we use max()
            if keys[i] - 1 == keys[i - 1]:
                tmp = curr
                curr = max(prev + keys[i] * num_to_count[keys[i]], curr)
                prev = tmp
            # Because previous curr is not adjacent to the current curr,
            # so we can cumulative sum to the previous curr
            else:
                tmp = curr
                curr = curr + keys[i] * num_to_count[keys[i]]
                prev = tmp

        return curr


"""
When we get a number k, we can't get k - 1 and k + 1 because we need to delete them after getting
So it's like house robber problem which does not allow us to rob the adjacent house.

Time: O(nlogn) to sort, and Space: O(n) for dictionary
"""


# nums = [3,4,2]  # 6
# nums = [2,2,3,3,3,4]  # 9
nums = [3,1]  # 4
print(Solution().deleteAndEarn(nums))

