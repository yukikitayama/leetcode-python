from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ans = 0
        nums_set = set(nums)

        for num in nums:

            curr_streak = 0
            curr_num = num

            while curr_num in nums_set:
                curr_streak += 1

                if curr_num * curr_num > 10 ** 5:
                    break

                curr_num *= curr_num

            ans = max(ans, curr_streak)

        return ans if ans >= 2 else -1

    def longestSquareStreak1(self, nums: List[int]) -> int:

        def binary_search(target):
            left = 0
            right = len(nums) - 1

            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return False

        nums.sort()
        seen = set()
        ans = 0

        for num in nums:

            if num in seen:
                continue

            streak = num
            streak_length = 1

            while streak * streak <= 10 ** 5:

                if binary_search(streak * streak):
                    seen.add(streak)
                    streak_length += 1
                    streak *= streak
                else:
                    break

            ans = max(ans, streak_length)

        return ans if ans >= 2 else -1