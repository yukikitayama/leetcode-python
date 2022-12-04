from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)

        sum_prefix = [0]
        for i in range(n):
            sum_prefix.append(sum_prefix[-1] + nums[i])

        sum_suffix = [0]
        for i in range(n - 1, -1, -1):
            sum_suffix.append(sum_suffix[-1] + nums[i])

        # print(f'sum_prefix: {sum_prefix}, sum_suffix: {sum_suffix}')

        min_avg = float('inf')
        ans = None

        for i in range(n):

            sum_first = sum_prefix[i + 1]
            count_first = i + 1
            avg_first = sum_first // count_first

            sum_last = sum_suffix[-(i + 2)]
            count_last = n - (i + 1)
            if sum_last == 0:
                avg_last = 0
            else:
                avg_last = sum_last // count_last

            abs_diff = abs(avg_first - avg_last)

            if abs_diff < min_avg:
                min_avg = abs_diff
                ans = i

            # print(f'i: {i}, avg_first: {avg_first}, avg_last: {avg_last}, abs_diff: {abs_diff}')

        return ans


class Solution1:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        n = len(nums)
        min_avg = float('inf')
        ans = None

        for i in range(len(nums)):

            nums_first = nums[:i + 1]
            count_first = i + 1
            avg_first = int(sum(nums_first) / count_first)

            nums_last = nums[i + 1:]
            count_last = n - (i + 1)
            if count_last == 0:
                avg_last = 0
            else:
                avg_last = int(sum(nums_last) / count_last)

            abs_diff = abs(avg_first - avg_last)

            if abs_diff < min_avg:
                min_avg = abs_diff
                ans = i

            # print(f'i: {i}, avg_first: {avg_first}, avg_last: {avg_last}, abs_diff: {abs_diff}')

        return ans


if __name__ == '__main__':
    nums = [2, 5, 3, 9, 5, 3]
    # nums = [0]
    print(Solution().minimumAverageDifference(nums))
