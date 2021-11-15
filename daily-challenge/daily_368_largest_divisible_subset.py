"""
- answer[i] % answer[j] == 0
  - answer[j] is bigger than answer[i]
- answer[j] % answer[i] == 0
  - answer[i] is a factor of answer[j]

- Any value can be added and form divisible subset if the value is divisible by the largest
  value in the divisible subset
  - If h % G == 0, [E, F, G, h] is divisible subset, where [E, F, G] was divisible subset
- Any value can be added and form the subset if the value can divide the smallest number
  in the subset
  - If E % d == 0, [d, E, F, G] is the subset
"""


from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        subsets = {-1: set()}
        for num in sorted(nums):

            # print(f'  num: {num}, subsets: {subsets}')
            # for k in subsets:
            #     if num % k == 0:
            #         print(f'    subsets[k]: {subsets[k]}, len(subsets[k]): {len(subsets[k])}')
            # print(f'  max: {max([subsets[k] for k in subsets if num % k == 0], key=len)}')

            # max() gives us the largest set where the current number is divisible by the largest number (k) in the set
            # | {nums} allows us to union the current num to the new set
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}

        # Get the largest set
        return list(max(subsets.values(), key=len))


nums = [1,2,4,7,8]
print(Solution().largestDivisibleSubset(nums))
