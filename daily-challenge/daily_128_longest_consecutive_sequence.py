from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)

        for num in nums_set:

            print(f'  num: {num}')

            # Run the rest only when find the start value
            # When num is not the start value, we don't even run the while loop
            # So though this looks like O(N^2), it's actually O(N)
            if num - 1 not in nums_set:
                curr_num = num
                curr_len = 1

                while curr_num + 1 in nums_set:

                    print(f'    curr_num: {curr_num}, curr_len: {curr_len}')

                    curr_num += 1
                    curr_len += 1

                ans = max(ans, curr_len)

        return ans


class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not len(nums):
            return 0

        nums.sort()

        # print(f'nums: {nums}')

        ans = 1
        curr = 1

        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    curr += 1
                    ans = max(ans, curr)
                else:
                    curr = 1

        return ans


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    # 4
    nums = [1, 2, 3, 100, 101, 102, 103]
    # nums = [1, 2, 0, 1]
    # 3
    # nums = [1, 2, 3]
    # 3
    print(Solution().longestConsecutive(nums))
