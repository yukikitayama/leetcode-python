"""
Idea
- Modify the nums in place?

Algorithm
- Initialize an empty hashmap
- Initialize ans empty list
- Iterate nums from left to right
  - Add a num to hashmap
  - If the value becomes two, append the key to ans
- return ans

Complexity
- Time: O(n)
- Space: O(n)


- 1 <= nums[i] <= n, so taking num from nums, (num - 1) is a valid index
  - because min possible num is 1 and max possible num is n, so
    min possible index is 0 and max possible index is n - 1
- We can do nums[num - 1]
- Iterate num in nums
  - get index by abs(num) - 1, multiply -1 to nums[the index]
    - If num appear only once, num remains negative after the iteration
    - But if num appear twice, nums[abs(num) - 1] becomes back positive with twice negative operations
    - We won't have three negation operations, because guaranteed to appear once or twice.
- Iterate num in nums again,
  - use the index of (abs(num) - 1) again to find the positive num in nums
  - If positive, append it to ans
  - Negate again to avoid double count
- Do not just append positive num to ans without using index of (abs(num) - 1),
  - because num could remain positive if no num - 1 pointed at the num, but it does not mean twice
"""


from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        # print(f'nums: {nums}')

        for num in nums:
            nums[abs(num) - 1] *= -1

            # print(f'num: {num}, abs(num) - 1: {abs(num) - 1}, nums[abs(num) - 1]: {nums[abs(num) - 1]}')

        # print(f'nums: {nums}')

        for num in nums:
            if nums[abs(num) - 1] > 0:
                ans.append(abs(num))
                nums[abs(num) - 1] *= -1

        # print(f'nums: {nums}')

        return ans


nums = [4,3,2,7,8,2,3,1]
# nums = [1, 2, 3, 4, 5]
nums = [1, 2, 2, 1, 4]
print(Solution().findDuplicates(nums))
