from typing import List
import collections


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = collections.defaultdict(list)

        for i in range(len(pid)):
            parent = ppid[i]
            child = pid[i]
            if parent:
                graph[parent].append(child)

        # print(f'graph: {graph}')

        ans = []

        queue = collections.deque([kill])

        while queue:

            curr = queue.popleft()

            ans.append(curr)

            for child in graph[curr]:
                queue.append(child)

        return ans


if __name__ == '__main__':
    pid = [1, 3, 10, 5]
    ppid = [3, 0, 5, 3]
    kill = 5
    kill = 3
    print(Solution().killProcess(pid, ppid, kill))
