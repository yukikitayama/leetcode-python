"""
sliding window
counter hashmap

"""

from typing import List
import collections


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:

        ans = []
        counter = collections.Counter()
        left = 0
        for right in range(len(nums)):

            counter[nums[right]] += 1

            if right - left + 1 == k:
                ans.append(len(counter))

                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1

        return ans