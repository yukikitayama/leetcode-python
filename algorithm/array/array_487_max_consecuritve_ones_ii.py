"""
- Use sliding window
- Continue expanding the current sequence if it's valid
- If not valid, stop expanding and contract the sequence
"""


from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        left, right = 0, 0
        num_zeroes = 0

        while right < len(nums):
            if nums[right] == 0:
                num_zeroes += 1

            while num_zeroes == 2:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1

            ans = max(ans, right - left + 1)

            right += 1

        return ans


if __name__ == '__main__':
    nums = [1, 0, 1, 1, 0]
    print(Solution().findMaxConsecutiveOnes(nums))
