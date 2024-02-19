from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return root

        lefts = []
        rights = []

        def boundary(node, is_left):

            # Terminate if leaf
            if not node.left and not node.right:
                return

            if is_left:
                lefts.append(node.val)
                if node.left:
                    boundary(node.left, is_left)
                else:
                    boundary(node.right, is_left)
            else:
                rights.append(node.val)
                if node.right:
                    boundary(node.right, is_left)
                else:
                    boundary(node.left, is_left)

        if root.left:
            boundary(root.left, True)

        if root.right:
            boundary(root.right, False)
            rights.reverse()

        # Leaves
        leaves = []

        def collect_leaves(node):
            if not node.left and not node.right:
                leaves.append(node.val)

            if node.left:
                collect_leaves(node.left)
            if node.right:
                collect_leaves(node.right)

        if root.left or root.right:
            collect_leaves(root)

        print(f"lefts: {lefts}")
        print(f"leaves: {leaves}")
        print(f"rights: {rights}")

        return [root.val] + lefts + leaves + rights