"""
- Scan from right
  - Record number and index
"""


from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                last_i = stack.pop()
                ans[last_i] = i - last_i
            stack.append(i)
        return ans


# temperatures = [73,74,75,71,69,72,76,73]
temperatures = [30,40,50,60]
# temperatures = [30,60,90]
print(Solution().dailyTemperatures(temperatures))


