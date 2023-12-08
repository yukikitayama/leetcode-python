from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []

        def preorder(node):

            if not node:
                return

            ans.append(str(node.val))

            if node.left:
                ans.append("(")
                preorder(node.left)
                ans.append(")")

            if not node.left and node.right:
                ans.append("()(")
                preorder(node.right)
                ans.append(")")
            elif node.right:
                ans.append("(")
                preorder(node.right)
                ans.append(")")

        preorder(root)

        return "".join(ans)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)

    print(Solution().tree2str(root))

