"""
- Backtrack
  - from left to right
- swap

- Make a hashmap with key unique number and value number of occurrence
-
"""


from typing import List
import collections


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:


        ans = []
        count = collections.Counter(nums)

        def backtracking(combination, counter):

            if len(combination) == len(nums):
                # Need combination[:] or list(combination) to make a copy of the list
                # otherwise combination is reference pointing at the shared object
                # so the snapshot of permutation is not saved in ans list
                ans.append(combination[:])
                return

            for num in counter:
                if counter[num] > 0:
                    combination.append(num)
                    counter[num] -= 1

                    backtracking(combination, counter)

                    # Backtrack
                    combination.pop()
                    counter[num] += 1

        print(f'count: {count}')

        backtracking([], count)

        return ans


"""
- Let n be the length of nums
- Time is O(n * n!) because it takes n to make a single permutation, and in total we have
  n! permutations
- Space is O(n) for a hashmap, O(n) for recursion stack, and O(n) for temporary answer list,
  so it's O(n)
"""


nums = [1, 1, 2]
print(Solution().permuteUnique(nums))



