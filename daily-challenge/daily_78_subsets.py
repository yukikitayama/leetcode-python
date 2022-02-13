from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:

            temp = [curr + [num] for curr in ans]
            ans += temp

        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
