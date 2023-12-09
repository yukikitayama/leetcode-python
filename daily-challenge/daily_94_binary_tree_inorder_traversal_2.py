from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []

        def inorder(node):

            if not node:
                return

            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)

        inorder(root)

        return ans


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    root = None

    print(Solution().inorderTraversal(root))
