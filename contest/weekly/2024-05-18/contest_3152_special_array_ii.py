"""
Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]

Output: [false,true]

Explanation:

The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
"""

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        booleans = []
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                booleans.append(False)
            else:
                booleans.append(True)

        # print(booleans)

        prefix_sums = [0]
        prefix_sum = 0
        for i in range(len(booleans)):
            if booleans[i]:
                prefix_sum += 1
            prefix_sums.append(prefix_sum)

        # print(prefix_sums)

        ans = []

        for from_, to_ in queries:

            num_pairs = to_ - from_
            num_specials = prefix_sums[to_] - prefix_sums[from_]

            if num_pairs == num_specials:
                ans.append(True)
            else:
                ans.append(False)

        return ans

    def isArraySpecial1(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        ans = []

        for from_, to_ in queries:
            res = True
            for i in range(from_ + 1, to_ + 1):

                if nums[i] % 2 == nums[i - 1] % 2:
                    res = False

            ans.append(res)

        return ans
