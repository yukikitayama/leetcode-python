"""
- make bank list a set
-
"""


from typing import List
import collections


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        queue = collections.deque()
        queue.append((start, 0))
        seen = set(start)

        while queue:
            node, step = queue.popleft()

            if node == end:
                return step

            for c in 'ACGT':
                for i in range(len(node)):
                    next_node = node[:i] + c + node[i + 1:]
                    if next_node in bank and next_node not in seen:
                        queue.append((next_node, step + 1))
                        seen.add(next_node)

        return -1


if __name__ == '__main__':
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    print(Solution().minMutation(start, end, bank))
