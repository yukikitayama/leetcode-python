"""
- initialize two variables to hold array index for current even and current odd
- scan from left to right
  - enumerate i and num
- Compare current num even or odd to i even or odd
  - Increment even or odd indices by 2
"""


from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_index = 0
        odd_index = 1

        ans = [None] * len(nums)

        for num in nums:

            if num % 2 == 0:
                ans[even_index] = num
                even_index += 2

            elif num % 2 == 1:
                ans[odd_index] = num
                odd_index += 2

        return ans


"""
Let n be the length of nums. Time: O(n) and Space: O(n) for another array
"""


nums = [4,2,5,7]
print(Solution().sortArrayByParityII(nums))


