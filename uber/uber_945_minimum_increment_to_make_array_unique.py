"""
- x will never be larger than the largest value in nums plus the length of nums
  - e.g. nums: [1, 1, 1], len(nums): 3, largest value: 1, largest plus length: 4,
    nums should be [1, 2, 3], so x will never be larger than the number
  - The largest number in the final array will be the original value plus the
    length of the array minus 1
"""


from typing import List
import collections


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        max_val = max(nums)
        count = collections.Counter(nums)
        # ?
        taken = []

        moves = 0
        for x in range(len(nums) + max_val):

            print(f'x: {x}, taken: {taken}, count[x]: {count[x]}')

            # the current num is not unique
            if count[x] >= 2:
                # -1 because among duplicated num, one does not need to change and other need to be incremented
                taken.extend([x] * (count[x] - 1))
                print(f'  taken: {taken}')

            # If there are num saved in taken list and current num is not used,
            # saved num is incremented to this current num
            elif taken and count[x] == 0:
                moves += x - taken.pop()
                print(f'  moves')

        return moves


"""
Complexity
- Let n be the length of nums and m be the max num
- Time is O(n + m) for the for loop
- Space is O(n) for counter and O(n) for taken list
"""


nums = [1, 2, 2]
nums = [1, 2, 2, 2]
print(Solution().minIncrementForUnique(nums))

