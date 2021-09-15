from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # Why convert to set?
        deletes = set(to_delete)
        res = []
        self.helper(root, False, deletes, res)
        return res

    def helper(self, root, hasParent, deletes, res):
        # When recursion reaches the leaf
        if not root:
            return None

        if root.val in deletes:
            # Delete the current node, so its children won't have a parent, so pass False below
            root.left = self.helper(root.left, False, deletes, res)
            root.right = self.helper(root.right, False, deletes, res)
            # Delete the current Node, so this node's parent won't have a child (This node), pass None to a parent
            return None

        # When current node is not deleted, it means that its children has a parent,
        # so the below helper function use True
        else:
            # TreeNode which needs to go to answer list is something isolated,
            # meaning it doesn't have parent node, so it's not connected with others by that
            if not hasParent:
                res.append(root)

            root.left = self.helper(root.left, True, deletes, res)
            root.right = self.helper(root.right, True, deletes, res)
            # The below only works when current node is a root because it was originally root in the binary tree,
            # or by deleting nodes, current node became a root.
            return root


"""
Time complexity
Let n be the number of nodes in the binary tree
O(n) because it traverses all the nodes

Space complexity
O(n) for delete set
"""