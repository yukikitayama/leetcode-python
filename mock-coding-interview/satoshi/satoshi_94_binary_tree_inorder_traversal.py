from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        def inorder(node):

            if node:

                left = inorder(node.left)

                if left:
                    ans.append(left.val)

                ans.append(node.val)

                right = inorder(node.right)

                if right:
                    ans.append(right.val)

        inorder(root)

        return ans