"""
Algorithm
- Initialize sub with the first element in nums
- Iterate nums from index of 1
  - If current num is bigger than elements in sub, append current num to sub
  - If current num is smaller than or equal to the elements in sub
    - Iterate sub to find the first element bigger than or equal to current num,
      and replace
      - It will create a invalid subsequence because order is different from original nums
      but the length is valid
- Return the length of sub
"""


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])

            else:
                j = 0
                while nums[i] > sub[j]:
                    j += 1
                sub[j] = nums[i]

        # print(f'sub: {sub}')

        return len(sub)


nums = [10,9,2,5,3,7,101,18]
nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
print(Solution().lengthOfLIS(nums))
