from typing import List
import collections


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)

        for k in graph:
            if len(graph[k]) == 1:
                start = k
                break

        ans = []

        def dfs(curr, prev):
            ans.append(curr)

            for neighbor in graph[curr]:
                if neighbor != prev:
                    dfs(neighbor, curr)

        dfs(start, float("inf"))

        return ans


if __name__ == "__main__":
    adjacentPairs = [[2, 1], [3, 4], [3, 2]]
    print(Solution().restoreArray(adjacentPairs))