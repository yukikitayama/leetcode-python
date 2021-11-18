"""
- get length of nums, n
- Get a complete set of length n
- Subtract nums set from complete set
- Return the set as list
"""


from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = set([i for i in range(1, n + 1)])
        b = set(nums)
        ans = list(a - b)
        return ans


"""
Complexity
- Time is O(n) to make a complete set
- Space is O(n) for complete set
"""


nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))




