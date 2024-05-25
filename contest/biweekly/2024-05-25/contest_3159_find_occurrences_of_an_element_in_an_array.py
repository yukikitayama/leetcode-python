from typing import List


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:

        x_count = 0
        x_indices = []
        for i in range(len(nums)):
            if nums[i] == x:
                x_count += 1
                x_indices.append(i)

        # print(x_count, x_indices)

        ans = []

        for query in queries:

            if query > x_count:
                ans.append(-1)
            else:
                ans.append(x_indices[query - 1])

        return ans
