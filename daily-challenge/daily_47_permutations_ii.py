"""
- Backtracking
"""


from typing import List
import collections


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def backtracking(curr, counter):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            # To avoid redundant permutations, use unique number as candidate
            for num in counter:

                if counter[num] > 0:

                    curr.append(num)
                    counter[num] -= 1

                    backtracking(curr, counter)

                    # Backtrack
                    curr.pop()
                    counter[num] += 1

        backtracking([], collections.Counter(nums))

        return ans


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))
