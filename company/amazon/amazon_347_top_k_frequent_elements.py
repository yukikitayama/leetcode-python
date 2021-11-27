from typing import List
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k == len(nums):
            return nums

        # Takes O(n)
        count = collections.Counter(nums)

        # Take O(nlogk)
        return heapq.nlargest(k, count.keys(), key=count.get)


nums = [1,1,1,2,2,3]
k = 2
nums = [1]
k = 1
print(Solution().topKFrequent(nums, k))

