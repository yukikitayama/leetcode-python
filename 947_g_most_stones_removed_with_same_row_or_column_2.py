from typing import List
from collections import defaultdict
import pprint


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Use x coordinate as key and list of indices of stone as value
        # to know whichi coordinates share the same row
        # Same for y
        x_to_index = defaultdict(list)
        y_to_index = defaultdict(list)
        for i, stone in enumerate(stones):
            x_to_index[stone[0]].append(i)
            y_to_index[stone[1]].append(i)

        pprint.pprint(f'x_to_index: {x_to_index}')
        pprint.pprint(f'y_to_index: {y_to_index}')

        num_shared = 0
        visited = set()

        for i in range(len(stones)):

            if i in visited:
                continue

            stack = [i]
            num_shared += 1

            while stack:
                curr_index = stack.pop()
                visited.add(curr_index)

                curr_x, curr_y = stones[curr_index]

                # Find coordinates sharing same row
                for other_index in x_to_index[curr_x]:
                    if other_index in visited:
                        continue
                    stack.append(other_index)

                # Find coordinates sharing same column
                for other_index in y_to_index[curr_y]:
                    if other_index in visited:
                        continue
                    stack.append(other_index)


        num_coordinates = len(stones)
        return num_coordinates - num_shared


"""
"""


# stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]  # 5
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]  # 3
print(f'Stones: {stones}')
print(Solution().removeStones(stones))
