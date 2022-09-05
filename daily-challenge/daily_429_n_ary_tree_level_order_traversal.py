from typing import List
import collections


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []

        ans = []

        queue = collections.deque()
        queue.append(root)

        while queue:

            curr_level = []

            for _ in range(len(queue)):

                curr_node = queue.popleft()

                curr_level.append(curr_node.val)

                if curr_node.children:

                    queue.extend(curr_node.children)

            ans.append(curr_level)

        return ans


if __name__ == '__main__':
    node1 = Node(1)
    node3 = Node(3)
    node2 = Node(2)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    root = node1
    root.children = [node3, node2, node4]
    root.children[0].children = [node5, node6]
    ans = Solution().levelOrder(root)
    print(ans)
