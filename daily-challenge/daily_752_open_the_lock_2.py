"""
BFS
  neighbor is 8 patterns, up or down for 4 digits
  if neighbor is in deadends hashset,
    don't append it to queue
  when current lock is target, return step
"""

from typing import List
import collections


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        # Edge
        if "0000" in deadends:
            return -1

        deadends_set = set(deadends)

        def generate_neighbors(comb):
            ans = []

            for i in range(4):
                for j in [1, -1]:
                    curr = comb[:]
                    curr[i] = (curr[i] + j) % 10
                    ans.append(curr[:])

            return ans

        # print(generate_neighbors([0, 0, 0, 0]))

        queue = collections.deque()
        queue.append([0, 0, 0, 0])
        turns = 0
        visited = set()
        visited.add(tuple([0, 0, 0, 0]))

        while queue:

            for _ in range(len(queue)):
                curr_comb = queue.popleft()

                if "".join([str(num) for num in curr_comb]) == target:
                    return turns

                for neighbor in generate_neighbors(curr_comb):
                    if "".join([str(num) for num in neighbor]) not in deadends_set and tuple(neighbor) not in visited:
                        queue.append(neighbor)
                        visited.add(tuple(neighbor))

            turns += 1

        return -1
