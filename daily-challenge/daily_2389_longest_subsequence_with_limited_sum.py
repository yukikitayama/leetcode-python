from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()
        ans = []

        for query in queries:

            count = 0

            for num in nums:

                if num <= query:
                    count += 1
                    query -= num
                else:
                    break

            ans.append(count)

        return ans


