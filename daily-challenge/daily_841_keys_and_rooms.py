from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = set([0])

        while stack:

            curr = stack.pop()

            if len(visited) == len(rooms):
                return True

            for next_room in rooms[curr]:
                if next_room not in visited:
                    visited.add(next_room)
                    stack.append(next_room)

        return False


if __name__ == '__main__':
    rooms = [[1], [2], [3], []]
    # True
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    # False
    print(Solution().canVisitAllRooms(rooms))
