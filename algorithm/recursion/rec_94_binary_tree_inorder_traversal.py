"""
- Inorder traversal
  - left, root, right
"""


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right

        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().inorderTraversal(root))
