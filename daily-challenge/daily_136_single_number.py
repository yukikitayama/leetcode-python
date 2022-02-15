from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans


if __name__ == '__main__':
    nums = [2, 2, 1]
    print(Solution().singleNumber(nums))
