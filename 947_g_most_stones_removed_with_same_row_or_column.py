from typing import List
from collections import defaultdict
import pprint


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        # Let x and y be the first and second element in the list in stones
        # e.g. stones: [[x_0, y_0], [x_1 y_1], ..., [x_n, y_n]]
        # group_by_ is dictionary Key: x, Value: index in the stones list
        x_to_indices = defaultdict(list)
        y_to_indices = defaultdict(list)

        for i in range(n):
            x, y = stones[i]
            x_to_indices[x].append(i)
            y_to_indices[y].append(i)

        # print('x_to_indices')
        # pprint.pprint(x_to_indices)
        # print('y_to_indices')
        # pprint.pprint(y_to_indices)

        num_disjoint_set = 0
        visited = set()

        for i in range(n):
            if i in visited:
                continue

            stack = [i]
            num_disjoint_set += 1

            while stack:
                current_index = stack.pop()
                visited.add(current_index)
                x, y = stones[current_index]

                for next_index_same_x in x_to_indices[x]:
                    if next_index_same_x in visited:
                        continue

                    stack.append(next_index_same_x)

                for next_index_same_y in y_to_indices[y]:
                    if next_index_same_y in visited:
                        continue

                    stack.append(next_index_same_y)

        return n - num_disjoint_set


"""
Time complexity
Let v be the number of indices, e be the length of adjacency list of each index.
O(v + 2e) = O(v + e) because it needs to iterate all the indice and we have for loop for each index adjacency list

Space complexity
It has one stack, two dictionary with size number of indices v, so O(v + v + v) = O(3v) = O(v)
"""


# stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
print(f'Stones: {stones}')
print(Solution().removeStones(stones))
