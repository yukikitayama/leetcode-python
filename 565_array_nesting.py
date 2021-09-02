from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False for _ in range(len(nums))]
        answer = 0
        for i in range(len(nums)):
            if not visited[i]:
                start = nums[i]
                count = 1
                start = nums[start]
                while start != nums[i]:
                    count += 1
                    visited[start] = True
                    start = nums[start]
                answer = max(answer, count)
        return answer


nums = [5,4,0,3,1,6,2]
nums = [0,1,2]
print(Solution().arrayNesting(nums))
