"""
- First make graph
  - {tree_node_val: [[val, 'L'], [val, 'R'], ...]}
- BFS
- Time N, Space N
"""


from typing import Optional
import collections
import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = collections.defaultdict(list)
        queue = collections.deque([root])

        while queue:

            for _ in range(len(queue)):

                node = queue.popleft()

                if node.left:
                    graph[node.val].append([node.left.val, 'L'])
                    graph[node.left.val].append([node.val, 'U'])
                    queue.append(node.left)

                if node.right:
                    graph[node.val].append([node.right.val, 'R'])
                    graph[node.right.val].append([node.val, 'U'])
                    queue.append(node.right)

        # pprint.pprint(graph)

        queue = collections.deque([(startValue, '')])
        visited = set()
        visited.add(startValue)

        while queue:

            for _ in range(len(queue)):

                curr_val, curr_path = queue.popleft()

                if curr_val == destValue:
                    return curr_path

                for next_val, direction in graph[curr_val]:
                    if next_val not in visited:
                        visited.add(next_val)
                        queue.append((next_val, curr_path + direction))


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(4)
    startValue = 3
    destValue = 6
    print(Solution().getDirections(root, startValue, destValue))
