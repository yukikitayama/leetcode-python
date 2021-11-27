"""
- It takes O(n) steps to make a single permutation, and
  it has n! permutations, so time is O(n * n!)
- Space is O(2n) = O(n) by counter hashtable and recursion call stack
"""


from typing import List
import collections


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                ans.append(comb[:])
                return

            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[num] += 1

        backtrack([], collections.Counter(nums))

        return ans


nums = [1, 1, 2]
print(Solution().permuteUnique(nums))






