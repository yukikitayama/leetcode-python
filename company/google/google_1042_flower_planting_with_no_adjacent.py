from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(n)]

        # print(graph)

        for x, y in paths:
            # -1 because x and y are 1-based
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        # print(graph)

        ans = [0] * n
        for i in range(n):

            # Find a set of flower types already planted
            planted_flower_type = set()
            for j in graph[i]:
                planted_flower_type.add(ans[j])

            # Find a set of flower types unplanted
            unplanted_flower_type = {1, 2, 3, 4} - planted_flower_type

            # Assign any flower type to current garden
            # pop() method of set removes a random element
            ans[i] = unplanted_flower_type.pop()

        return ans


if __name__ == '__main__':
    n = 3
    paths = [[1, 2], [2, 3], [3, 1]]
    n = 4
    paths = [[1, 2], [3, 4]]
    print(Solution().gardenNoAdj(n, paths))
