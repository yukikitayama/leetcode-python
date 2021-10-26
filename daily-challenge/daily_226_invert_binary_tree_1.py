"""
- root = root
- root.left = root.right
- root.right = root.left
  - root.left.val = root.right.val
  - root.left.left = root.right.right
  - root.left.right = root.right.left

  - root.right.val = root.left.val
  - root.right.left = root.left.right
  - root.right.right = root.left.left

- preorder recursion
- Time O(n)

- Recursively visit each node
  - swap left and right child
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


"""

"""


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
ans = Solution().invertTree(root)
print(ans.val)
print(ans.left.val)
print(ans.right.val)
print('None' if not ans.left.left else ans.left.left.val)
print(ans.left.right.val)
print(ans.right.left.val)
print(ans.right.right.val)





