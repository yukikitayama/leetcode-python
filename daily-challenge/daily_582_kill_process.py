from typing import List
import collections
import pprint


class Node:
    def __init__(self, val=0):
        self.val = val
        self.children = []


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        map_ = collections.defaultdict(Node)
        for id_ in pid:
            node = Node(val=id_)
            map_[id_] = node

        # print(map_)

        for i in range(len(ppid)):
            if ppid[i] > 0:
                # Get Node as parent
                par = map_[ppid[i]]

                # Get child
                chi = pid[i]

                # Append child as Node
                par.children.append(map_[chi])

        # for k, v in map_.items():
        #     print(f'Node: {k} with children')
        #     for c in v.children:
        #         print(f'  {c.val}')

        ans = [kill]

        def recursion(node):
            for c in node.children:
                ans.append(c.val)
                recursion(c)

        recursion(map_[kill])

        return ans


if __name__ == '__main__':
    pid = [1, 3, 10, 5]
    ppid = [3, 0, 5, 3]
    kill = 5
    pid = [1]
    ppid = [0]
    kill = 1
    print(Solution().killProcess(pid, ppid, kill))
