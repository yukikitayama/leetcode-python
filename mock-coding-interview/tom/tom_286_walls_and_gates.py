from typing import List
import collections


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited = set()
            visited.add((r, c))
            distance = 0

            while queue:

                for _ in range(len(queue)):

                    curr_r, curr_c = queue.popleft()

                    if distance > 0 and rooms[curr_r][curr_c] > distance:
                        rooms[curr_r][curr_c] = distance

                    for offset_r, offset_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        next_r = curr_r + offset_r
                        next_c = curr_c + offset_c

                        if 0 <= next_r < len(rooms) and 0 <= next_c < len(rooms[0]):
                            if rooms[next_r][next_c] not in [-1, 0] and (next_r, next_c) not in visited:
                                queue.append((next_r, next_c))
                                visited.add((next_r, next_c))

                distance += 1

        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                # Gate
                if rooms[r][c] == 0:
                    # BFS
                    bfs(r, c)