"""
Result
- Start: 6:35
- End: 6:48
- Solved: 1
- Saw solution: 0
- Optimized: 1
"""


from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pos = nums[0]
        neg = nums[0]
        ans = max(pos, neg)
        for i in range(1, len(nums)):
            pos, neg = max(nums[i], nums[i] * pos, nums[i] * neg), min(nums[i], nums[i] * neg, nums[i] * pos)
            ans = max(ans, pos, neg)

            # print(f'  i: {i}, nums[i]: {nums[i]}, pos: {pos}, neg: {neg}, ans: {ans}')

        return ans


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    # 6
    nums = [-2, 0, -1]
    # 0
    # nums = [-2]
    # -2
    # nums = [-2,3,-4]
    # 24
    # nums = [-4, -3, -2]
    # 12
    print(Solution().maxProduct(nums))
