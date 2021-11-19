"""
- Recursion DFS to find left and right boundary
- Use iterative BFS to find leaves

- Use recursion
  - Inorder traversal to find leaves, put them into list
  - If left, left traversal, unless it's
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        def is_leaf(node):
            return not node.left and not node.right

        def add_leaves(node):
            if is_leaf(node):
                ans.append(node.val)
            else:
                if node.left:
                    add_leaves(node.left)
                if node.right:
                    add_leaves(node.right)

        ans = []

        if not root:
            return ans

        # Add root
        if not is_leaf(root):
            ans.append(root.val)

        # Add left boundary
        t = root.left
        while t:
            if not is_leaf(t):
                ans.append(t.val)

            if t.left:
                t = t.left
            else:
                t = t.right

        # Add leaves
        add_leaves(root)

        # Add right boundary
        stack = []
        t = root.right
        while t:
            if not is_leaf(t):
                stack.append(t.val)

            if t.right:
                t = t.right
            else:
                t = t.left
        while stack:
            ans.append(stack.pop())

        return ans


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
print(Solution().boundaryOfBinaryTree(root))
