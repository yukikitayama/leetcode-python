from typing import List
import itertools


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        # print(f'arr: {arr}, target: {target}')

        # Key: cumulative sum, Value: index at which the cumulative sum occurs
        prefix = {0: -1}
        best_till = [float('inf')] * len(arr)

        # print(f'best_till: {best_till}')

        ans = best = float('inf')

        # itertools.accumulate() gives us the prefix sum, or cumulative sum
        # Question is about subarray sum to target, so cumulative sum is useful
        for i, curr in enumerate(itertools.accumulate(arr)):

            # print(f'i: {i}, curr: {curr}')

            # print(f'if curr - target in prefix: {curr - target in prefix} for curr - target: {curr - target}')
            #
            if curr - target in prefix:

                # end is the index at which sub array sums up to target
                end = prefix[curr - target]

                # print(f'end: {end}')

                # print(f'if end > -1: {end > -1}')
                if end > -1:
                    # print(f'ans: {ans}, i - end + best_till[end]: {i - end + best_till[end]}')
                    ans = min(ans, i - end + best_till[end])
                    # print(f'ans: {ans}')

                best = min(best, i - end)

            best_till[i] = best
            prefix[curr] = i

            # print(f'i: {i}, curr: {curr}, best_till: {best_till}, prefix: {prefix}')
            # print(f'best_till: {best_till}, prefix: {prefix}')

        return -1 if ans == float('inf') else ans


arr = [3,2,2,4,3]
target = 3
arr = [7,3,4,7]
target = 7
# arr = [3,1,1,1,5,1,2,1]
# target = 3
print(Solution().minSumOfLengths(arr, target))

