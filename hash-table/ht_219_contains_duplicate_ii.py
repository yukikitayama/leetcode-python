"""
Result
- Start: 9:31
- End: 9:38
- Solved: 1
- Optimized: 1
- Saw solution: 0

Idea
- Hashmap with key num and value index
- iterate nums
  - add num as key and index as value if the num does not exist in the map
  - if exist
    - calculation
    - update the index value in map with the current index
"""


from typing import List
import collections


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_index = collections.defaultdict(int)

        for i, num in enumerate(nums):

            if num not in num_to_index:
                num_to_index[num] = i
            else:
                if abs(i - num_to_index[num]) <= k:
                    return True
                else:
                    num_to_index[num] = i

        return False


"""
- Time is O(n) for the for loop
- Space is O(n) for the hashmap
"""


nums = [1,2,3,1]
k = 3
nums = [1,0,1,1]
k = 1
nums = [1,2,3,1,2,3]
k = 2
print(Solution().containsNearbyDuplicate(nums, k))




