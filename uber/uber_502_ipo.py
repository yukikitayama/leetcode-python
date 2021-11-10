"""
- projects we can currently choose is project i where capital[i] <= w
- Backtracking
  - Get workable projects by w and capital,
  - Increment max_capital by profits
  - Decrement k
  - Continue until k is 0
  - Backtrack
    - Try different projects
"""


from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        # Is this guaranteed to be able to return?
        # It's fine because w won't decrease by starting another project
        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))

        n = len(profits)
        projects = [(capital[i], profits[i])for i in range(n)]

        # print(projects)

        # sort projects such that the smallest capital project is the last one
        # projects are popped from the last
        projects.sort(key=lambda x: -x[0])

        available = []
        while k > 0:
            while projects and projects[-1][0] <= w:
                # Push profit
                # By min heap, bigger profit comes to top of the heap by -profit
                heapq.heappush(available, -projects.pop()[1])

            if available:
                # Increment w by the largest profits
                w -= heapq.heappop(available)

            # empty available list means no more project or project capital is bigger than current capital
            else:
                break

            k -= 1

        return w


k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
k = 3
w = 0
profits = [1,2,3]
capital = [0,1,2]
print(Solution().findMaximizedCapital(k, w, profits, capital))






