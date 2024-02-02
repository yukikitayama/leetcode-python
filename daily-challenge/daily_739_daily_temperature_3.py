"""
iterate temperatures
  stack collects temperature

if curr > top
  compute difference of indices
  pop top
  append curr

  keep popping until curr < top

stack keeps monotonically decreasing
"""

from typing import List


class Solution:
    def dailyTemperature1(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            if not stack:
                stack.append(i)

            else:

                while stack and temperatures[i] > temperatures[stack[-1]]:

                    top = stack.pop()
                    diff = i - top
                    ans[top] = diff

                stack.append(i)

        return ans

    def dailyTemperature(self, temperatures: List[int]) -> List[int]:
        hottest = 0
        ans = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):

            if temperatures[i] >= hottest:
                hottest = temperatures[i]
                continue

            days = 1
            # <= because we need to find strictly higher value
            while temperatures[i + days] <= temperatures[i]:
                days += ans[i + days]
            ans[i] = days

        return ans


if __name__ == "__main__":
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    # temperatures = [30, 40, 50, 60]
    # temperatures = [30, 60, 90]
    temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    # [8,1,5,4,3,2,1,1,0,0]
    print(Solution().dailyTemperature(temperatures))










