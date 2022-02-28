from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        ans = []

        right = 0

        while right < len(nums):

            left = right

            # Expand range
            while right + 1 < len(nums) and nums[right + 1] == nums[right] + 1:
                right += 1

            if left == right:
                ans.append(str(nums[left]))
            else:
                ans.append(f'{nums[left]}->{nums[right]}')

            right += 1

        return ans


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]
    print(Solution().summaryRanges(nums))
