from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()

        ans = []
        buf = []

        for i in range(0, len(nums), 2):

            buf.append(nums[i])
            buf.append(nums[i + 1])

            ans.append(buf.pop())
            ans.append(buf.pop())

        return ans