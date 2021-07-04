from typing import List

class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int:
        longest_streak = 0

        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak

    def longestConsecutive2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                # Consecutive
                if nums[i] == nums[i - 1] + 1:
                    current_streak += 1

                # Consecutive stopped
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)

    def longestConsecutive3(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]

sol = Solution()
# answer = sol.longestConsecutive1(nums)
# answer = sol.longestConsecutive2(nums)
answer = sol.longestConsecutive3(nums)
print(f'Answer: {answer}')
