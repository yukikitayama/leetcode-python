"""
- Changing the order of removing changes the number of removed stones
- Number of removed stones is the number of steps DFS can go to the next
- graph dictionary key: x or y and value: list of index to stones
- Total stones minus the number of connected components is the number of removed stones
"""


from typing import List
import collections


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        x_to_index = collections.defaultdict(list)
        y_to_index = collections.defaultdict(list)

        for i, stone in enumerate(stones):
            x = stone[0]
            y = stone[1]
            x_to_index[x].append(i)
            y_to_index[y].append(i)

        # print(f'{x_to_index}, {y_to_index}')

        n = len(stones)
        num_connected_component = 0
        visited = set()

        for i, stone in enumerate(stones):

            if i in visited:
                continue

            num_connected_component += 1
            stack = [i]

            while stack:

                curr_i = stack.pop()
                visited.add(curr_i)
                curr_x, curr_y = stones[curr_i]

                for next_i in x_to_index[curr_x]:
                    if next_i not in visited:
                        stack.append(next_i)

                for next_i in y_to_index[curr_y]:
                    if next_i not in visited:
                        stack.append(next_i)

        return n - num_connected_component


if __name__ == '__main__':
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    stones = [[0, 0]]
    stones = [[3, 2], [3, 1], [4, 4], [1, 1], [0, 2], [4, 0]]
    # 4
    print(Solution().removeStones(stones))
