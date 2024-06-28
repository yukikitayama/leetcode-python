"""
High indegree city is assigned high value
Hashmap
  k: city index
  v: value of city
"""

from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        """Simplify calculation"""
        indegree = [0] * n
        for a, b in roads:
            indegree[a] += 1
            indegree[b] += 1
        indegree.sort()

        ans = 0
        value = 1

        # Least indegree city has least value
        # each city has the number of edges equal to indegree
        # So we increment by its value multipled by the number of each indegree
        for d in indegree:
            ans += value * d
            value += 1

        return ans

    def maximumImportance1(self, n: int, roads: List[List[int]]) -> int:
        indegree = [0] * n
        for a, b in roads:
            indegree[a] += 1
            indegree[b] += 1

        indegree = [[d, city_index] for city_index, d in enumerate(indegree)]
        indegree.sort(reverse=True)

        # print(indegree)

        city_to_value = {}
        for i in range(n):
            city_to_value[indegree[i][1]] = n - i

        # print(city_to_value)

        ans = 0

        for a, b in roads:
            ans += city_to_value[a] + city_to_value[b]

        return ans