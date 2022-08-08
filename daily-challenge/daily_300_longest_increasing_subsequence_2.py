"""
- binary search or priority queue
- O(n logn)
"""


from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        for num in nums:
            i = bisect.bisect_left(sub, num)

            if i == len(sub):
                sub.append(num)

            else:
                sub[i] = num

        return len(sub)


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]

        for num in nums[1:]:

            if num > sub[-1]:
                sub.append(num)

            # Replace existing for the future possibility
            else:

                i = 0
                while sub[i] < num:
                    i += 1
                sub[i] = num

        return len(sub)


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for i in range(1, len(nums)):

            for j in range(i):

                if nums[i] > nums[j]:

                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # 4
    print(Solution().lengthOfLIS(nums))
