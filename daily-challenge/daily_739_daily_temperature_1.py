"""
- brute force
  - iterate each temperature,
  - user two pointers
- Complexity
  - Time is O(n^2)
- Result
  - TLE
"""


from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans = []
        # for i in range(len(temperatures)):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             ans.append(j - i)
        #             break
        #         elif j == len(temperatures) - 1:
        #             ans.append(0)
        #     if i == len(temperatures) - 1:
        #         ans.append(0)
        # return ans

        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans[i] = j - i
                    break
        return ans


# temperatures = [73,74,75,71,69,72,76,73]
# temperatures = [30,40,50,60]
temperatures = [30,60,90]
print(Solution().dailyTemperatures(temperatures))


