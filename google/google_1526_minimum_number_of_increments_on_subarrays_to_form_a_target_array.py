from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        answer = 0
        current = 0
        for num in target:
            if num > current:
                answer += max(num - current, 0)
            current = num

        return answer


"""
Algorithm
- It scans from left to right.
- If the current number is bigger than the previous number, we need to increment it
- If the subsequent numbers are smaller the current number, previous increment operation already made effect, 
  so we don't have to care
- But After decreasing, if we see the number increase again, we need to increment again, because we can think like
  - those small numbers between previous bigger number and current bigger number are separated by the see and 
  - we have two islands, so two subarray, we need to do increment operation again.
  
Time
- Let n be the length of target. O(n) because it iterates the target array

Space
- O(1) because we only variables.
"""


target = [1,2,3,2,1]
# target = [3,1,1,2]
target = [3,1,5,4,2]
target = [1,1,1,1]
print(Solution().minNumberOperations(target))
