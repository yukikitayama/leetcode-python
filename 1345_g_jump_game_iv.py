from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]
        # print(f'Graph: {graph}')

        # curs is a list of nodes that needs to go in the current iteration
        curs = [0]
        visited = {0}
        step = 0

        while curs:

            # nex is a list of nodes which should go next iteration
            # Since it only refers to the next, when current start, we should nex = [] to clear it
            nex = []

            # curs contains indices of list
            for node in curs:
                # print(f'node: {node}, step: {step}')

                # Check if reached end
                if node == n - 1:
                    return step

                # Check the same value
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # Clear the list to prevent redundant search
                # Okay to clear because all the children are already in nex list by the above for loop
                graph[arr[node]].clear()

                # Check neighbors
                for child in [node - 1, node + 1]:

                    # Check if the neighbor index in the boundary and not visited
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1


"""
Time complexity
Let n be the length of arr
O(n) to visit all the elements in the arr at most once

Space complexity
O(2n) = O(n) for 2 arrays with the length n
"""


arr = [100,-23,-23,404,100,23,23,23,3,404]
print(Solution().minJumps(arr))
