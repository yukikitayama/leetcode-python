import collections


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        directions = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]

        queue = collections.deque()
        queue.append((0, 0))
        visited = set()
        ans = 0

        while queue:

            for _ in range(len(queue)):

                curr_x, curr_y = queue.popleft()

                if (curr_x, curr_y) == (x, y):
                    return ans

                for offset_x, offset_y in directions:
                    next_x = curr_x + offset_x
                    next_y = curr_y + offset_y

                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        queue.append((next_x, next_y))

            ans += 1


if __name__ == '__main__':
    x = 2
    y = 1
    x = 5
    y = 5
    print(Solution().minKnightMoves(x, y))
