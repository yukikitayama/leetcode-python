from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()

        # print(nums)

        if len(nums) <= 4:
            return 0

        answer = float('inf')

        for i in range(4):
            small = nums[i]
            # -4, -3, -2, -1
            large = nums[-4 + i]
            difference = large - small

            answer = min(answer, difference)

        return answer


"""
We are allowed to change only three times to minimize difference between max and min
So what we can do is the following
1. decrease the top 3 largest values
2. decrease the top 2 and increase the top 1 smallest
3. decrease 1 and increase 2
4. increase 3

We sort the array in ascending order
1. Take difference between the first value in the array and the forth value from the last
  - Because the last 3 values would be smaller by the above move, but the forth is still left.
2. Take the difference between the second and the 3rd from the last
  - Second because smallest one got larger
  - The 3rd from the last because the last 2 values got smaller by the above operations.
3. 4. likewise
We get minimum value from the 4 cases.

Complexity
Python sort is time complexity is O(nlogn) and space complexity is O(n)
"""

nums = [5, 3, 2, 4]
nums = [1,5,0,10,14]
# nums = [6, 6, 0, 1, 1, 4, 6]
print(Solution().minDifference(nums))
