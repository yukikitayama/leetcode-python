"""
- recursion
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        # Below recursion stops when val reaches the None
        # that time, root is the node before leaf, so insert the TreeNode(val) to the child
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        # Eventually return root, but in recursion root is the current node
        return root


"""
- Let h be the height of tree, and time is O(h)
  - That is, O(log n) because in every level, it reduces the number of nodes to search by half
"""


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
val = 5
# root = []
# val = 5
ans = Solution().insertIntoBST(root, val)
print(ans.val)
print(ans.left.val, ans.right.val)
print(ans.left.left.val, ans.left.right.val, ans.right.left.val, None)


