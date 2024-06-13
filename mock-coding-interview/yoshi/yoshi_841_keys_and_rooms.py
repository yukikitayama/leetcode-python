from typing import List
import collections


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        queue = collections.deque()
        queue.append(0)
        visited = set()
        visited.add(0)

        while queue:

            for _ in range(len(queue)):

                curr_room = queue.popleft()

                for next_room in rooms[curr_room]:
                    if next_room not in visited:
                        visited.add(next_room)
                        queue.append(next_room)

        return len(visited) == len(rooms)