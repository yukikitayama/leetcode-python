from typing import List
from collections import defaultdict
import pprint


class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        # Make a graph
        adj = defaultdict(set)
        for e in roads:
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])

        # print(f'Graph:')
        # pprint.pprint(adj)

        # Dynamic programming array
        # f[i][v], i is index at targetPath, v is the candidate current city to put at the index i,
        # and f gives us the tuple (cost, candidate previous city)
        f = [None] * len(targetPath)

        # Base case
        f[0] = [None] * n
        for v in range(n):
            # (0, v) if current city is same as the current city in targetPath
            # If they are different, we need to have 1 edit distance, so (1, v)
            f[0][v] = (1, v) if names[v] != targetPath[0] else (0, v)

        # print(f'DP array after initializing base case:')
        # pprint.pprint(f)

        for i in range(1, len(targetPath)):
            f[i] = [None] * n

            # For each index in targetPath, we try all the cities
            for v in range(n):
                # Initialize cost and city for current index i
                # Because it's before traversing the graph, we don't know
                # what the cost and city will be, so initialize with inf cost
                # and empty city with ''. But these will be updated in the below for loop
                f[i][v] = (float('inf'), '')

                for u in adj[v]:
                    cost = f[i - 1][u][0] + (1 if names[v] != targetPath[i] else 0)
                    if cost < f[i][v][0]:
                        f[i][v] = (cost, u)

        # print(f'DP array after traversing:')
        # pprint.pprint(f)

        # Initialize the last city in the best path and the cost as base case to make the best path
        min_cost = float('inf')
        best_hop = None
        for u in range(0, len(f[-1])):
            if f[-1][u][0] < min_cost:
                min_cost = f[-1][u][0]
                best_hop = u

        # Make the rest of the best path
        best_path = [best_hop]
        for i in range(len(targetPath) - 1, 0, -1):
            prev_hop = f[i][best_hop][1]
            best_path.insert(0, prev_hop)
            best_hop = prev_hop
        return best_path

    def mostSimilar_recursive_td(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]):
        adj = defaultdict(set)
        for e in roads:
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])

        # Memoization for top down dynamic programming
        memo = {}

        def f(i, u):
            """

            :param i: starting index at targetPath
            :param u: the i-1 th node we just chose immediately before best_subpath
            :return: tuple (edit_distance, best_subpath). best_subpath is some path in graph such that
                when compared with targetPath[i:len(targetPath) - 1], it differs minimally with by
                edit_distance node
            """
            if i == len(targetPath):
                return 0, []

            if (i, u) in memo:
                return memo[(i, u)]

            min_cost = float('inf')
            best_path = []

            neighbors = adj[u] if u is not None else range(n)

            for v in neighbors:
                cost, sub_path = f(i + 1, v)

                print(f'v: {v}, i: {i}, cost: {cost}, sub_path: {sub_path}')

                if names[v] != targetPath[i]:
                    cost += 1

                # Update if we find a better lower cost
                if cost < min_cost:
                    min_cost = cost
                    # V is added to the current path so far from the end of the path
                    best_path = [v] + sub_path

            memo[(i, u)] = (min_cost, best_path)
            return memo[(i, u)]

        cost, path = f(0, None)
        return path


"""
mostSimilar_recursive_td
memo[(i, u)] returns us a tuple (cost, path) such that 
to have city at index i in targetPath, if we use city at index u in names,
we can have the returned cost and path
"""


n = 5
roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]]
names = ["ATL","PEK","LAX","DXB","HND"]
targetPath = ["ATL","DXB","HND","LAX"]
print(f'roads: {roads}')
print(f'names: {names}')
print(f'targetPath: {targetPath}')
# print(Solution().mostSimilar_recursive_td(n, roads, names, targetPath))
print(Solution().mostSimilar(n, roads, names, targetPath))
