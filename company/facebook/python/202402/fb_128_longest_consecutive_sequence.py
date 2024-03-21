from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0

        for i in range(len(nums)):
            curr_num = nums[i]
            curr_length = 1

            # Nested loop only starts when current number is the beginning of a sequence
            # so the time complexity will be O(N)
            # nums = [100,4,200,1,3,2], only 1, 100, and 200 will initiate while-loop
            if curr_num - 1 not in nums_set:

                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_length += 1

                ans = max(ans, curr_length)

        return ans

    def longestConsecutive1(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            curr_num = nums[i]
            curr_length = 1

            while curr_num + 1 in nums:
                curr_num += 1
                curr_length += 1

            ans = max(curr_length, ans)

        return ans
