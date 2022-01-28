"""
- Keep track of previous node while inorder traversal
- If previous is the p, the current node is the answer
"""


from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None

        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor


class SolutionWithoutBST:
    def __init__(self):
        self.previous = None
        self.inorder_successor_node = None

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':

        # Find the leftmost node at p.right
        if p.right:
            leftmost = p.right
            # Stop when current node doesn't have left child
            while leftmost.left:
                leftmost = leftmost.left
            self.inorder_successor_node = leftmost

        # Otherwise normal inorder traversal
        else:
            self.inorder_case2(root, p)

        return self.inorder_successor_node

    def inorder_case2(self, node: 'TreeNode', p: 'TreeNode'):

        print(f'inorder_case2, node: {node.val if node else None}')

        if not node:
            return

        # Recurse all the way to the left
        self.inorder_case2(node.left, p)

        print(f'  node.val: {node.val}')

        if self.previous == p and not self.inorder_successor_node:
            self.inorder_successor_node = node
            return

        self.previous = node

        print(f'  self.previous: {self.previous.val}')

        self.inorder_case2(node.right, p)


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    p = root.left
    # 2

    root = TreeNode(7)
    root.left = TreeNode(4)
    root.left.left = TreeNode(2)
    root.left.left.right = TreeNode(3)
    p = root.left
    # 7

    root = TreeNode(7)
    root.left = TreeNode(4)
    root.left.left = TreeNode(2)
    root.left.left.right = TreeNode(3)
    root.right = TreeNode(10)
    root.right.left = TreeNode(8)
    root.right.right = TreeNode(12)
    p = root
    # 8

    ans = Solution().inorderSuccessor(root, p)
    print(ans.val)
