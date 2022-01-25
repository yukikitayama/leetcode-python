"""
- bottom-up recursion
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        ans = 0

        if not root:
            return ans

        def is_uni(node):

            nonlocal ans

            # Check leaf
            if not node.left and not node.right:
                ans += 1
                return True

            is_uni_boolean = True

            if node.left:
                is_uni_boolean = is_uni(node.left) and is_uni_boolean and node.left.val == node.val

            if node.right:
                is_uni_boolean = is_uni(node.right) and is_uni_boolean and node.right.val == node.val

            if is_uni_boolean:
                ans += 1

            return is_uni_boolean

        is_uni(root)

        return ans


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(5)
    print(Solution().countUnivalSubtrees(root))
