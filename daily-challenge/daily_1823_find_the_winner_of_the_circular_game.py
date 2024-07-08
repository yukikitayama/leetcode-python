import collections


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = collections.deque(range(1, n + 1))

        while len(circle) > 1:

            # Move the leave person at the front of the queue
            for _ in range(k - 1):
                circle.append(circle.popleft())

            # Leave the person
            circle.popleft()

        return circle[0]

    def findTheWinner2(self, n: int, k: int) -> int:
        circle = list(range(1, n + 1))
        curr = 0

        while len(circle) > 1:
            leave = (curr + k - 1) % len(circle)
            circle.pop(leave)
            curr = leave

        return circle[0]

    def findTheWinner1(self, n: int, k: int) -> int:
        in_game_array = [True] * n
        in_game_set = set([i for i in range(n)])
        curr = 0

        while len(in_game_set) > 1:
            for _ in range(k):
                curr = (curr + 1) % n
