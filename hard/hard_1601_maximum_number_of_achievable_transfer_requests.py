from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        ans = 0
        indegree = [0] * n

        def backtracking(i, c):
            nonlocal ans

            # Termination
            if i == len(requests):

                for j in range(len(indegree)):
                    if indegree[j] != 0:
                        return

                ans = max(ans, c)
                return

                # Case 1: Process current request
            indegree[requests[i][0]] -= 1
            indegree[requests[i][1]] += 1
            backtracking(i + 1, c + 1)

            # Backtrack
            indegree[requests[i][0]] += 1
            indegree[requests[i][1]] -= 1

            # Case 2: Ignore current request
            backtracking(i + 1, c)

        backtracking(0, 0)

        return ans