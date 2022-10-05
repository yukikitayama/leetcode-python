"""
- BFS level order traversal
"""


from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            node = TreeNode(val=val)
            node.left = root
            return node

        queue = collections.deque()
        queue.append(root)

        curr_depth = 1
        while curr_depth < depth - 1:
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            curr_depth += 1

        while queue:

            curr_node = queue.popleft()

            tmp = curr_node.left
            new_node = TreeNode(val=val)
            curr_node.left = new_node
            curr_node.left.left = tmp

            tmp = curr_node.right
            new_node = TreeNode(val=val)
            curr_node.right = new_node
            curr_node.right.right = tmp

        return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(5)
    val = 1
    depth = 2
    print(Solution().addOneRow(root, val, depth))
