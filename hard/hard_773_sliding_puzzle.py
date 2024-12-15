"""
0, 1, 2
3, 4, 5
"""


from typing import List
import collections


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        directions = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4]
        ]

        def swap(curr_state, i, j):
            s = list(curr_state)
            s[i], s[j] = s[j], s[i]
            next_state = "".join(s)
            return next_state

        # BFS initialization
        start_state = "".join(str(num) for row in board for num in row)
        visited = set()
        queue = collections.deque()
        queue.append(start_state)
        visited.add(start_state)
        move = 0

        # Start BFS
        while queue:

            for _ in range(len(queue)):

                curr_state = queue.popleft()

                if curr_state == "123450":
                    return move

                curr_index = curr_state.index("0")
                for next_index in directions[curr_index]:

                    next_state = swap(curr_state, curr_index, next_index)

                    if next_state in visited:
                        continue

                    visited.add(next_state)
                    queue.append(next_state)

            move += 1

        return -1

    def slidingPuzzle1(self, board: List[List[int]]) -> int:

        def swap(curr_state, i, j):
            s = list(curr_state)
            s[i], s[j] = s[j], s[i]
            next_state = "".join(s)
            return next_state

        directions = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4]
        ]
        visited = {}

        def dfs(curr_state, index_zero, num_move):

            if curr_state in visited and visited[curr_state] <= num_move:
                return

            visited[curr_state] = num_move

            for index_next in directions[index_zero]:
                next_state = swap(curr_state, index_zero, index_next)
                dfs(next_state, index_next, num_move + 1)

        # Start DFS
        start_state = "".join(str(num) for row in board for num in row)
        dfs(start_state, start_state.index("0"), 0)

        return visited.get("123450", -1)
