from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total_array_sum = sum(nums)
        target_sum, remainder = divmod(total_array_sum, k)

        if remainder != 0:
            return False

        nums.sort(reverse=True)

        taken = ['0'] * n

        memo = {}

        print(f'nums: {nums}, k: {k}, target_sum: {target_sum}, taken: {taken}')

        def backtrack(index, count, curr_sum):
            taken_str = ''.join(taken)

            print(f'  In backtrack: index: {index}, count: {count}, taken_str: {taken_str}, memo: {memo}')

            if count == k - 1:
                return True

            if curr_sum > target_sum:
                return False

            # ?
            if taken_str in memo:
                return memo[taken_str]

            if curr_sum == target_sum:
                # ?
                memo[taken_str] = backtrack(0, count + 1, 0)
                print(f'    memo: {memo}')
                return memo[taken_str]

            for j in range(index, n):
                if taken[j] == '0':
                    taken[j] = '1'

                    if backtrack(j + 1, count, curr_sum + nums[j]):
                        return True

                    print(f'      Backtracking... memo: {memo}')

                    taken[j] = '0'

            memo[taken_str] = False
            return memo[taken_str]

        return backtrack(0, 0, 0)


"""
Backtracking plus memoization
"""


nums = [4,3,2,3,5,2,1]
k = 4
# nums = [1,2,3,4]
# k = 3
print(Solution().canPartitionKSubsets(nums, k))




