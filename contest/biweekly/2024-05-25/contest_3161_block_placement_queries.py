from typing import List


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        obstacles = [0]

        ans = []

        for query in queries:

            if query[0] == 1:
                obstacles.append(query[1])
                obstacles.sort()

            elif query[0] == 2:
                pass

            print(obstacles)

        return ans