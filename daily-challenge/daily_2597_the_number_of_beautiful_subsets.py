from typing import List
import collections


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        # Optimize to reduce the number of calls of backtracking
        nums.sort()

        counter = collections.Counter()

        def backtracking(index):

            # Terminate
            if index == len(nums):
                return 1

            # Exclude
            ans = backtracking(index + 1)

            # Include
            if nums[index] - k not in counter:

                counter[nums[index]] += 1

                ans += backtracking(index + 1)

                # Backtrack
                counter[nums[index]] -= 1
                if counter[nums[index]] == 0:
                    del counter[nums[index]]

            return ans

        # Backtracking include one case where all the numbers are excluded
        # but this problem requires non-empty subset, so manually exclude empty case count
        return backtracking(0) - 1

    def beautifulSubsets1(self, nums: List[int], k: int) -> int:
        """?"""

        def count_beautiful_subsets(index, mask):

            if index == len(nums):
                # mask > 0 checks non-empty subset
                return 1 if mask > 0 else 0

            is_beautiful = True

            for i in range(index):
                # ?
                if 1 << i & mask == 0 or abs(nums[i] - nums[index]) != k:
                    # if abs(nums[i] - nums[index]) != k:
                    continue
                else:
                    is_beautiful = False
                    break

            skip = count_beautiful_subsets(index + 1, mask)

            if is_beautiful:
                take = count_beautiful_subsets(index + 1, mask + (1 << index))
            else:
                take = 0

            return skip + take

        return count_beautiful_subsets(0, 0)