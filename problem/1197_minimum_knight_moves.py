from collections import deque


class Solution:
    def __init__(self):
        # Knight 8 possible moves
        self.offsets = [
            (1, 2), (2, 1), (2, -1), (1, -2),
            (-1, -2), (-2, -1), (-2, 1), (-1, 2)
        ]

    def minKnightMoves(self, x, y):
        return self.bfs(x, y)

    def bfs(self, x, y):
        visited = set()
        # Use deque.append to append to right side, and deque.popleft to pop from left side for FIFO
        # We start from already visited origin (0, 0)
        queue = deque([(0, 0)])
        # steps tell us the minimum number of steps
        steps = 0

        while queue:

            # Potentially we need to visit all the locations in queue, we get len(queue) to visit all in for loop
            curr_level_cnt = len(queue)
            print(f'curr_level_cnt: {curr_level_cnt}, '
                  f'queue: {queue}')

            # Finishing for loop of current level means we finish this level, so we increment steps outside of for loop
            for _ in range(curr_level_cnt):

                curr_x, curr_y = queue.popleft()
                print(f'curr_x: {curr_x}, curr_y: {curr_y}')

                # If we reach the goal
                if (curr_x, curr_y) == (x, y):
                    return steps

                # Try all the possible knight moves
                for offset_x, offset_y in self.offsets:
                    next_x, next_y = curr_x + offset_x, curr_y + offset_y
                    print(f'  next_x: {next_x}, next_y: {next_y}')

                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        queue.append((next_x, next_y))

            steps += 1


sol = Solution()
# test = {'x': 5, 'y': 5}
test = {'x': 2, 'y': 1}
answer = sol.minKnightMoves(x=test['x'], y=test['y'])
print(f'Answer: {answer}')
