"""
- counter
- sort by count ascending, key descending
- time O(NlogN)
"""


from typing import List
import collections


class Solution1:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        c = collections.Counter(nums)
        num_to_count = [[k, v] for k, v in c.items()]
        num_to_count.sort(key=lambda x: (x[1], -x[0]))
        ans = []
        for num, count in num_to_count:
            ans += [num] * count
        return ans


if __name__ == '__main__':
    nums = [2,3,1,3,2]
    print(Solution().frequencySort(nums))
