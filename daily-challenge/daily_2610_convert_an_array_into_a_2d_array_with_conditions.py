"""
Counter
"""

from typing import List
import collections


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        counter = collections.Counter(nums)

        ans = []

        while counter.keys():

            curr = []

            curr_keys = list(counter.keys())

            for k in curr_keys:

                curr.append(k)
                counter[k] -= 1

                if counter[k] == 0:
                    del counter[k]

            ans.append(curr)

        return ans


if __name__ == "__main__":
    nums = [1, 3, 4, 1, 2, 3, 1]
    nums = [1, 2, 3, 4]
    print(Solution().findMatrix(nums))

