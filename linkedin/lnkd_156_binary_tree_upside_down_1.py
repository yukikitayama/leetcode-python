"""
- level order traversal
- keep prev level and current level
- left child's right to prev node
- left child's left to the right child
-
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Stop recursion at the deepest leftmost node
        if not root or not root.left:
            return root

        new_root = self.upsideDownBinaryTree(root.left)
        # connect parent's right to left child's left
        root.left.left = root.right
        # connect parent to left child's right
        root.left.right = root
        # In the middle of the recursion, temporarily set None, but the recursion stack will connect
        # At the end of recursion, correctly set the leaf to be None
        root.left = None
        root.right = None

        # Every recursion stack return the new_root that this function needs to return
        # But other nodes are updated
        return new_root






"""
    1
   / \
  2   3
 / \
4   5
udbt(TreeNode(1)),

  if: F, udbt(TreeNode(2)),

    if: F, udbt(TreeNode(4)),

      root.left: None, if: T, return root: TreeNode(4)

    newRoot: TreeNode(4), root.right: TreeNode(2).right = TreeNode(5), root.left.left: TreeNode(4).left,
    TreeNode(4).left: TreeNode(5), root.left.right: TreeNode(4).right = TreeNode(2), TreeNode(2).left: None,
    TreeNode(2).right: None, return newRoot: TreeNode(4)

  newRoot: TreeNode(4), root: TreeNode(1), root.right: TreeNode(1).right = TreeNode(3),
  root.left.left: TreeNode(2).left = TreeNode(3), root.left.right: TreeNode(2).right = TreeNode(1),
  root.left: TreeNode(1).left = None, root.right: TreeNode(1).right = None, return newRoot: TreeNode(4)

return TreeNode(4)


root: TreeNode(2), newRoot: TreeNode(4), root.right: TreeNode(5), root.left.left: TreeNode(4).left = TreeNode(5),
root.left.right: TreeNode(4).right = TreeNode(2),
"""


