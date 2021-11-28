from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        # Index is employee ID, element lists are subordinates of each employee
        children = [[] for i in range(n)]

        for i, m in enumerate(manager):
            if m >= 0:
                children[m].append(i)

        # print(f'children: {children}')

        def dfs(i):
            # [0] because bottom of the tree has empty list [].
            # With empty list, list comprehension will be skipped.
            # We don't want that
            # Use max() because a manager i with informTime[i] can inform all the subordinates, so it's not sum()
            # So the leaf of the tree always return 0, because it will be max([0]) and it's 0 and informTime[leaf] is 0
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]

        return dfs(headID)


"""
Time complexity
Let n be the number of employees. O(n) to iterate all the vertices in DFS

Space complexity
O(n) for stack
"""


n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]
n = 3
headID = 0
manager = [-1,0,1]
informTime = [1,2,0]
print(Solution().numOfMinutes(n, headID, manager, informTime))


"""
The time for a manager = max(manager's employee) + informTime[manager]

"""
