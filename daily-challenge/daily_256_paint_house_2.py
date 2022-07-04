from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        prev = costs[-1][:]

        for i in range(len(costs) - 1, -1, -1):
            if i == len(costs) - 1:
                continue

            curr = costs[i][:]

            curr[0] += min(prev[1], prev[2])
            curr[1] += min(prev[0], prev[2])
            curr[2] += min(prev[0], prev[1])
            prev = curr
        return min(prev)


class Solution1:
    def minCost(self, costs: List[List[int]]) -> int:

        def dfs(n, color, memo):
            if (n, color) in memo:
                return memo[(n, color)]

            cost = costs[n][color]

            if n == len(costs) - 1:
                pass
            elif color == 0:
                cost += min(dfs(n + 1, 1, memo), dfs(n + 1, 2, memo))
            elif color == 1:
                cost += min(dfs(n + 1, 0, memo), dfs(n + 1, 2, memo))
            elif color == 2:
                cost += min(dfs(n + 1, 0, memo), dfs(n + 1, 1, memo))

            memo[(n, color)] = cost

            return cost

        memo = {}

        return min(
            dfs(0, 0, memo),
            dfs(0, 1, memo),
            dfs(0, 2, memo)
        )


if __name__ == '__main__':
    costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    # 10
    costs = [[7, 6, 2]]
    # 2
    print(Solution().minCost(costs))
