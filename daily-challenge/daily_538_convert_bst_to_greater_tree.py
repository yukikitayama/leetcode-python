"""
- Find total
- Inorder traversal to compute cumulative sum
- Total minus cumulative sum up to previous
- Time O(2N), Space O(N)

- Reverse inorder traversal
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Gave up morris traversal
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        node = root

        while node:
            if not node.right:
                total += node.val
                node.val = total
                node = node.left

            else:
                succ = get_successor(node)

                if succ.left is None:
                    succ.left = node
                    node = node.right


class Solution2:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        node = root
        stack = []
        while stack or node:

            while node:
                # When node is left, it goes to bottom of stack and top is right
                # So we can process right first
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            node = node.left

        return root


class Solution1:
    def __init__(self):
        self.total = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root


if __name__ == '__main__':
    pass
