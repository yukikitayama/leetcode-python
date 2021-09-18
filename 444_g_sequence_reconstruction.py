from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:

        # print(f'org: {org}, seqs: {seqs}')

        # first for loop, second for loop => [first for loop][second for loop]
        # for seq in seqs:
        #     for x in seq:
        #         x
        # Make a set
        values = {x for seq in seqs for x in seq}
        # values = {x for x in seq for seq in seqs}
        # print(f'values: {values}')

        # Make a graph
        # Key: first element in seq in seqs, value: A list of second elements in seq in seqs
        graph = {x: [] for x in values}
        # print(f'graph: {graph}')
        # graph = defaultdict(list)

        # Key: second element in seq in seqs,
        # value: integer how many first elements in seq in seqs point at second element
        indegrees = {x: 0 for x in values}
        # print(f'indegrees: {indegrees}')

        # Make a directed graph
        for seq in seqs:

            for i in range(len(seq) - 1):

                graph[seq[i]].append(seq[i + 1])
                indegrees[seq[i + 1]] += 1

        # print(f'graph: {graph}')
        # print(f'indegrees: {indegrees}')

        # Find the first to vertex to start with
        # Vertices without the incoming edges are the vertices to start with
        queue = deque()
        for node, count in indegrees.items():
            if count == 0:
                queue.append(node)
        # print(f'queue: {queue}')
        # print()

        res = []

        while queue:

            # ?
            if len(queue) != 1:
                return False

            source = queue.popleft()

            # print(f'Current node: {source}')

            res.append(source)

            # print(f'res: {res}')

            for target in graph[source]:

                # print(f'In for loop, target: {target}')

                # Decrement because ?
                indegrees[target] -= 1

                # ?
                if indegrees[target] == 0:
                    queue.append(target)

                # print(f'indegrees: {indegrees}, queue: {queue}')

        return len(res) == len(values) and res == org


"""
Think integers in seqs are vertices in a directed graph
"""


org = [1,2,3]
seqs = [[1,2],[1,3]]
org = [1,2,3]
seqs = [[1,2],[1,3],[2,3]]
print(Solution().sequenceReconstruction(org, seqs))
